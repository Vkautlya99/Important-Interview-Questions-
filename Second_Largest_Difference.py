# We have given a integer array then find the second maximum difference

def Second_Maximum_difference(array):
  max1 = max2 = float("-inf")
  min1 = min2 = float("inf")
  
  for num in array :
    if num > max1:
       max2 = max1
       max1 = num
    elif num > max2:
       max2 = num
 
    
    if num < min1 :
      min2 = min1 
      min1 = num 
    elif num < min2 :
      min2 = num 
  
  diff1 = max1 - min2 
  diff2 = max2 - min1
  return max(diff1, diff2)

array = [2,4,1,6,9,22,10] 
print(Second_Maximum_difference(array))





