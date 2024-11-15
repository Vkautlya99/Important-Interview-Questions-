
# Write a program to find the leap year between start and end year 


def Leap_year_between_start_and_end(start, end):
    for year in range(start, end):
       if(year % 4 == 0 and year % 400 != 0) or (year % 100 == 0):
          print(year)

start = 2000
end = 2024 
Leap_year_between_start_and_end(start, end)




