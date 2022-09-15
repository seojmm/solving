import sys
import collections
input = sys.stdin.readline

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
sorted = [-1]*len(arr)

def quickSort(arr, start, end):
  if start >= end:
    return
  
  pivot = start
  i, j = start+1, end

  while i <= j:
    while i <= end and arr[i] <= arr[pivot]:
      i += 1
    while j > start and arr[j] >= arr[pivot]:
      j -= 1
    
    if i > j:
      arr[pivot], arr[j] = arr[j], arr[pivot]
    else:
      arr[i], arr[j] = arr[j], arr[i]
  
  quickSort(arr, start, j-1)
  quickSort(arr, j+1, end)

