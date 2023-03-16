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
    print(str)
    app = ''
    # ran = 'abs234cdjklfksmvalkflzcm232489ifnj'


    if len(str) == 3:

        '''FOR GENERATING REANDOM STRING'''
        result = ''.join((random.choice(string.ascii_lowercase)for x in range(3)))
        # run loop until the define length
        print(" Random string generated in Lowercase: ", result)
        '''FIRST WORD TO THE END  '''
        print("Appended string :",(str[-2:len(str)]) + (str[0]))
        '''ADDED RANDOM STRING AT FIRST AND LAST'''
        app = result + (str[-2:len(str)]) + (str[0]) + result
        print(app)
    else:
        print(str[::-1])


def decode(str):

    '''TAKING INPUT OF THE ENCODED WORD '''
    str = (input("ENTER THE ENCODED STRING YOU RECIEVED :"))
    print(str)
    app = ''
    deco = ''
    # ran = 'abs234cdjklfksmvalkflzcm232489ifnj'

    if len(str) == 3:
        print(str[::-1])

    else:
        '''REMOVING FRIST AND LAST 3 CHARACTERS'''
        app = (str[3:-3])
        print(app)
        deco = app
        '''SLICING THE STRINGS BY REMOVING LAST AND ADDING IT TO THE FIRST INDEX'''
        decoding1 = (deco[0:-1])
        print(f"The decoded word is :{deco[2] + decoding1}")

'''CALLING FUNCTIONS'''
code("hello")
decode("hello")












