testcase = int(input().strip())

for _ in range(0,testcase):
    k = int(input().strip())
    li = list(map(int, input().split()))

    twin = 0
    can_build = False

    for j in range(0,len(li)):

        if li[j] >= 3:
            can_build = True
        elif li[j] >=2:
            twin += 1
            
            if twin >= 2:
                can_build = True
                break
    
    if can_build:
        print("YES")
    else:
        print("NO")

            
