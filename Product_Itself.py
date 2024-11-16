# Product except Itself 

def Product_itself(arr):
    product = [1] * len(arr)

    for i in range(len(arr)):
       for j in range(len(arr)):
         if i != j:
           product[i] *= arr[j]
    return product

arr = [1,2,3,4,5]               # TC :- O(n^2)
print(Product_itself(arr))      # SC :- O(1)







