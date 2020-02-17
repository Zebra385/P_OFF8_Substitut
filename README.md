# ***.........................Projet OFF Sustitut............................***
## 1. Qu'est ce que ce projet ?
###    C'est un programme qui permet de trouver un substitut à un aliment. 
### Celui ci s'appuira sur la base de données d'Open Food Facts
## 2. Comment démarrer le programme?
###  Il faut installer les bibliothèques à  l'aide de la commande:
 py -m pip install -r requirements.txt
### On utilisera la version python 3.7.5 en 32 bits
## 3.Comment exécuter le programme?
### Il faut commencer par ouvrir l'accés au serveur localhost
### Puis, il suffit de lancer en python Main.py
## Celui-ci propose un menu  via le terminale: 
#### Bonjour, Bienvenue sur OFF_Substitut:
#### 0- Première utilisation, enregistrement du catalogue des catégories et
####   produits 
#### 1 - Quel aliment souhaitez-vous remplacer ?
#### 2 - Retrouver mes aliments substitués
#### 3 - Quitter menu
#### Quel est votre choix
###     3-1 Choix 0
#### C'est la première utilisation du programme, ici les tables sont créées et
#### remplies
###     3-2 Choix 1
#### Le programme propose des catégories, il faut en choisir une, puis il propose
#### des produits de cette catégorie, il faut alors en choisir un afin de 
#### connaître son substitut qui est affiché
#### Ensuite on a la possibilité d'enregistrer la réponse ou de quitter le 
#### programme 
###     3-3 Choix 2
#### Affichage des résultats
## 4- La strastégie de developement du projet:
### 4-1 fichier principale en python, Main.py
#### Automatisation à l'aide d'une fontion (display_menu(option)) pour l'affichage
#### d'un menu, option étant l'intitulé du numero(index) dans le menu 
### 4-2 Comment récupérer les catégories  et produits dans openfoodfacts
#### Récupération catalogue catégories et produits grâce aux librairies Request.
#### et MySql.connector 
#### Choix 0 pour télécharger dans des bases de données Catégories et produits.
### 4-3 Affichage contenue de la table Catégory pour choix categorie
#### choix 1 pour affichage contenu table categorie puis choix categorie, puis 
#### affichage des produits de la catégorie choisie, puis choix du produit afin
#### de déterminer son substituant
#### Possibilités d'enregistrés ou pas le résultat
#### Afin de simplifier la démarche le choix du substituant s'effectue en prenant
####le meilleur nutriscore des élèments de la même catégorie
### 4-4 Visualisation des résultats enregistrés
#### Jointure entre les tables products et substituants pour afficher les résultats