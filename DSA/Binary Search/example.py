data = [i for i in range(1,101)]

num_search = int(input("Enter the number you want to search: "))

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        
        else:
            low = mid + 1
    return None


print(binary_search(data,num_search))