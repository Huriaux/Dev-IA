# -----------------------------------------------[PROJET Udemy #4: LE JEU DU NOMBRE MYSTERE]-------------------------------------------------- #
# section 30

# créer un nombre aléatoire entre 0 et 100
import sys
import random
nombre_mystere = random.randint(0, 100)
nombre_essais = 5
reste = "Il te reste {} essais"
gagne = "Bravo ! Le nombre mystère était bien {} !"
resultat = "Tu as trouvé la nombre en {} essais"
perdu = "Dommage ! Le nombre mystère était {}"

#  boucle while
while True:
    print("*** Le jeu du nombre mystère ***")

# nombre d'essais
    for essais in range(1, 6):
# un peu d'orthographe quand même :)
        if nombre_essais == 1:
            reste = reste.strip("s")
        
        print(reste.format(nombre_essais))


# conditions nombre entier (==int) sinon 'erreur'
        devine = input("Devine le nombre : ")
        if not devine.isdigit() or not (0 <= int(devine) <= 100):
            print("Veuillez entrer un nombre valide.")
            continue
        else:
            devine = int(devine)
            nombre_essais -= 1
            
# les indices (conditions)
        if devine == nombre_mystere and nombre_essais == 4:
            print(gagne.format(nombre_mystere))
            resultat = resultat.replace("essais", "essai")
            print(resultat.format("1"))
            print("Fin du jeu.")
            sys.exit()
        elif devine == nombre_mystere:
            nombre_essais = 5 - int(nombre_essais)
            print(resultat.format(nombre_essais))
            print(gagne.format(nombre_mystere))
            print("Fin du jeu.")
            sys.exit()
            
        elif devine > nombre_mystere:
            print(f"Le nombre mystère est plus petit que {devine}")
        else:
            print(f"Le nombre mystère est plus grand que {devine}")
    
        if nombre_essais == 0:
            print(perdu.format(nombre_mystere))
            print("Fin du jeu.")
            sys.exit()