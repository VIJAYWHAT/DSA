def find_index(arr, target):
    if target not in arr:
        return "number not found"
    else:
        return arr.index(target)

arr = [5, 17, 18, 18, 18, 19, 25]
target = 18

index = find_index(arr, target)
print(index)
