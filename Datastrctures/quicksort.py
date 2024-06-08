def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
 
array = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(array)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
   