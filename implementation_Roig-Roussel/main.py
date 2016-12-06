#!/usr/bin/python
# -*- coding: utf8 -*-
from joueur import *;
from grille import *;
from flotte import *;

def main():

    print("========== Bienvenue dans la Bataille Navale ==========");

    #Saisie de la taille de la grille souhaitée par le joueur
    print("Saisissez la taille de votre grille :")
    tailleGrille=input()

    print(" ");

    #Saisie du nom des deux joueurs par l'utilisateur
    print("Entrez le nom du Joueur 1 : ")
    NomJoueur1=input(); #On récupère le nom du premier joueur
    Joueur1=Joueur(NomJoueur1); #On crée le premier joueur
    Joueur1.Grille=Grille(tailleGrille); # On attribut une grille au joueur 1
    Joueur1.Flotte=Flotte(); #On ne definit pas de taille car le joueur pourra ajouter autant de bateaux qu'il veux


    print("Entrez le nom du Joueur 2 : ")
    NomJoueur2=input(); #On récupère le nom du second joueur
    Joueur2=Joueur(NomJoueur2); #On crée le second joueur
    Joueur2.Grille=Grille(tailleGrille);
    Joueur2.Flotte=Flotte();


    print("La partie va opposer "+NomJoueur1+" à "+NomJoueur2+" !");

    #Placement des bateaux
    print("--------------Placement des bateaux-----------------");
    print("Combien voulez de bateaux : ");
    nbBat=input();


    #On ajoute les bateaux de taille definie par l'utilisateur
    for j in range(0,nbBat):
        taille=-1;
        while (taille<1):
            print("Saisir la taille du bateau "+(j)+" :");
            taille=input();
        #On ajoute le bateau aux flottes des deux joueurs afin de mémoriser leurs tailles.
    	Joueur1.Flotte.ajouterBateaux(taille);
    	Joueur2.Flotte.ajouterBateaux(taille);

    #Les bateaux sont initialisés mais pas placés
    #On place les bateaux

    print("--------------------------------------------------------------------------------------------")
    print(" ")
    print(Joueur1.name()+" place ses bateaux :  ")
    print(" ")

     #Le joueur 1 place ses différents

    for i in range(0,nbat):
    	t=0
        #On initialise x et y à des coordonnées invalides afin que les tests renvoient faux si l'utilisateur ne rentre pas de coordonées
    	x=-1
    	y=-1
    	#On place la première coordonnée du bateau i
        #Cette boucle while vérifie que les coordonées sont valides
    	while (Joueur1.Grille.verificationCoordonnees(x,y)==False):
    		print("Entrez la "+(t+1)+" position du bateau"+(i)+" :")
    		print("x = ");
    		x=input();

    		print("y = ");
    		y=input();
        #Les premières coordonnées sont valides, on les insert
        Joueur1.Grille.placerPositionBateau(i,x,y);

        #Après avoir placé les premières coordonnées, on ajoute les suivantes si tailleBat>1
    	for t in range(1,Joueur1.Flotte.getTaille(i)):
    		x=-1;
    		y=-1;
    		while (Joueur1.Grille.estValide(i,x,y)==False):
    			print("Entrez la "+(t+1)+" position du bateau"+i+" :")
    			print("x = ");
    			x=input();

    			print("y = ");
    			y=input();

    		Joueur1.Grille.placerPositionBateau(i,x,y)

    print("--------------------------------------------------------------------------------------------")
    print(" ")
    print(Joueur2.name()+" place ses bateaux :  ")
    print(" ")

     #Le joueur 2 place ses différents

    for i in range(0,nbat):
    	t=0
        #On initialise x et y à des coordonnées invalides afin que les tests renvoient faux si l'utilisateur ne rentre pas de coordonées
    	x=-1
    	y=-1
    	#On place la première coordonnée du bateau i
        #Cette boucle while vérifie que les coordonées sont valides
    	while (Joueur2.Grille.verificationCoordonnees(x,y)==False):
    		print("Entrez la "+(t+1)+" position du bateau"+(i)+" :")
    		print("x = ");
    		x=input();

    		print("y = ");
    		y=input();
        #Les premières coordonnées sont valides, on les insert
        Joueur2.Grille.placerPositionBateau(i,x,y);

        #Après avoir placé les premières coordonnées, on ajoute les suivantes si tailleBat>1
    	for t in range(1,Joueur2.Flotte.getTaille(i)):
    		x=-1;
    		y=-1;
    		while (Joueur2.Grille.estValide(i,x,y)==False):
    			print("Entrez la "+(t+1)+" position du bateau"+i+" :")
    			print("x = ");
    			x=input();

    			print("y = ");
    			y=input();

    		Joueur2.Grille.placerPositionBateau(i,x,y)







    print("==================== Début du jeu ========================");
    #Début du jeu
    #On initialise une variable tour de jeu qui permet d'alterner le jeu entre les deux joueurs
    tourDeJeu=1;

    #Notre fonction estVide permet de verifier avant chaque nouveau tour si la grille d'un des joueurs est vide
    while ((Joueur1.Grille.estVide()==False) or (Joueur2.Grille.estVide()==False)):
    	if (tourDeJeu==1):
    		print(Joueur1.name()+ " à toi de tirer !");
    		#Joueur 1 tire
    		a=-1;
    		b=-1;
            #On verifie que les coordonées sont bien comprises dans la grille
    		while (Joueur2.Grille.estDansGrille(a,b)==False):
    			print("Entrez les cordonnées de la cible : ");
    			a=input();
    			b=input();
    		result=Joueur2.Grille.tirer(a,b);
    		print(result);


    		tourDeJeu=2; #Changement de tour

    	else:
    		print(Joueur2.name()+ " à toi de tirer !");
    		#Joueur 2 tire

    		a=-1;
    		b=-1;
    		while (Joueur2.Grille.estDansGrille(a,b)==False):
    			print("Entrez les cordonnées de la cible : ");
    			a=input();
    			b=input();
    		result=Joueur2.Grille.tirer(a,b);
    		print(result);

    		tourDeJeu=2; #Changement de tour


    print("==================== Fin du jeu ========================");

    if(Joueur1.Grille.estVide()):
    	print(Joueur2.name()+" a gagné");
    else:
    	print(Joueur1.name()+ "a gagné");




    #Fin de Partie
