N = 5
arr = [8, 3, 7, 9, 2]
M = 3
require = [5, 7, 9]

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

arr.sort()
for req in require:
    if binary_search(arr, req, 0, N-1):
        print("yes")
    else:
        print("no")
