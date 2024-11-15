# Write a program to find the second smallest number in an array


def second_smallest_element_in_Array(arr):
    smallest = min(arr)
    second_smallest = max(arr)

    for num in arr :
       if num < second_smallest and num != smallest:
          second_smallest = num 
    return second_smallest

arr = [5,1,6,2,9,7,4,3]                                                # TC :- O(n)
print(second_smallest_element_in_Array(arr))                           # SC :- O(1)















