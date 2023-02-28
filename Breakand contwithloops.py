# # break the whole loop

for i in range (12):
    if (i==11):
        break
    print("5 X",i+1, "=", 5 +i *5)

print("Leave the table")

#JUST SKIP THE ITERATION

for i in range (10):
    if( i == 8):
        print("Skip the iteration of 5 X",i)
        continue
    print("5 X",i+1, "=", 5 +i *5)

print("It will skip the iteration of 5X9 in the table")

#STIMULATING DO WHILE LOOP IN PYTHON True

while True:
    n = int(input("Enter number :"))
    print(n)
    if not n > 0:
     break
print("Loop ended")

#EXAMPLE 2

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break

print("loop is ended")