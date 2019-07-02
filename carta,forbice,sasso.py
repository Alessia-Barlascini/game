import random

game = input("enter carta, forbice or sasso: ")

list = ["carta", "forbice", "sasso"]
pc_game = random.choice(list)

print ("random computer is: " + pc_game)

if game == pc_game:
    print ("equal")

elif game == ("carta") and pc_game == ("sasso"):
    print ("you win")

elif game == ("carta") and pc_game == ("forbice"):
    print ("you loose")

elif game == ("forbice") and pc_game == ("sasso"):
    print ("you loose")

elif game == ("forbice") and pc_game == ("carta"):
    print ("you win")

elif game == ("sasso") and pc_game == ("carta"):
    print("you loose")

elif game == ("sasso") and pc_game == ("forbice"):
    print("you win")