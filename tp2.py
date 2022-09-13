
#créé par Noah Pfister


import random

minimum = 1
maximum = 5




answer = random.randint(minimum, maximum)
guessed = False

tries = 0

while not guessed:
    write = input("devin un nombre entre 1 et 1000")
    write = int("vous avez eu ",write)
    if answer == write:
        print(tries)
        reesayer = input("vous avez raison!!, voulez vous reesayer? o/n")
        guessed = True
        if reesayer == "o":
            guessed = False
        if reesayer == "n":
           print("Merci et au revoir")
        guessed = True

    if answer < write:
        print("votre reponse est plus grande que la reponse?")
        tries = tries + 1

    if answer > write:
        print("votre reponse est plus petite que la reponse?")
        tries = tries + 1




