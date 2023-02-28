# Write a python program to translate a message into secret code language. Use the rules below to translate
# normal English into secret code language

# Coding:
# if the word contains at  least 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

def code(str):
    str = (input("Enter your word :"))
    app = ''
    # ran = 'abs234cdjklfksmvalkflzcm232489ifnj'
    S = 3

    if len(str) == 3:
        print(str)

    result = ''.join((random.choice(string.ascii_lowercase) for x in range(S)))
    # run loop until the define length
    print(" Random string generated in Lowercase: ", result)
    app = result + (str[-2:len(str)]) + (str[0]) + result
    print(app)

    else:











