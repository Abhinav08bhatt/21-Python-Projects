from time import sleep
from random import randint
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_key():
    style("\n\nPress ENTER to ROLL THE DIE...")
    input()

def style(s,n=0.03):
    '''
    nothing, just attention to details
    :param s: string input
    :param n: speed of text (default 0.04)
    '''
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

def int_input(s):
    style(s)
    try :
        x = int(input("\n> "))
        return x
    except :
        style("\nWrong input\n\n")
        return int_input(s)
    
def game_outline():
    '''
    return :
    number of player
    the final winning score
    '''
    num = int_input("Enter the number of players : (1-5) - ")
    end = int_input("Enter the winning score - ")
    return num,end

def roll_die():
    '''
    1 and 6 are included
    '''
    return randint(1,6)

def outcome_1():
    style("\n\nUh-oh... the die landed on 1.\n")
    style(f"You ran out of Luck. This round ends with  points.\n")


def outcome_others(points):
    style("\n\nLucky roll!\n")
    style(f"You earned {points} points from this outcome.\n")

def player_input(score):
    bet = int_input("Enter the number of times u want to roll the die - ")
    chance_score = 0
    for chance in range (1,bet+1):
        press_key()
        outcome = roll_die()
        style(f"The outcome was : {outcome}")
        if outcome == 1 :
            outcome_1()
            chance_score = 0
            break    
        else :
            outcome_others(outcome)
            chance_score += outcome
    print("\n")
    style(f"You earned {chance_score} points in this round!!!\n")
    score += chance_score
    style(f"Final score is now : {score}\n")



def score_calculator(score):
    # 2,3,4,5,6 : adds to score
    # 1 : score = 0
    pass

def ui():
    pass

def game():
    pass

if __name__ == "__main__":
    player_input(0)