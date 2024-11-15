
# WAP to find maximum count of 1s in and array

def Maximum_Count(array):
   count = 0
   res = 0

   for i in range(len(array)):
      if array[i] == 0:
         count = 0
      else :
          count += 1
          res = max(res , count)
   return res 


array = [0,1,0,0,1,1,1,0,1,0,0]            # TC :- O(n)
print(Maximum_Count(array))                # SC :- O(1)










