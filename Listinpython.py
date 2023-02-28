marks = [5,6,7,"Abmohiz",88,99,100]
print(marks)
#LIST INDEX
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[5])

#List NEGATIVE INDEXING
print(marks[5-2])
print(marks[-2])
#Making Positive
print(marks[len(marks)-2])
if 7 in marks:
    print("yes")
else:
    print("No")
if "Ab" in "Abmohiz":
    print("Hey ABMOHIZ")

#jumping Indexing
print(len(marks))
print(marks[0:7:2])

#LIST COMPREHENSION
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

#METHODS of LIST
list1 = [ i for i in range(10)]
list1.append(8)
list1.sort()
list1.sort(reverse = True)
list1.insert(2,34)
list2 = [22,33,44,55,66,77]
list1.extend(list2)
list1.sort(reverse = True)
print(list1)

tup = (1,2,3,"abmohiz",77,True)
#tup[0]=90 It will display an error
print(tup)
if 77 in tup:
    print("Yesi it is")

tup2 = tup[1:4]
print(tup2)
y=list(tup)
y.append(99)
print(y)