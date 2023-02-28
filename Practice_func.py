#USING FUNCTION COMPUTE THE PAY
# def computepay(hours, rate):
#     print(f"In Company you worked {hours} hours at the rate of {rate}")
#     if hours>40:
#         reg = rate * hours
#         total = (hours - 40.0) * (rate * 0.5)
#         pay = reg + total
#     else:
#         pay = hours * rate
#
#     return pay
#
# sh = float(input("Enter hours in float :"))
# sr = float(input("Enter rate in float :"))
# xp = computepay(sh,sr)
# print("Your Pay is :",xp)

#FIND WEATHER THE YEAR IS LEAP YEAR OR NOT :
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# def is_leap(year):
#     leap = False
#     if (year % 4  == 0):
#         leap = True
#         if (year % 100 == 0):
#             leap = False
#             if( year % 400 == 0):
#                 leap = True
#     return leap
# for i in range(6):
#     xp = int(input("Enter year :"))
#
#     cp = is_leap(xp)
#     print('This year is :',cp)

n = int(input("Enter a number"))

for i in range(0,n):
    g = i + 1

    print(str(g))
