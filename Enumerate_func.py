# ENUMERATE FUNCTION

# marks = [12, 33, 44, 55, 99, 23, 76, 88]
#
# for index,mark in enumerate(marks):
#     print(f"The index is : {index} and the corresponding marks is : {mark}")
#     if index == 4:
#         print("well Done Ab you got in this subject",mark)

# CHANGING THE INDEX FROM 0 TO 1, IT WILL START FROM 1 IF I:
marks = [12, 33, 44, 55, 99, 23, 76, 88]

for index, mark in enumerate(marks, start = 1):
    print(f"The index is : {index} and the corresponding marks is : {mark}")
    if index == 5:
        print("well Done Ab you got in this subject", mark)
width = 15
height = 12.0
print(height/3)

