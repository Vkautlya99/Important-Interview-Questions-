# Write a program to print the occurence of the each characters in a string 

# The question is about finding the occurrence of characters in a string.

# Iterate through the string and count the occurrence of each character.

# Use a hash table to store the count of each character.

# Consider the case sensitivity of the characters.

# Handle special characters and spaces as required.


# METHOD :- 1
from collections import Counter

def Occurrence_of_each_Character_in_a_String(string):
    return dict(Counter(string))

string = "helper"
print(Occurrence_of_each_Character_in_a_String(string))


# METHOD :- 2

def Occurence_of_each_Character_in_a_String(string):
    count = {}
    for char in string :
       if char in count :
          count[char] += 1
       else :
          count[char] = 1
    return count 

string = "helper"                 #TC :- O(n)

print(Occurence_of_each_Character_in_a_String(string))    # SC :- O(m)


