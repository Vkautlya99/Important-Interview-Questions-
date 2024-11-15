# Write a program to print the Opposite Equilateral triangle start pattern.


def Opposite_Equilateral_Star_Triangle(row):
    for i in range(row, -1, -1):
      print(" " * (row - i) + "*" * (2 * i - 1))


row = 5 
Opposite_Equilateral_Star_Triangle(row)     






