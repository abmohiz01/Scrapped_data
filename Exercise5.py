'''https://github.com/abmohiz01'''
'''Snake water game'''
import random
def game():


    rounds = 10
    Game = ['Snake ', 'Water', 'Gun']
    # Points = ['Win', 'Draw','Lose',]
    player1_point = 0
    player2_point = 0
    # player1 = ''
    # player2 = ''

    print("1 is for Snake \n"
      "2 is for Water \n"
      "3 is for Gun\n ")

    while rounds <= 1:

        print(f"Round left {rounds}")
        player2 = random.choice(Game)
        print(f"Player 2 choses {player2}")



        player1 = int(input("Enter from 1 to 3 :"))
        if player1 == 1:
            print(f"Our player choses {Game[0]}")

        elif player1 == 2:
            print(f"Our player choses {Game[1]}")

        elif player1 == 3:
            print(f"Our player choses {Game[2]}")




        if player1 == Game[0]:
            if player2 == Game[1]:
                player1_point += 1
        elif player2 == Game[2]:
            player2_point += 1



        elif player1 == Game[1]:

            if player2 == Game[2]:

                player1_point += 1

            elif player2 == Game[0]:

                player2_point += 1



        elif player1 == Game[2]:

            if player2 == Game[0]:

                player1_point += 1

            elif player2 == Game[1]:

                player2_point += 1

    rounds -= 1
    if player1_point > player2_point:  # if user wins
        print(f"WOOUUH! You have win \nYour_point = {player1_point}\nComputer_point = {player2_point}")
    elif player2_point > player1_point:  # if computer wins
        print(
            f"WE RESPECT YOUR HARD WORK, BUT YOU LOSE AND YOU ARE A LOSER NOW! \nYour_point = {player1_point}\nComputer_point = {player2_point}")
    elif player2_point == player1_point:  # if match draw
        print(f"MATCH DRAW\nYour_point = {player1_point}\nComputer_point = {player2_point}")
    else:  # just checked
        print("can't calculate score")

    exit = input("PRESS ENTER TO EXIT")

a= game()
print(a)





'''USING DICTIONARY'''
