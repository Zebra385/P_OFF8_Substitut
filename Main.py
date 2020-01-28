# coding: utf-8 # For French language

print("Bonjour, Bienvenue sur OFF_Substitut\n Quel est votre choix :")
choix = input(" 1 -  Quel aliment souhaitez-vous remplacer ?\n "
              "2 -  Retrouver mes aliments substitués ")
while choix != '1' and choix != '2':
    if choix != '1' or choix!= '2':  # if key '1' or '2' is not pressed
        print("Non, mauvais choix, vous vous êtes trompé")
        print(" Quel est votre choix?")
        choix = input(" 1 -  Quel aliment souhaitez-vous remplacer ?\n "
                      "2 -  Retrouver mes aliments substitués ")
print("Ton choix est : ", choix)