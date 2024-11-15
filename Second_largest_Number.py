# Write a program to find the second largest number in an array


def Second_Largest_Number_in_Array(arr):
   largest = max(arr)
   second_largest = min(arr)

   for num in arr :
      if num > second_largest and num != largest:
         second_largest = num
   return second_largest

arr = [9,3,1,5,8,3,7,4]
print(Second_Largest_Number_in_Array(arr)) 









