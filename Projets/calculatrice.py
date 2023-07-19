# ----------------------------------------------------[PROJET #1: LA CALCULATRICE]------------------------------------------------------ #
# section 20

# # je déclare mes variables avec la fonction 'input'
# nombre1 = input("Entrez le premier nombre : ")
# nombre2 = input("Entrez le deuxième nombre : ")

# # je convertis les valeurs de mes variables de chaine de caractère en nombre entier avec la fonction int()
# nombre1 = int(nombre1)
# nombre2 = int(nombre2)

# # je crée une nouvelle variable 'resultat' dans lequel je stocke le résultat de l'addition de 'nombre1' et 'nombre2'
# resultat = nombre1 + nombre2

# # j'utilise le f-strinf pour insérer les valeurs 'nombre1', 'nombre2' et 'resultat' dans la phrase demandé
# phrase = f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {resultat}"

# # et je fais print !
# print(phrase)

# --------------------------------------[PROJET #2: LA CALCULATRICE (avec la gestion des erreurs)]--------------------------------------- #
# section 28

while True:
    nombre1 = input("Entrez le premier nombre : ")
    nombre2 = input("Entrez le deuxième nombre : ")
    
    if nombre1.isdigit() and nombre2.isdigit():
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)
        resultat = nombre1 + nombre2
        print(f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {resultat}")
        break
    else:
        print("Veuillez entrer deux nombres valides")