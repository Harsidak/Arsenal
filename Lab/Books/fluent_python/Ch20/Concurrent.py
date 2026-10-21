"""
Fluent Python (2nd Edition) — Chapter 20: Concurrent Executors
=============================================================
Comprehensive Summary & Executable Notes on `concurrent.futures`

TOPICS COVERED:
1. Overview: Concurrency vs. Parallelism & The GIL
2. The `Future` Object Lifecycle & Key Methods
3. Pattern 1: `executor.map` (Order-preserving)
4. Pattern 2: `executor.submit` + `futures.as_completed` (Completion-order)
5. Handling Exceptions in Concurrent Tasks
6. `ThreadPoolExecutor` vs `ProcessPoolExecutor` (I/O-bound vs CPU-bound)
7. Sizing Thread & Process Pools
8. The Classic "Flags" Download Pattern from the Book
"""

from concurrent import futures
import math
import os
import time
from typing import Callable, Iterable, List, Tuple


# ============================================================================
# 1. CORE CONCEPTS & THE GIL
# ============================================================================
"""
- Concurrency: Dealing with lots of things at once (interleaving tasks, e.g. waiting for network).
- Parallelism: Doing lots of things at once (running simultaneously on multiple CPU cores).
- Python GIL (Global Interpreter Lock):
  * Only one OS thread can execute Python bytecode at any given moment.
  * ThreadPoolExecutor releases the GIL during I/O operations (network, disk, time.sleep,
    and C-extensions like NumPy/OpenCV), making it great for I/O-bound tasks.
  * ProcessPoolExecutor bypasses the GIL completely by spawning separate OS processes,
    each with its own Python interpreter and GIL (ideal for CPU-bound tasks).
"""


# ============================================================================
# 2. THE ANATOMY OF A `Future` OBJECT
# ============================================================================
"""
A `Future` represents the eventual result of an asynchronous computation.
You rarely instantiate them directly; executors create and manage them for you.

Essential Future methods:
- `future.done()` -> bool: Non-blocking; returns True if completed or cancelled.
- `future.cancelled()` -> bool: Returns True if successfully cancelled before execution.
- `future.cancel()` -> bool: Tries to cancel task (fails if already executing).
- `future.result(timeout=None)` -> Result: Blocks until finished; returns result or raises exception.
- `future.exception(timeout=None)` -> Exception or None: Returns exception raised by callable.
- `future.add_done_callback(fn)`: Attaches a callback executed when future completes.
"""
 

# ============================================================================
# 3. MOCK WORKLOADS (I/O-BOUND vs CPU-BOUND)
# ============================================================================

def mock_download(item_id: str, delay: float = 1.0) -> str:
    """Simulates an I/O-bound network call (like downloading a country flag)."""
    # print(f"[{item_id}] Starting download (takes {delay:.1f}s)...")
    time.sleep(delay)
    if item_id == "FAIL":
        raise ConnectionError(f"Simulated network drop for {item_id}")
    return f"Downloaded-{item_id}"


def cpu_heavy_task(n: int) -> int:
    """Simulates a CPU-bound task (heavy math computation)."""
    # Prime factorization / heavy check
    count = 0
    for i in range(2, n):
        if all(i % d != 0 for d in range(2, int(math.isqrt(i)) + 1)):
            count += 1
    return count


# ============================================================================
# 4. PATTERN 1: `executor.map`
# ============================================================================
def demo_executor_map() -> None:
    """
    `executor.map(fn, *iterables, timeout=None)`:
    - High-level, drop-in replacement for built-in `map()`.
    - Key Trait: Returns results in the SAME ORDER as the inputs, regardless
      of which task finished first!
    - Caveat: If any task raises an exception, the exception is raised when
      you iterate up to that item from the returned generator.
    """
    print("\n--- 1. Demo: executor.map (Preserves Input Order) ---")
    items = ["BR", "CN", "IN", "US", "ID"]
    delays = [1.5, 0.5, 1.0, 0.2, 0.8]  # Note US (0.2s) finishes fastest

    start_time = time.perf_counter()
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        # executor.map submits all tasks and yields results in input order
        results = executor.map(mock_download, items, delays)
        
        for item, result in zip(items, results):
            elapsed = time.perf_counter() - start_time
            print(f"[{elapsed:4.2f}s] Received result for {item}: {result}")


# ============================================================================
# 5. PATTERN 2: `executor.submit` + `futures.as_completed`
# ============================================================================
def demo_as_completed() -> None:
    """
    `executor.submit(fn, *args, **kwargs)` & `futures.as_completed(fs)`:
    - Low-level, maximum flexibility.
    - Submit returns a `Future` immediately.
    - `as_completed(futures_list)` yields futures as soon as they FINISH,
      independent of submission order (fastest first).
    - Best for:
      * Different callables or heterogeneous arguments.
      * Progressive UI updates / progress bars (e.g. tqdm).
      * Immediate response handling as results arrive.
    """
    print("\n--- 2. Demo: submit + as_completed (Yields in Completion Order) ---")
    items = [("BR", 1.5), ("CN", 0.5), ("IN", 1.0), ("US", 0.2), ("ID", 0.8)]

    start_time = time.perf_counter()
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Map each future back to its metadata if needed
        future_to_item = {
            executor.submit(mock_download, code, delay): code
            for code, delay in items
        }

        for future in futures.as_completed(future_to_item):
            code = future_to_item[future]
            try:
                res = future.result()
                elapsed = time.perf_counter() - start_time
                print(f"[{elapsed:4.2f}s] Completed: {code} -> {res}")
            except Exception as exc:
                print(f"[{code}] generated an exception: {exc}")


# ============================================================================
# 6. PATTERN 3: ERROR HANDLING IN CONCURRENT TASKS
# ============================================================================
def demo_error_handling() -> None:
    """
    Exceptions in concurrent workers:
    - Never raised at submit time!
    - Stored inside the `Future` object until `.result()` is invoked.
    - Always wrap `future.result()` in try/except inside `as_completed()`.
    """
    print("\n--- 3. Demo: Error Handling with as_completed ---")
    items = [("US", 0.3), ("FAIL", 0.4), ("IN", 0.2)]

    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_map = {
            executor.submit(mock_download, code, delay): code
            for code, delay in items
        }

        for future in futures.as_completed(future_map):
            code = future_map[future]
            try:
                res = future.result()
                print(f"Success: {code} -> {res}")
            except ConnectionError as err:
                print(f"Handled error for [{code}]: {err}")


# ============================================================================
# 7. THREADS VS. PROCESSES: CHOOSING THE RIGHT EXECUTOR
# ============================================================================
def demo_process_pool() -> None:
    """
    `ProcessPoolExecutor` vs `ThreadPoolExecutor`:
    - ThreadPool:
      * Low memory overhead, fast startup.
      * Ideal for I/O bound (HTTP requests, database calls, disk reads).
      * Default `max_workers = min(32, (os.cpu_count() or 1) + 4)`
    - ProcessPool:
      * Bypasses Python's GIL.
      * Real multi-core parallelism for CPU-bound computations.
      * Memory overhead: Each process duplicates/initializes interpreter state.
      * Arguments and return values MUST BE PICKLABLE (serialized via IPC).
      * Default `max_workers = os.cpu_count()`
      * CRITICAL on Windows: Must be guarded with `if __name__ == '__main__':`!
    """
    print("\n--- 4. Demo: ProcessPoolExecutor for CPU-Bound Work ---")
    workload = [8000, 10000, 12000, 15000]

    # Run with ProcessPoolExecutor across available CPU cores
    start = time.perf_counter()
    with futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_heavy_task, workload))
    duration = time.perf_counter() - start

    print(f"Computed primes count for {workload}")
    print(f"Results: {results}")
    print(f"Time taken with {os.cpu_count()} CPU cores: {duration:.3f}s")


# ============================================================================
# 8. BOOK SPECIFIC: THE "FLAGS" DOWNLOAD ARCHITECTURE
# ============================================================================
"""
Fluent Python Ch 20 uses the 'flags' example to benchmark:
1. Sequential (baseline): 1 worker downloading one flag at a time.
2. ThreadPoolExecutor: Concurrent HTTP requests.
3. asyncio (Ch 21 comparison): Single-threaded cooperative multitasking.

The typical ThreadPool pattern from the book:

```python
POP20_CC = 'CN IN US ID BR PK NG BD RU MX PH VN ET EG DE IR TR CD FR GB'.split()

def download_many(cc_list: list[str]) -> int:
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))
```
"""


# ============================================================================
# 9. SUMMARY CHEAT SHEET
# ============================================================================
"""
+-----------------------------+----------------------------------------------+
| Requirement                 | Recommended Approach                         |
+-----------------------------+----------------------------------------------+
| Same function, many items,  | `executor.map(fn, iterable)`                 |
| preserve input order        |                                              |
|                             |                                              |
| Asynchronous completion,    | `executor.submit()` +                        |
| custom args, progress bar   | `futures.as_completed(futures_list)`         |
|                             |                                              |
| Network, HTTP, Disk, I/O    | `futures.ThreadPoolExecutor(max_workers=...)`|
|                             |                                              |
| CPU, Math, Image processing | `futures.ProcessPoolExecutor(max_workers=...)`|
|                             |                                              |
| Windows requirement         | MUST protect top-level code with             |
|                             | `if __name__ == '__main__':`                 |
+-----------------------------+----------------------------------------------+
"""


if __name__ == "__main__":
    print(f"Running Concurrency Demos (System CPUs: {os.cpu_count()})...")
    demo_executor_map()
    demo_as_completed()
    demo_error_handling()
    demo_process_pool()
