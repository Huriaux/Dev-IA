import sys

utilisateur = input("Tapez votre nom d'utilisateur : ")
print(utilisateur)

age = ("Quel est votre âge ? (Vous devez être majeur) : ")
print(age)

reponse_age = input()
if int(reponse_age) >= 18:
    print("Accès autorisé !")
else: 
    print("Accès refusé")
    sys.exit()
    
    
while True:
    mdp = input("Entrez un mot de passe : ")
    print(mdp)

    if len(mdp) >= 8:
        break
    else:
        print("Le mot de passe doit comporter au moins 8 caractères." + mdp)


while True:
    verif_mdp = input("Confirmez votre mot de passe : ")
    print(verif_mdp)

    if verif_mdp == mdp:
        print("Votre inscription est réussie, bienvenue !")
        break
    else: 
        print("ERREUR: Le mot de passe est inccorect... " + verif_mdp)

sys.exit()