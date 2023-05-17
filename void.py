import random
import datetime

#player will be able to spin in this clanName generator for a random clanName
def clanName():
    clanName = ['vage' , 'treed' , 'yaguwa' , 'slin']
    clan_generator = random.randint(0, 3)

    return clanName[clan_generator]

def powersystem():
    powersystem = ['stats']
    stat_points = ['vitality' , 'strength' , 'weapon']
    stat_increase = random,range(3, 10)
    stat_generator = random.randint(0, 2)


    #if boss_level == 15:
        #new_stat = stat_generator('x5')

    
    print(" you gained " , str(stat_points) , "plus point" , str(stat_increase) , "increased points" , (stat_generator) , "random points")



def travel():
    miles_traveled = random.randrange(38,61)
    days_spent = random.randrange(3,8)
    
    print("you've traveled " + str(miles_traveled) + "miles & it took" +str (days_spent) + " days")


def rest():
    vitality_increase: int = random.randrange(1,6)
    days_spent = random.randrange(2,6)

    print((vitality_increase) + (days_spent))


def hunt():
     animal = 100
     days_spent = random.randrange(2,6)

     print((animal) + (days_spent))


def status_bag():
    commands = ['Travel','Rest', 'Hunt', 'Status', 'Help']
    print(commands)

# def save():
#     save_all = datetime + random
#     print(save_all)
     
clanName()
powersystem()
travel()
rest()
hunt()
status_bag()
# save()

print('clanName' , 'powersystem' , 'travel' , 'rest' , 'hunt' , 'status_bag')

 #User will get a in game note telling the user how to play the game

print('welcome to the void follow the arrow to the cave')

def runGame():
 runGame = ('play')
    
# print (runGame)

print(clanName())
