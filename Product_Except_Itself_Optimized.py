# Optimized source code of Product except itself 

def Product_Except_Itself(arr,n):
   zeros = 0
   product = 1
   res = [0] * n

   for num in arr :
      if num == 0:
        zeros += 1
      else:
        product *= num
    
   for i in range(n):
       if zeros > 1:
          res[i] = 0
       elif zeros == 1 :
          if arr[i] == 0:
            res[i] = product
          else :
            res[i] = 0
       else :
          res[i] = product // arr[i]   
   return res

n = 5
arr = [10, 3, 5, 6, 2]
print(Product_Except_Itself(arr, n)) 



