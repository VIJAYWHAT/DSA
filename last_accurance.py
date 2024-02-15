def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    i=1
    while low <= high:
        mid = (low + high) // 2

        print(f"Iteration no: {i}")
        print(f"low = {low} --- > mid = {mid} --- > high = {high}\n")

        if arr[mid] == target:
            while mid < len(arr) - 1 and arr[mid + 1] == target:
                mid = mid + 1
            return mid
        
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        i += 1
        
    return -1


arr = [2,3,5,6,7,7,9,13,16]
target = 7

index = binary_search(arr,target)
print(index)
