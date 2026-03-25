Matrix = [list(map(int,input().strip().split())) for i in range(0,5)]
x = y = 0
for i in range(0,5):
    found = False
    for j in range(0,5):
        if Matrix[i][j] == 1:
            x = i
            y = j
            found = True
            break
    if found:
            break
total = abs(x-2) + abs(y-2)
print(total)