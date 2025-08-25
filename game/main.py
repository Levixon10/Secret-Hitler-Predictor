# import classes 
from deck import Deck
from players import Player
from rule import Ruler

#function returns number of ways of choosing 2 objects from num objects
def Choose2(num):
    return (num*(num-1))//2

# input players
player_names = eval(input("Enter name of players as a list: "))  

# create Player objects
PlayerDict = {name: Player(name) for name in player_names}


# make currentDeck and passedDeck
currentDeck = Deck(6, 11)
passedDeck = Deck(0, 0)

# run the game for 15 rounds
round_num=1
while True:
    print(f"\nRound {round_num}")
    prez = input("Enter the president: ")
    chanz = input("Enter the chancellor: ")
    policy = input("Enter the policy passed (L/F): ")

    Ruler.voting(prez, chanz)                
    
    #Assigning probabilities
    p_1,p_half,p_minushalf,p_minus1=0,0,0,0
    q_1,q_half,q_minushalf,q_minus1=0,0,0,0
    if policy=="L":
        p_1=max(Choose2(currentDeck.fascistRem)/Choose2(currentDeck.Rem),0)
        p_half=max(currentDeck.fascistRem*currentDeck.liberalRem/Choose2(currentDeck.Rem),0)
        q_half=max((p_half+p_1)/2,0)
    else:
        p_minus1=max(Choose2(currentDeck.liberalRem)/Choose2(currentDeck.Rem),0)
        p_minushalf=max(currentDeck.fascistRem*currentDeck.liberalRem/Choose2(currentDeck.Rem),0)
        q_minushalf=max((p_minus1+p_minushalf)/2,0)
    
    PlayerDict[prez].assignMarks(p_1,p_half,p_minushalf,p_minus1)
    PlayerDict[chanz].assignMarks(q_1,q_half,q_minushalf,q_minus1)

    currentDeck.change(policy, -1)   
    passedDeck.change(policy, 1)
    print(f"Round : {round_num}")
    for player in PlayerDict:
        print(f"Current marks of {player} : {PlayerDict[player].Marks} ")
    run=input("Is the game going to continue?[Y/N]")
    if run=="N":
        break

    round_num+=1


