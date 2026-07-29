tests = int(input())
for i in range(tests):
    n = int(input())
    k = int(input())

    nums = []
    j = 1
    while(len(nums) <= k):
        if (j % n != 0):
            nums.append(j)
        j +=1
    nums = tuple(nums)
    print(nums[k-1])