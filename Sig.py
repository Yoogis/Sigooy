from Sigmap import method
from Sigforest import method2
from Sigbag import method3
from Sigvilhome import method4

# CAKE GAME

print("~ Cake Game ~")
print("Welcome! Please input your player name.")
while True:
    ply1 = input("Player name : ")
    print("Your name is "+ply1+" correct? ")
    yon = input("y or n : ")
    if yon == "y" or yon == "yes":
        print ("Hi "+ply1+".")
        break
    elif yon == "n" or yon == "no":
        print("Please input your player name.")
    elif yon != "y" or yon != "yes":
        print("You did not input y or n. Please input your player name.")
        continue
print("Welcome to Cake Game and thank you for coming to Cake Game Bakery. What do you need?")
enter = input("Press enter to respond")
print("'...'")
enter = input("Press enter to continue")
fname = input("Oh yes! You need to bake a cake for your friend! What was their's name again? : ")
print("Yes! "+fname+". It is their birthday today! Let's bake them a cake.")
enter = input("Press enter to continue   ")

# - 

print("You enter the kitchen.")
flavor = input("What flavor do you think "+fname+" likes? : ")
print(flavor+" is a good choice! \nFor "+flavor+" we need flour, sugar, eggs and the most important ingredient for "+flavor+", but we don't have it.")
enter = input("Press enter to respond")
print("'?!'")
enter = input("Press enter to continue")
print("Don't worry! You can find it at Cake Game Mountain!")
enter = input("Press enter to respond")
print("'...'")
enter = input("Press enter to continue")
print("You can't let "+fname+" down! Here is a map of Cake Game. Go all the way to Cake Game Mountain and get the secret ingredient.")
enter = input("Press enter to open the map")
method()
print("Don't worry if you wanted to look at it again, you will get multiple opportunities to do so!")
print("Find the secret ingredient before "+fname+"'s birthday celebration!")
enter = input("Press enter to continue")
print("The first place you have to go to is Cake Game Forest. In Cake Game Forest, you can find a village that knows how to find the ingredient. Make sure to talk to the villagers.")
enter = input("Press enter to continue")
print("You start to walk on the trail when you encounter a bag.")
while True:
    bag = input("Do you want to see what is inside of it? y or n : ")
    if bag == ('y') or bag == ('yes'):
        method3()
        print("What was that? I don't think it is useful.")
        break
    elif bag == ('n') or bag == ('no'):
        print("You leave the bag")
        break
    elif bag != ("y") or bag != ("n") or bag != ("yes") or bag != ("no"):
        print("Your response isn't valid.")
        continue
enter = input("Press enter to continue walking")
print("You see the forest as you approach it. There is a bird singing to you, and the forest gives off unsettling vibes.")
enter = input("You check the map before you go in. \nPress enter to open the map")
method()
print("You decide to enter the forest.")
enter = input("Press enter to continue")
method2()
print("You look around and realize you are in the village. You look for a villager nearby when you find one looking at you.")
while True:
    talk = input("Do you want to talk to the villager?")
    if talk == ("yes") or talk == ("y"):
        #prepare for a long part for the IF
        print("You approach the villager")
        print("Villager : 'Hello. What brings you to our town?'")
        enter = input("Press enter to respond")
        print("'...'")
        enter = input("Press enter to continue")
        print("Villager : 'You need to know how to get to the Cake Game Mountains to get the secret ingredient? \nThat mountain has not been climbed successfully in over 100 years. Are you sure about this?'")
        while True:
            sure = input("Are you sure you want to risk your life for "+fname+"'s Birthday? : ")
            if sure == 'yes' or sure == 'y':
                print("'...'")
                print("Villager : 'Yes? Okay..'")
                print("The villager signals for you to follow them into a building that seems to be their home.")
                enter = input("Press enter to enter the villager's home.")
                method4()
                print("Their home seems homey.")
                print("Villager: 'As you probably already know, the Cake Game Mountains are dangerous and hard to climb.\nThe most important thing for you to be watch out for is the Cake Game Baker. They like to send people to the Cake Game Mountains and make them grab ingredients for them. I hope you aren't one of them..'")
                enter = input("Press enter to continue.")
                print("You realize that the villager either has already caught on or they will soon, so you run out of the house.")
                break
            elif sure == 'no' or sure == 'n':
                print("'...'")
                print("Villager : 'No? That's a good choice. My grandfather went three years ago and he hasn't returned since. I wonder what happened to him.")
                enter = input("Press enter to continue")
                print("You decide to leave the villager.")
                break
            else:
                print("Your response is not valid.")
                continue
        break
    elif talk == ("no") or talk ==("n"):
        print("You decide to not talk to this villager.")
        break
    else:
        print("Your response is not valid")
        continue

print("You decide that you don't need help from this village and you exit the forest.")
enter = input("Press enter to continue")
print("You head for the mountains.")
