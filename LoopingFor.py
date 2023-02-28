# name = 'ABMOHIZ'
# for i in name:
#     print(i)
#     if (i == 'B'):
#         print("This is Special")

# colors = ["Red", "green", "blue", "black"]
# for colour in colors:
#     print(colour)
#
#     for i in colour:
#         print(i)

# for k in range(10 ,15,1):
#     print(k + 1)

# for k in range(1,2000):
#     print(k + 1)

# FOR LOOP WITH ELSE
# INTERVIEW QUESTION
#
# for i in range(8):
#     print(i)
#     if(i == 6):
#         break
# else:
#     print("Out of loop")


#PRINT THE LARGEST NUMBER:
largest = 0
a = [2,34,55,66,98,12,23]
for num in a:
    if num > largest:
        largest = num
        print ("the largest number is",num)
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", smallest)
print("Smallest:", smallest)
