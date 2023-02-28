# Program 1
# a = int(input("Enter the number"))
# print(a)
#
# while(a <= 38):
#     a = int(input("Enter the number"))
#     print(a)
#
# print("Done with the loop")

#Program

# count = int(input("enter a number"))
# while(count > 0):
#     print(count)
#     count = count -1
# print("Blast off")
# print(count)
# n = 0
# while True:
#     if n == 3:
#         break
#     print(n)
#     n = n + 1
# n1 = 0
# while n1>0:
#     print("Leather ")
#     print("blast off  ")
#     print("her ")
#
#
# for i in [2,1,5]:
#     print(i)
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)