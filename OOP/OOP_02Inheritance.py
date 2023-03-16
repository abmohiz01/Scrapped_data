# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#
#     def show(self):
#         print(f"Name of employee is:{self.name} an id is:{self.id}")
#
# class Programmer(Employee):
#
#     def language(self):
#         print("TYhe language is python")
#
# e1 = Employee("Abmohiz",7)
# e1.show()
# e2 = Programmer("Google",1998)
# e2.show()
# e2.language()

# class Player:
#     '''a player in a shooter game'''
#
#     def blast(self,enemy):
#         print("The player blast an enemy.\n ")
#         enemy.die()
#
# class Alien:
#
#     def die(self):
#         print("The Alien gasps and says , Oh this is it ,This is the big one\n\
#                Yes its getting dark now.")
#
#
# hero = Player()
# invader = Alien()
# hero.blast(invader)
#
# input("\n\nPress the enter key")

#Playing Cards
#Demonstrates combinig objects

'''CREATING THE CARD CLASS'''

class Card:

    Ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    Suits = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

'''CREATING THYE HAND CLASS'''

class Hand:

    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<empty>"
        return rep
    def clear(self):
        self.cards = []

    def __add__(self, card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    '''USING CARD OBJECTS'''

card1 = Card(rank= "A", suit= "c")
print(f"Printing a card object :{card1}")
card2 = Card(rank= "2", suit= "c")
print(f"Printing a card object :{card2}")
card3 = Card(rank= "3", suit= "c")
print(f"Printing a card object :{card3}")
card4 = Card(rank= "4", suit= "c")
print(f"Printing a card object :{card4}")
card5 = Card(rank= "5", suit= "c")
print(f"Printing a card object :{card5}")

'''COMBINING CARD OBJECTS USING A HAND OBJECT'''

my_hand = Hand()
print(f"My hand before I add any cards:",my_hand)
my_hand.__add__( card1 )
my_hand.__add__( card2 )
my_hand.__add__( card3 )
my_hand.__add__( card4 )
my_hand.__add__( card5 )

print(f"My hand after I add any cards:",my_hand)
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nGive the first two cards from my hand to your hand")
print(f"Your hand {your_hand}:")
print(f"My hand {my_hand}:")
my_hand.clear()
print(f"\n My hand clearing it :{my_hand}")


