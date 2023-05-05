import random
import datetime


def travel():
    miles_traveled = random.range(38,61)
    days_spent = random.range(3,8)

    print(" you've traveled " + str(miles_traveled) + "miles & it took" +str (days_spent) + " days")


def rest():
    health_increase: int = random.randrange(1,6)
    days_spent = random.randrange(2,6)

    print(" you've gained " + str(health_increase) + "health & it took" + str(days_spent)"days")


def hunt():
    animal = 100
    days_spent = random.randrange(2,6)

    print("you've gained " + str(animal) + " lbs of food & it took" + str(days_spent)"days")


def help_function():
    commands = ['Travel','Rest', 'Hunt', 'Status', 'Help']
    print(commands)


travel()
rest()
hunt()
help_function()