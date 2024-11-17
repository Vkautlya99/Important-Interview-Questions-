# Find maximum (or minimum) sum of a subarray of size k

# This type of question is solved by Sliding Window approach.

def Maximum_Subarray_Sum(arr, k):
   if len(arr) < k :
      return "Array length is small"
    
   current_sum = sum(arr[:k])
   max_sum = current_sum

   for i in range(k, len(arr)):
      current_sum = current_sum - arr[i - k] + arr[i]
      max_sum = max(max_sum , current_sum)

   return max_sum

k = 4
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(Maximum_Subarray_Sum(arr, k))        # TC :- O(n), # SC :- O(1)
