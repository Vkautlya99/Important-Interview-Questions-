# Count characters Write a program to count and print the 
# total number of characters (lowercase english alphabets only), 
# digits (0 to 9) and white spaces (single space, tab i.e. '\t' and newline i.e. '\n') 
# entered till '$'. That is, input will be a stream of characters 
# and you need to consider all the characters which are 
# entered till '$'. Print count of characters, count of digits and count of white spaces respectively 


def Count_Of_Char_Digit_Space(text):
    char_count = 0
    digit_count = 0
    space_count = 0

    for char in text :
       if char == "$" :
          break 
       if "a" <= char <= "z":
          char_count += 1
       elif "0" <= char <= "9":
          digit_count += 1
       elif char == " " or char == "\t" or char == "\n":
          space_count += 1
    print(char_count, digit_count, space_count)

text = "a b1c 2d3"  
Count_Of_Char_Digit_Space(text)









