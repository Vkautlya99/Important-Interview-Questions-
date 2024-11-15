# Sort a Binary array without using two pointers 

# Method : Two pointer Ap

def Binary_Array_Sorting(arr):
    left = 0
    right = len(arr) - 1
    while left < right :
       while arr[left] == 0 and left < right :
          left += 1
       while arr[right] == 1 and left < right :
          right -= 1
       if left < right :
          arr[left], arr[right] = arr[right], arr[left]
          left += 1
          right -= 1
    return arr

arr = [1,1,0,0,1,0,0,1,0,1]                          #TC = O(n)
print(Binary_Array_Sorting(arr))                     #SC = O(1)




