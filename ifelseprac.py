# #Using IFELSE
age = int(input("Enter the number"))
if(age > 18):
    print("You can drive")
elif(age == 18):
    print("good age to drive  but be careful")
elif (age >= 10):
    print("Wait a little more")
elif (age <= 0):
    print("No driving Kid")
else:
    print("Stay home")



#Nested IF

x =20

if x < 10:
  print("Above ten,")
if x >= 20:
    print("your license Will expire after 5 years")

else:
    print("but not above 20.")
