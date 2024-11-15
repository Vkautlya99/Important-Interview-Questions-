# Maximum DifferenceYou are given an array 'ARR' of the 'N' element. Your task is to find the maximum difference between any of the two elements from 'ARR'. If the maximum difference is even print "EVEN" without quotes. If the maximum difference is odd print "ODD" without quotes. For example:Given 'ARR' = [1, 10, 5, 2, 8, 1], answer is "ODD". Here the maximum difference is between 10 and 1, 10-1 = 9



def Maximum_Difference_Even_or_Odd(array):
   min_element = float("inf")
   max_element = float("-inf")

   for num in array :
      if num < min_element :
        min_element = num 
      if num > max_element:
        max_element = num 
   diff = max_element - min_element

   if diff % 2 == 0:
     return "EVEN"
   else :
     return "ODD"

array = [11,2,3,4,5,6,7,8,9]
print(Maximum_Difference_Even_or_Odd(array))










