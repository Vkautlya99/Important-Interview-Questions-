
# WAP to find the nearest prime number of a given number and it can be before of after of the input number/given number 


def is_prime(n):
   if n <= 1 :
      return False
   for i in range(2 , (n // 2) + 1):
      if n % i == 0 :
         return False 
   return True   

def Nearest_prime(n):
   prime = 0
   for i in range(n - 1 , 1 , -1):
       if is_prime(i):
          prime = i
          break 
   return prime 

n = 103                          # TC :- O(n^2)
print(Nearest_prime(n))          # SC :- O(1)
       
   
