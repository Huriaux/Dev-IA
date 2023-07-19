# -----------------------------------------------[PROJET Udemy #3: LA LISTE DE COURSES]-------------------------------------------------- #
# section 29

import sys
shop_list = []
icon = "\U0001F449 "

# boucle while
while True:
    print("-----------------------------------------------------")
    print("Choisissez parmi les 5 options : ")
    print("1: Ajouter un élément à la liste")
    print("2: Supprimer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

# choix des options
    choice_options = input(f"{icon} Votre choix : ")
    if not choice_options.isdigit() or not (1 <= int(choice_options) <= 5):
        print("Votre choix n'est pas incorrect, veuillez réessayer...")
    else:
        choice_options = int(choice_options)
    
# 1 ajouter un élément
    if choice_options == 1:
            add = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
            shop_list.append(add)
            print(f"L'élément {add} a bien été ajouté à la liste.")

# 2 supprimer un élément
    elif choice_options == 2:
        delete = input("Entrez le nom d'un élément à retirer à la liste de courses : ")
        if delete in shop_list:
            shop_list.remove(delete)
            print(f"L'élément {delete} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {delete} n'est pas dans le contenu.")
         
# 3 Afficher liste
    elif choice_options == 3:
        if len(shop_list) == 0:
            print("Votre liste ne contient aucun élément.")
        else:
            for i, item in enumerate(sorted(shop_list, reverse=True), 1):
                print(f"{i}. {item}")

# 4 Vider liste
    elif choice_options == 4:
        shop_list.clear()
        print("La liste a été vidée de son contenu.")

# 5 Quitter 
    elif choice_options == 5:
        print("À bientôt !")
        sys.exit()