# import classes 
from deck import Deck
from players import Player
from rule import Ruler

# input players
player_names = eval(input("Enter name of players as a list: "))  

# create Player objects
PlayerList = [Player(name) for name in player_names]

# make currentDeck and passedDeck
currentDeck = Deck(6, 11)
passedDeck = Deck(0, 0)

# run the game for 15 rounds
for round_num in range(1, 16):
    print(f"\nRound {round_num}")
    prez = input("Enter the president: ")
    chanz = input("Enter the chancellor: ")
    policy = input("Enter the policy passed (L/F): ")

    Ruler(prez, chanz)                
    currentDeck.update(policy, -1)   
    passedDeck.update(policy, 1)
