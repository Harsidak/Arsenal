n = int(input())
presents = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    result[presents[i] - 1] = i + 1
print(*result)
