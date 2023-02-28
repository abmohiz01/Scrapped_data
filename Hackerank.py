# IF ELSE PROGRAM FROM hacker rank
# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

# n = 3
#
#
# if  n % 2 != 0:
#     print("Weird")
# elif(n % 2 == 0 and n in range(2,5)):
#     print("Not weird")
# elif(n % 2 == 0 and n in range(1,6)):
#     print(" Weird")
# if(n % 2 == 0 and n > 20):
#     print("Not Weird")

# n = int(input().strip())
# if n%2 != 0:
#     print("Weird")
# else:
#     if n >=2 and n <= 5:
#         print("Not Weird")
#     elif n >=6 and n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")

# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# s = a + b
# print(s)
# m = a - b
# print(m)
# p = a * b
# print(p)
i=0
n =4

for i in range(n):
    if (n > 0):
        print(i**2)


