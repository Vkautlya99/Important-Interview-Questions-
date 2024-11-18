# WAP to print the last non repeating character in a string 

def Last_Non_Repeating_Character(string):
   for i in range(len(string) - 1, -1, -1):
      if string.count(string[i]) == 1:
         return string[i]
   return None 

string = "Vikram"
print(Last_Non_Repeating_Character(string))



