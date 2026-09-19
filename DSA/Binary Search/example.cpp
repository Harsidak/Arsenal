#include <bits/stdc++.h>
using namespace std;

// Fast I/O for Codeforces
void fast_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

// ---------------------------------------------------------
// 1. Binary Search the Answer (Integer BSTA)
// ---------------------------------------------------------

// Check function that returns true if 'mid' is a valid solution
bool check(long long mid) {
    // Write your problem-specific logic here
    return true; 
}

// Finding the MINIMUM possible value that satisfies check()
// Pattern: F F F F T T T -> find the first T (e.g., minimize cost/time)
long long bs_minimize(long long low, long long high) {
    long long ans = -1; // Keep track of the best answer found
    while (low <= high) {
        long long mid = low + (high - low) / 2; // Prevents integer overflow
        if (check(mid)) {
            ans = mid;
            high = mid - 1; // Try to find a smaller valid value
        } else {
            low = mid + 1;  // Try larger values
        }
    }
    return ans;
}

// Finding the MAXIMUM possible value that satisfies check()
// Pattern: T T T T F F F -> find the last T (e.g., maximize speed/efficiency)
long long bs_maximize(long long low, long long high) {
    long long ans = -1;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;  // Try to find a larger valid value
        } else {
            high = mid - 1; // Try smaller values
        }
    }
    return ans;
}

// ---------------------------------------------------------
// 2. Binary Search on Doubles (Real Values)
// ---------------------------------------------------------
double bs_double(double low, double high) {
    // Run for a fixed number of iterations (e.g., 80 to 100) to ensure high precision
    // and avoid infinite loops due to precision issues
    for (int iter = 0; iter < 80; ++iter) {
        double mid = low + (high - low) / 2.0;
        if (check(mid)) {
            // Adjust bounds based on whether you want to minimize or maximize
            low = mid; 
        } else {
            high = mid;
        }
    }
    return low; // or high depending on target
}

// ---------------------------------------------------------
// 3. Built-in C++ STL Reference
// ---------------------------------------------------------
void stl_reference_example() {
    vector<int> v = {1, 2, 4, 4, 5, 6, 8};
    
    // Check if element exists
    bool exists = binary_search(v.begin(), v.end(), 4); // returns true
    
    // First element >= target (lower_bound)
    auto it_lb = lower_bound(v.begin(), v.end(), 4);
    int idx_lb = distance(v.begin(), it_lb); // Index of first 4 -> 2
    
    // First element > target (upper_bound)
    auto it_ub = upper_bound(v.begin(), v.end(), 4);
    int idx_ub = distance(v.begin(), it_ub); // Index of first element > 4 (i.e. 5) -> 4
}

int main() {
    fast_io();
    
    // Your Codeforces solution structure:
    /*
    int t;
    cin >> t;
    while (t--) {
        // Read input
        // Solve using bs_minimize or bs_maximize
    }
    */
    
    return 0;
}