
# write a program to finf that the input year is leap year or not using one if statement. 


def Is_leap_year(year):
   if (year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0)):
      return True
   else :
      return False 

year = int(input())
print(Is_leap_year(year))







