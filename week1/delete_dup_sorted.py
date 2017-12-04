# Challenge 1 - Deleting duplicates from a sorted array
# This problem is concerned with deleting repeated elements from a sorted array.

# Write a program which takes as input a sorted int[] and updates it such that:

# all duplicates have been removed and
# all remaining valid elements have been shifted left to fill the emptied indices
# all remaining empty indices have values set to 0
# the function returns the number of remaining valid elements (the array size minus the number of removed elements)
# For example, given an input array with the values {2,3,5,5,7,11,11,11,11,13}, after the function completes, the values in the array should be {2,3,5,7,11,13,0,0,0}, and the function should return 6.

# Hint: There is an O(n) time and O(1) space solution.

def delete_dup(sorted_arr, length):
    print(sorted_arr)
    result_arr = sorted_arr[0:1]
    index = 0
    for i, item in enumerate(sorted_arr):
        if i > 0 and sorted_arr[i] != sorted_arr[i-1]:
          result_arr.append(sorted_arr[i])
          index += 1

    for i in range(index, length):
        result_arr.append(0)

    return result_arr

sorted_arr = [2,3,5,5,7,11,11,11,11,13]
print(delete_dup(sorted_arr, 10))
