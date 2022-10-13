#créé par Noah Pfister


import random

#ici je definit le maximum
minimum = 1
maximum = 1000



#Ceci choisi quel nombre serai le maximum
answer = random.randint(minimum, maximum)
guessed = False

#ceci est la fonction qui tient compte du nombre d'essai
tries = 0

#on demande pour le nombre requis, et si tu reussi, ca recommence.
while not guessed:
    write = input("devin un nombre entre 1 et 1000")
    write = int(write)
    if answer == write:
        print(tries)
        reesayer = input("vous avez raison!!, voulez vous reesayer? o/n")
        guessed = True
        if reesayer == "o":
            guessed = False
        if reesayer == "n":
           print("Merci et au revoir")
           guessed = True
#si tu ne reussis pas, ceci
    if answer < write:
        print("votre reponse est plus grande que la reponse?")
        tries = tries + 1

    if answer > write:
        print("votre reponse est plus petite que la reponse?")
        tries = tries + 1

        
