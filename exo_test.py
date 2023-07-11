# Les étapes pour créer un formulaire :

# 1) Démarrer par un simple 'print(utilisateur)', l'invité devra rentrer un nom d'utilisateur sans restriction.

# 2) Demander l'âge : (condition)
# 'input' pour demander à l'invité d'indiquer son âge :
    # vérifier si l'âge et > ou = à 18 ans
        # si 'age' n'est pas >= à 18 ans, le script devra afficher le message 'Vous n'êtes pas majeur : Accès refusé...' et FIN du script.
        # dans le cas contraire, il affichera 'Vous êtes majeur : Accès autorisé !' ainsi la question suivante.
        
# 3) Tapez le mot de passe : (boucle + condition)
# le mot de passe devra contenir 8 caractères ou plus. 
    # si pas, retourner la même question en ajoutant le message "Votre mot de passe doit contenir au moins 8 caractères".
    # si ok, passer à la question suivante.
    
# 4) Confirmer le mot de passe : (boucle + condition)
    # si le mot de passe indiquez est différent du premier qui est demandé, retourner à la question de 'verif_mdp' 
    # en ajoutant le message "Votre mot de passe est différent, veuillez retaper correctement"
    # si ok, mettre le message : "Votre inscription est réussie, bienvenue !", FIN du script.


import sys

utilisateur = input("Tapez votre nom d'utilisateur : ")

age = ("Quel est votre âge ? (Vous devez être majeur) : ")
print(age)

reponse_age = input()
if int(reponse_age) >= 18:
    print("Vous êtes majeur : Accès autorisé !")
else: 
    print("Vous n'êtes pas majeur : Accès refusé...")
    sys.exit()
    

while True:
    mdp = input("Entrez un mot de passe : ")

    if len(mdp) >= 8:
        break
    else:
        print("Le mot de passe doit comporter au moins 8 caractères, veuillez réessayer...")


while True:
    verif_mdp = input("Confirmez votre mot de passe : ")
    print(verif_mdp)

    if verif_mdp == mdp:
        print("Votre inscription est réussie, bienvenue !")
        break
    else: 
        print("ERREUR: Le mot de passe n'est pas identique, veuillez réessayer... ")

sys.exit()