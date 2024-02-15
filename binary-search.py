def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    i=1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:    
            return mid
        
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        i += 1
    
    return -1


arr = [2,3,5,6,7,7,9,13,16]
target = 7

Index = binary_search(arr,target)
print(Index)
