# Write a program to print the Equilateral triangle start pattern.

def Equilateral_Star_Triangle_Pattern(row):
   for i in range(1, row + 1):
      print(" " * (row - i) + "*" * (2 * i - 1))

row = 5
Equilateral_Star_Triangle_Pattern(row) 




