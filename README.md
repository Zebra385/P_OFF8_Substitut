# ***.........................Projet OFF Sustitut............................***
## 1. Qu'est ce que ce projet ?
###    C'est un programme qui permet de trouver un substitut à un aliment. 
### Celui ci s'appuira sur la base de données d'Open Food Facts
## 2. Comment démarrer le programme?
###  Il faut installer les bibliothèques à  l'aide de la commande:
 py -m pip install -r requirements.txt
### On utilisera la version python 3.7.5 en 32 bits
## 3.Comment exécuter le programme?
### il suffit de lancer en python Main.py
## Celui-ci propose un menu  via le terminale: 
### Bonjour, Bienvenue sur OFF_Substitut:
### 1 - Quel aliment souhaitez-vous remplacer ?
### 2 - Retrouver mes aliments substitués
### 3 - Quitter menu
### Quel est votre choix
## 4- La strastégie de develepement du projet:
### 4-1 fichier principale en python, main.py
#### Automatisation à l'aide d'une fontion (displa_menu(option)) pour l'affichage
#### d'un menu, option étant l'intitulé du numero(index) dans le menu 
### 4-2 Comment récupérer les catégories dans openfoodfacts
#### On utilise postman pour récuperer sous forme d'un fichier json nommé 
#### Categories_Aliment_France_OFF.json les catégories. La requete GEST est :
#### https://fr.openfoodfacts.org/categories.json
#### Puis on enregistre le résultat  en cliquand sur "save reponse",
#### il faut mettre le fichier dans le même réêrtoire que le programme
####  principal Main.py