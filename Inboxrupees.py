print("*******************************************")
print("           Welcome to Inbox Rupees")
print("*******************************************")
name = str(input("Enter your Name :"))
print("Welcome  to Win Game Sir",name)
# raise error here

user = str(input("Are you ready to Earn some cash. Yes/No :"))
if user == "yes" and "Yes":
    print("Lets go")
else:
    print("Come back later")



# q1 = ["Which of the following is not an operating system?"]
#
# a1 = ["Windows", "Linux", "Oracle", "DOS"]
#
#
#
# q2 = ["What is the maximum length of the filename in DOS?"]
#
# a2 = ['4', "5", "8", "12 :"]
#
#
#
#
# q3 = ["When was the first operating system developed?" ]
# a3 =["1941", "1949", "1950" ,"1950"]
#
#
#
# q4 = ["Which of the following is the extension of Notepad?"]
# a4 = [".txt","xls","ppt","bmp"]
#
#
#
# q5 = ["what else a command interpreter is called"]
# a5 = ["prompt","kernel","shell","command" ]
#
# questions = ([q1],[q2], [q3], [q4], [q5])
# answers = ([a1],[a2],[a3],[a4],[a5])
# levels = [1000, 2000, 3000, 4000,5000]
# money = 0
# for i in range(0, len(questions)):
#
#     question = questions[i]
#     print(f"\n\nQuestion for Rs. {levels[i]}")
#     print(f"a. {answers[0]}          b. {answers[1]} ")
#     print(f"c. {answers[2]}          d. {answers[3]} ")
#     reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
#     if (reply == 0):
#         money = levels[i - 1]
#         break
#     if (reply == question[-1]):
#         print(f"Correct answer, you have won Rs. {levels[i]}")
#         if (i == 4):
#             money = 10000
#         elif (i == 9):
#             money = 320000
#         elif (i == 14):
#             money = 10000000
#     else:
#         print("Wrong answer!")
#         break
#
# print(f"Your take home money is {money}")
#
#
#



questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[:]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = levels[i - 1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")



