# We have given a integer find the sum of all digits

def Sum_of_the_given_integer(num):
   sum = 0
   for char in num :
      sum = sum + int(char)
   return sum 


num = "12345"                                      # TC :- O(n)
print(Sum_of_the_given_integer(num))               # SC :- O(1)



