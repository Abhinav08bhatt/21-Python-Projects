from random import randint
from time import sleep
import os

def clear():
    '''
    to clear the terminal for a better console UI
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def style(s,n=0.04):
    '''
    nothing, just attention to details
    :param s: string input
    :param n: speed of text (default 0.04)
    '''
    for i in range (0,len(s)):
        print(s[i],end='')
        sleep(n)

def valid_in():
    '''
    takes the different inputs but find the closest and return : r for rock , p for paper and s for scissors 
    possibilities : r R rock ROCK Rock rk rock (so we will focus on starting word...if its and ask the user if the user if they mean it)
    '''
   
    while True:
        user = input("\n\nEnter your side : ").lower()
        if user[0]=='r':
            if user == 'r' or user =='rock':
                user = 'r'
                return user
            else:
                ask = input("Did you mean ROCK ? (y/n) : ")
                if ask == 'y':
                    user = 'r'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        elif user[0]=='p':
            if user == 'p' or user =='paper':
                user = 'p'
                return user
            else:
                ask = input("Did you mean PAPER ? (y/n) : ")
                if ask == 'y':
                    user = 'p'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        elif user[0]=='s':
            if user == 's' or user =='scissors':
                user = 's'
                return user
            else:
                ask = input("Did you mean SCISSORS ? (y/n) : ")
                if ask == 'y':
                    user = 's'
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
        else:
            style("\nummm, we could not guess your input.\nTry Again...",0.02)
            sleep(2)

def ui():
    pass

def game():

    style(f"\nROCK{'.'*3}",0.02)
    sleep(0.5)
    style(f"PAPER{'.'*3}",0.02)
    sleep(0.5)
    style(f"SCISSORS{'.'*3}",0.02)
    sleep(0.5)
    user = valid_in()
    print(user)

if __name__ == "__main__":

    # l = ["a","b","c"]
    # print(l[randint(0,2)])
    # pass

    game()
