print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
add_sep   = "\n*******************************************************************************\n"
add_space = "\n\n"


print(add_sep
    + "You enter a tavern and a strange man approaches you with an offer." 
    + "\n"
    + "\"I will give you this treasure map that leads to the long lost treasure of Red Beard found somewhere on skull island.\"" 
    + "\n"
    + "\"But only if you promise me when you find the treasure you give me a specific orb inside the treasure chest.\""
    + add_space)
option_one = input("Do you accept his offer? Answer by typing \"y\" for yes or \"n\" for no:\n").casefold()

if option_one == "y":
    
    print(add_sep
          + "You board a ship and sail to Skull Island."
          + "\n"
          + "Upon arriving you look at the map and notice a mountain with a hole in it that looks similar to the mountain on the island."
          + add_space)
    option_two = input("Do you climb the mountain? y/n:\n").casefold()

    if option_two == "y":
        print(add_sep
              + "You climb the mountain and enter the hole in it and find a device with a lens in it, but it appears to be broken."
              + "\n"
              + "Looking at the device you notice it has a place for another lens and three other lenses nearby."
              + "\n"
              + "The lenses are identical except in dimension. There is a smaller sized lens, a medium sized lens and a larger sized lens."
              + "\n"
              + "You think you may be able to fix it by putting one of these lenses in the device."
              + add_space)
        option_three = input("Do you choose the \"small\", \"medium\" or \"large\" lens:\n").casefold()

        if option_three == "small":
            print(add_sep
                  + "You put the smaller lens in the device and a highly focused beam of light comes out of it."
                  + "\n"
                  + "The beam of light is so powerful it catches the vegetation on the island on fire."
                  + "\n"
                  + "You are now a pyromaniac. Game Over.")
            
        elif option_three == "medium":
            print(add_sep
                  + "You put the medium sized lens in the device and a focused beam of light comes out of it."
                  + "\n"
                  + "The beam points to a smaller clearing in the tropical forest. You climb down the mountain and go the the clearing."
                  + "\n"
                  + "Upon arriving you dig around in the clearing and find the tresaure chest!")
            
            print(add_sep
                  + "Suddenly! The strange man from the tavern appeard from the foliage."
                  + "\n"
                  + "He say's \"You found the treasure chest! Now give me the orb as we promised.\"")
            option_four = input("Do you give him the orb not knowing what it does? y/n:\n")

            if option_four == "y":
                print(add_sep
                      + "You suddenly are in the tavern again, very confused and think you may have dreamed the entire encounter and the quest you embarked on."
                      + "\n"
                      + "You move on thinking it was a dream. Game Over.")
                
            elif option_four == "n":
                print(add_sep
                      + "You question the stange man from the tavern about what the orb does and he refuses to tell you."
                      + "\n"
                      + "You decide to not give him the orb and he attempts to take the orb by force."
                      + "\n"
                      + "You take the orb out of the treasure chest and start running away with it. But as soon as you put your hands on it the strange man disappears."
                      + "\n"
                      + "Confused but still with your treasure and the orb you board the ship with your bounty and leave the island forever. You Win???")
                
            else:
                print(add_sep
                      + "Instead of giving him the orb you just stare blank at him..."
                      + "\n"
                      + "Uncomfortably long..."
                      + "\n"
                      + "Is this some sort of strange staring contest???"
                      + "\n"
                      + "He eventually leaves due to how awkward you made the situation, which is great becuase you now have your treasure all to yourself! You Win!")
            
        elif option_three == "large":
            print(add_sep
                  + "You put the larger sized lens in the device and a wide beam of light comes out of it."
                  + "\n"
                  + "Congratulations, you made a lighthouse that only really works during a sunny day, which is rather useless. Game Over.")
        
        else:
            print(add_sep
                  + "You instead shove a rock in the device and watch the rock slowly grow darker..."
                  + "\n"
                  + "The rock grows darker because the sun is going down, and the device kind of needs the sun to work but you don't realize that. Game Over. (You didn't answer with a valid answer)")

    elif option_two == "n":
        print("You look at the mountain and decide that you don't want to exert that much energy. Game Over. (You didn't answer y/n)")

    else:
        print(add_sep
              + "For some reason you turn around and start walking into the ocean. Game Over. (You didn't answer y/n)")

elif option_one == "n":
    print(add_sep
          + "You pass over his offer and move on with your life. Game Over.")

else:
    print(add_sep
          + "You stand there speaking gibberish to the strange man."
          + "\n"
          + "Suddenly you realize he is actually pretty normal and you are the strange one. Game Over. (You didn't answer y/n)")
