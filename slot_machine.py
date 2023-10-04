"""
David Roebrts
CS152
December 1
CS152 B
"""

"""
This is a slot machine game almost identical to it's real life counterpart.
After running the game the results will appear
After each game the visual window must be closed for it to properly update"""

import random
from tkinter import *
import matplotlib.pyplot as plt

def window(midleft,midmid, midright):
    """Function to visualize the results of each round in tkinter.
    In the future, I will replace the text with actual pictures and make the userinterface more sophisticated"""
    root = Tk()
    label1 = Label(root,text = "Slot Machine Game")
    label1.grid(row=0,column=0)
    x = StringVar()
    x.set(midleft)
    y = StringVar()
    y.set(midmid)
    z = StringVar()
    z.set(midright)

    label2 = Label(root, textvariable=x)
    label2.grid(row=15,column=5)
    label3 = Label(root, textvariable=y)
    label3.grid(row=15,column=10)
    label4 = Label(root, textvariable=z)
    label4.grid(row=15,column=15)
    root.mainloop() 
    

def Results(player_money,rounds):
    """Function to print the results of the game on a spreadsheet in exel
    Takes in the number of rounds and players money during that round as inputs"""
    #open file titled Player Records and appened data in it
    fp = open("Player Record.csv", 'a')
    
    fp.write(str(player_money) +  "," + str(rounds) + "\n")
    fp.close()


def PlottingResults():
    """Function that uses matplotlib to graph results of game
    Tkes in the Results functions spreadsheet to graph"""
    fp = open("Player Record.csv", 'r')
    line = fp.readline()
    for line in fp:
        words = line.split(",") 
        x = int(words[1])
        y = int(words[0])
        plt.plot(x, y,"o")
    plt.title(player_name + " " + "Results")
    plt.xlabel("Rounds")
    plt.ylabel("Player Money")
    plt.show()


def clearfile():
    """Function to clear the file made from the Results function after every game
    Keeps the resulting graph clean"""
    fp = open("Player Record.csv", "w")
    fp.close()


def main():
    """Main function where game takes place
    Uses severlal other independent functions to keep data organized"""
    icons = ["Grape","Lemon","SEVEN", "Cherry", "Apple"]
    
    print("Welcome money cow- I mean elegant player to this wonderful slotmachine game.")
    print("*This game in no way endorses real life gambling, this is just a simulation.*")
    player_money = 1000
    print("Create a player name")
    global player_name      #create global variable that can be used later on when plotting graph
    player_name = input()
    print("Player name:", player_name)
    print(player_name+ " starts with:", player_money)
    
    while True:
        counter=1
        while player_money>0:
            
        
            print("Current Funds:", player_money)
            
            try:
                bet_amount = int(input("How much would you like to bet?:"))
            except:
                print("only integer values")
                continue
            if bet_amount>player_money:
                print("Not Enough Money")
            else:
                Results(player_money,counter)

                player_money-=bet_amount
                topleft = random.choice(icons)
                topmid= random.choice(icons)
                topright= random.choice(icons)
                midleft= random.choice(icons)
                midmid= random.choice(icons)
                midright= random.choice(icons)
                bottomleft= random.choice(icons)
                bottommid= random.choice(icons)
                bottomright= random.choice(icons)
                counter += 1
                print()
                print("|",topleft,"|","|",topmid,"|","|",topright,"|")
                print('___________________________________')
                print("|",midleft,"|","|",midmid,"|","|",midright,"|")
                print('___________________________________')
                print("|",bottomleft,"|","|",bottommid,"|","|",bottomright,"|")
                #window(midleft, midmid, midright)
                print(counter)
                JackPot = 1000 + (100 * counter)
                if midleft == midmid and midmid == midright and midleft == "SEVEN":
                    print("You Hit The Jack Pot")
                    player_money += bet_amount + JackPot
                    print("Updated Player Money:", player_money)
                elif midleft == midmid and midmid == midright:
                    print("you won")
                    player_money += bet_amount*2
                    print("Updated Player Money:",player_money)
                else:
                    print("So ya lost did ya? Then I'll be pocketin' your wager")
                    print("Thanks fer playin' mate")
                    
                    
                    if player_money == 0:
                        print("Game Over Out of Money")
                        return Results(player_money,counter), PlottingResults(), clearfile()
                              
if __name__ == "__main__":
    main()

