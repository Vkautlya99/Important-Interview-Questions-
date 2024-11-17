# Sliding Window Maximum (Maximum of all subarrays of size K)

# Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.
from collections import deque 

def Maximum_of_all_subarrays(arr, k):
   res = []
   dq = deque()
   n = len(arr)

   for i in range(n):
    # Removing out of index bound
      while dq and dq[0] < i - k + 1:
         dq.popleft()

    # Removing Smaller Elements
      while dq and arr[dq[-1]] < arr[i]:
         dq.pop()

    # The suarray of size k will be in decresing order 
      dq.append(i)

    # Appending Maximum of the subarray in the result
      if i >= k-1 :
        res.append(arr[dq[0]])
   return res 

k = 3
arr = [1,2,3,1,4,2,4,5,2,3,5]
print(Maximum_of_all_subarrays(arr, k))     # TC :- O(n), # SC :- O(k)
                                       