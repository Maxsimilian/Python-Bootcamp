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

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == "left":
    print(
        "You walked along the path and you see a big caste!, which is surrounded by a lake. You got two options: You can either swim to the castle or wait for the drawbridge to let down.")
    choice2 = input("Make your choice: Type 'swim' or 'wait'\n").lower()
    if choice2 == "wait":
        choice3 = input(
            "You can see 3 doors: Blue door, Red door and Yellow Door. Make your choice: Type 'Red' or 'Blue' or 'Yellow'\n").lower()
        if choice3 == "yellow":
            print("Congrats you have found the treasure! You Win!")
            print('''  
         _.+._
       (^\/^\/^)
        \@*@*@/
        {_____}
           ''')

        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game Over.")
        else:
            print("Game Over.")

    else:
        print("Your were attacked by trout. Game Over.")

else:
    print("You fell into a hole. Game Over")
