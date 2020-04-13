'''**********************************
*                                   *
*       Code by Etienne Naude       *
*                                   *
**********************************'''

#import and global variables
from random import seed
from random import random
from random import randint
current = 0
chance = []
chest =[]
squares=[]
ID = 0
total_rounds = 100000000
current_round = 0

#class structure for squares(tiles) on the board
class square:
    global ID
    name = ""
    hits = 0
    modifier = 0
    ID_num =ID
    probality = 0.000
    def __init__(self,name ="", modifier ="none"):
        global ID
        self.modifier =modifier 
        self.name =name
        self.ID_num = ID
        ID +=1

    def inc(self):
        self.hits +=1

    def get_hit(self):
        return "self.hits"

    def set(self,name,mod = "none"):
        self.name = name
        self.modifier = mod
    def get_prob(self):
        global current,squares,chest,chance,current_round,total_rounds
        self.probality = round(self.hits/current_round*100,3)
        return self.probality

    def __str__(self):
        self.get_prob()
        return "** {}: {}% \t: {} **".format(self.ID_num,self.probality, self.name)

#class structure for chance and community chest cards
class card:
    title =""
    move = None

#initailize the game, set up card and 
def setup():
    global current,chest,chance,squares,ID
    #creates "deck" of community chest and chance cards
    for i in range(17):
        chance.append(card())
        chest.append(card())

    chance[0].move=0
    chance[1].move=24
    chance[2].move=11
    chance[3].move=5
    chance[4].move=39
    chance[5].move=10
    chance[6].move=100
    chance[7].move=100
    chance[8].move=100
    chance[9].move=100

    chest[0].move=0
    chest[1].move=10

    #creates board squares
    for i in range(40):
        squares.append(square())

    squares[0].set("Go")
    squares[10].set("jail", "jail")
    squares[20].set("parking")
    squares[30].set("go to jail","jail")

    squares[2].set("chest","chest")
    squares[17].set("chest","chest")
    squares[33].set("chest","chest")

    squares[7].set("chance","chance")
    squares[22].set("chance","chance")
    squares[36].set("chance","chance")

    squares[5].set("rail","rail")
    squares[15].set("rail","rail")
    squares[25].set("rail","rail")
    squares[35].set("rail","rail")

#function to "roll the dice"
def roll():
    global current
    a = randint(1,6)
    b = randint(1,6)
    count = 0
    total = a+b
    while a == b:                               #while doubles
        count +=1
        a = randint(1,6)
        b = randint(1,6)
        total += a+b
        if count ==3:
            current = 10
            return 0                            #3 doubles
    if current + total >=40:
        current += (total - 40)
        return total
    current +=total
    return total

#function to analyse dice rolls
def analysis():
    num = 100000000
    count = []
    per =[]
    for i in range(40):
        count.append(0)
        per.append(0)

    for i in range(num):
        count[roll()]+=1

    for i in range(40):
        per[i] = round(100*count[i]/num,3)

    #print(count)
    for i in per:
        print(i)

#pick a chance card (community chest is much easier)
def pick_chance():
    global chance, current
    picked = chance[randint(0,16)].move 
    
    if picked == None:                          #do nothing
        pass
    elif picked == 100:                         #move relitive
        second = randint(1,4)
        if second == 1:                         #go back 3
            current -=3
        elif second == 4:                       #go to nearest Utility
            if current <28 and current>=12:
                current = 28
            else:
                current=12
        else:                                   #go to nearest rail road
            if current >=5 and current<35:
                if current >=15:    
                    if current >=25:            #last rail
                        current = 35            
                    else:                       #third rail
                        current = 25            
                else:                           #second rail    
                    current = 15                    
            else:                               #first rail
                current = 5
    else:                                       #move to place 
        current = picked

#"play" a game of monopoly containing total_rounds of moves
def play():
    global current,squares,chest,chance,current_round,total_rounds
    for current_round in range(total_rounds):
        roll()                                      #roll the dice
        token = squares[current]                    #set the postiion to the current square
        if token.modifier != 0:
            if token.modifier == "chest":           #see if the current square has a spcail action assosaited with it eg chance, goto jail etc
                picked = chest[randint(0,16)].move 
                if picked == None:
                    pass
                else:
                    current = picked
            if token.modifier == "chance":
                pick_chance()
            if token.modifier == "jail":
                current =10
        squares[current].inc()                      #increase the count for the times ended a turn on a square

    for j in range(40):
        print(squares[j].get_prob())                #print the probabilty of landing on each square.

setup()

#comment out on the the 2 following lines
analysis()
#play()