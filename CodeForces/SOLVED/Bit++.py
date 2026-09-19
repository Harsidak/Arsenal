n = int(input().strip())
count = 0

for i in range(n):
    Operation = input().strip()
    if 'X' in Operation:
        if "++" in Operation:
            count += 1
        if "--" in Operation:
            count -= 1

print(count)