def get_smallest(arr):
  position = 0
  smallest = arr[position]
  for idx, item in enumerate(arr):
    if item < smallest:
      smallest = item
      position = idx    
  return position

def selection_sort(arr):
  newCol = []
  while arr:
    smallest = get_smallest(arr)
    newCol.append(arr.pop(smallest))
  return newCol

arr = [10, 11, 7, 20, 6, 23, 25, 30, 5, 8, 9, 3, 2, 1, 12, 13, 4, 0]
print selection_sort(arr)