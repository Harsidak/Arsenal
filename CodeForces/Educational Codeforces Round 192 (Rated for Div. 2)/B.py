testcase = int(input().strip())

for _ in range(0,testcase):
    n = int(input().strip())
    a = list(map(int, input().split()))

    score = []
    m = 0
    for i in range(0,n):
        if a[i] in (1,2):
            m += 1
        else:
            m -= 1
        
        score.append(m)

        score = []

    max_h = 0
    high = -999999
    for i in range(n-2, 0, -1):
        high =  max(high, score[i])
        max_h[i] = high 
        score.append(m)

    can = False
    crrrr = 0
    for i in range(n-2):
        currr += 1 if a[i] == 1 else -1
        if currr >= 0 and high[i + 1] >= score[i]:
            can = True
            break
    if score <= 0:
        print("NO")
    else:
        print("YES")
            
            
