from sys import exit
import numpy as np

def gold_room():
    print("This room is full of gold.  How many gold coins do you take?")

    try:
       choice = int(input("> "))
    except:
       dead("You chose a non-integer amount of coins. \n Trying in vain to break one of the coins into pieces, you upset the bear who rips your face off.")

    if choice < 50:
        print("Nice, you're not greedy.  You escape the bear on your way out.  You Win!")
        exit(0)
    else:
        dead("You drop coins as you flee, upsetting the bear who rips your face off")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        if bear_moved == True:
         choice = input("> [take honey,taunt bear, open door] ")
        else:
         choice = input("> [take honey,taunt bear] ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def ladder():
    print("you slowly ascend the ladder to an attic.  You see an anvil and a hole in the floorboards: cthulu is below")
    print("there is another ladder on the opposite side of the attic.")
    print("do you push the anvil onto Cthulu's head or crawl to the other ladder. [push, crawl]")
   
    decision=input(">")
    
    if decision == 'push':

     fate=np.random.rand()
   
     if fate < 0.5:
      print("you bonk Cthulu on the head, knocking him unconscious, and claim a pot of gold.")
      exit(0)
     else:
      dead("you are too loud pushing the anvil: Cthulu looks at you, you go insane and eat your head")

    else:
     print("you get to the other side, descend and find nothing ...")
     fate2=np.random.rand()
     if fate2 < 0.5:
      dead("your life is a failure. Cthulu hears you whining, chases you and drives you to madness: you eat your head.")
     else:
      print("Let's do this again")
      start()
      

def dead(why):
    print(why, "Game Over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left. And there is a ladder leading to a window above the right door")
    print("Which one do you take [right, left, ladder]?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "ladder":
        ladder()
    else:
        dead("You stumble around the room until you starve.")

start()
