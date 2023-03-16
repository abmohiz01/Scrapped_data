print("*******************************************")
print("           Welcome to Inbox Rupees")
print("*******************************************")
name = str(input("Enter your Name :"))
print("Welcome  to Win Game Sir",name)


user = str(input("Are you ready to Earn some cash. Yes/No :"))
if user == "yes" and "Yes":
    print("Lets go")
else:
    print("Come back later")


question1 = [
            ["Which of the following is not an operating system?"],

            ["What is the maximum length of the filename in DOS?"],
            ["When was the first operating system developed?" ],
            ["Which of the following is the extension of Notepad?"],
            ["what else a command interpreter is called"]
             ]
answer1 = [ ["Windows", "Linux", "Oracle", "DOS","none"],
            ['4', "5", "8", "12"],
            ["1941", "1949", "1950" ,"1950"],
            [".txt","xls","ppt","bmp"],
            ["prompt","kernel","shell","command" ]

            ]



levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0


for i in range(0, len(question1)):

    questions = question1[i]
    answers = answer1[i]
    '''MAKING QUESTION LIST STARTING FROM 1 INDEX'''
    print(f"Question {i +1} is {questions}")
    print(f"\n\nQuestion for Rs. {levels[i]}")
    '''PRINTING ANSWERS'''
    print(f"a. {answers[0]}          b. {answers[1]} ")
    print(f"c. {answers[2]}          d. {answers[3]} ")
    '''TAKING THEIR REPLIES FROM USER'''
    reply = int(input("enter from 1 - 4"))
    if reply == 2:
        print(f"correct {answers[2]} You have won {levels[i]}")
        money = levels[i]
        continue



    else:

        print("Wrong")
        print(f"The amount you are taking home is: {money} ")
        break

