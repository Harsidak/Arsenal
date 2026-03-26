n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

total = sum(coins)
your_sum = 0
count = 0

for coin in coins:
    your_sum += coin
    count += 1
    if your_sum > total - your_sum:
        break

print(count)