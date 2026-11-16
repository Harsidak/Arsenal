import sys

def prob(n: int, k: int, v: int) -> int:
    total = 0
    current = v

    while(current > 0):
        total += current
        current = current // k

    if(total >= n):
        return 0
    else:
        return -1

def bs(n: int, k: int) -> int:
    left = 0
    right = n
    ans = n

    while(left <= right):
        mid = (left + right)//2
        if(prob(n, k, mid) == 0):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def main():
    input_data = sys.stdin.read().splitlines()
    n, k = map(int, input_data[0].split())
    print(bs(n, k))

if __name__ == "__main__":
    main()