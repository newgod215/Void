import random
import datetime

def clanName():
    clanName = ['vage' , 'treed' , 'yaguwa' , 'slin']
    random_spin =  random.choices(4)

def powersystem():
    stat_points = ['vitality' , 'strength' , 'weapon']
    stat_increase = random.range(3,10)
    
    print(" you gained " + str(stat_points) + "plus point" + str (stat_increase) + "increased points")
        
def travel():
    miles_traveled = random.range(38,61)
    days_spent = random.range(3,8)
    
    print(" you've traveled " + str(miles_traveled) + "miles & it took" +str (days_spent) + " days")


def rest():
    vitality_increase: int = random.randrange(1,6)
    days_spent = random.randrange(2,6)

    print(" you've gained " + str(vitality_increase) + "health & it took" + str(days_spent)"days")


def hunt():
    animal = 100
    days_spent = random.randrange(2,6)

    print("you've gained " + str(animal) + " lbs of food & it took" + str(days_spent)"days")


def status_bag():
    commands = ['Travel','Rest', 'Hunt', 'Status', 'Help']
    print(commands)

clanName()
powersystem()
travel()
rest()
hunt()
status_bag()


print('clanName' , 'powersystem' , 'travel' , 'rest' , 'hunt' , 'status_bag')

#User will get a in game note telling the user how to play the game

print('welcome to the void follow the arrow to the cave')

def runGame():
    
