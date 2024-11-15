# Find first non repeated character in string

def First_Non_repeating_Character(string):
    count = {}
    for char in string :
       if char in count :
          count[char] += 1
       else :
          count[char] = 1
    for char in string :
       if count[char] == 1:
          return char 
    return "No repeated characters are there"

string = "vilolo"                                            # TC = O(n)
print(First_Non_repeating_Character(string))                 # SC = O(1)









