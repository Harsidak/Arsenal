n,k = map(int,input().strip().split())
scores = list(map(int,input().strip().split()))
count = 0

threshold = scores[k-1]

for i in scores:
    if i >= threshold and i>0:
        count+=1
print(count)
