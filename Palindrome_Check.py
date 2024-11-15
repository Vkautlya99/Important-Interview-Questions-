# String Palindrome : Given a string, determine if it is a palindrome, considering only alphanumeric characters. 


# METHOD :- 1


def alpha_palindrome(String):
   filtered_String = " ".join(char.lower() for char in String if char.isalnum())
   return filtered_String == filtered_String[::-1]

String = "A man, a plan, a canal: Panama"     # TC :- O(n)
print(alpha_palindrome(String))               # SC :- O(n)




def Alphanumeric_Palindrome(string):
    left = 0
    right = len(string) - 1
    
    while left < right :
       while left < right and not string[left].isalnum():
          left += 1
       while left < right and not string[right].isalnum():
          right -= 1
       if string[left].lower() != string[right].lower():
          return False 
       left += 1
       right -= 1
    return True 

string = "A man, a plan, a canal: Panama"            # TC :- O(n)
print(Alphanumeric_Palindrome(string))               # SC :- O(1)
















