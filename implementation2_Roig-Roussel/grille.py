#!/usr/bin/python
# -*- coding: utf8 -*-
class Grille :


	def __init__(self, tailleGrille):
		#Initialise une grille, avec comme paramètre la taille de celle-ci.
        #Renvoie erreur si grille n'a pas été initialisée



    	def placerPositionBateau(self, numBat, xBat, yBat):
    		#Données: Grille, numéro du bateau à placer, et coordonnées indiquant où on veut le placer
    		#Pré-conditions: numBat:int, xBat:int, yBat:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Ajoute le bateau de numéro numBat à la position (xBat,yBat) sur la grille du joueur et renvoie la grille. Renvoie erreur si la position n'est pas ajoutée !
    		#Post-conditions:


        def getBateau (self, xBat, yBat):
    		#Données: Grille et coordonnées étudiées
    		#Pré-conditions: xBat:int, yBat:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Renvoie le numéro du bateau correspondant aux coordonnées xBat, yBat, ou renvoie -1 s'il n'y pas de bateau
    		#Post-conditions: numBat:int





    	def supprimerPosition(self, xBat, yBat):
    		#Données: Grille et cordonnées (xBat,yBat)
    		#Pré-conditions: xBat:int, yBat:int , on suppose vérfifiée le fait que la postion contient un bateau et avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Supprime la position indiquée par les coordonnées (xBat,yBat) et renvoie la grille modifiée
    		#Post-conditions:


    	def envue(self, xTir, yTir):
    		#Données: Grille et coordonnées(xTir,yTir)
    		#Pré-conditions: xTir:int, yTir:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat:Renvoie True si il y a un bateau sur la coordonnée xTir ou sur la coordonnée yTir, renvoie False sinon
    		#Post-conditions: bool


    	def estDansGrille(self, x, y):
    		#Données: Grille et coordonnées (x,y)
    		#Pré-conditions: x:int, y:int
    		#Resultat: Renvoie True si la position indiquée par (x,y) se trouve dans la grille, renvoie False sinon
    		#Post-conditions: bool

    	def estBateau (self, x, y):
    		#Données: Grille et coordonnées (x,y)
    		#Pré-conditions: x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Renvoie True s'il y a un bateau aux coordonnées (x,y) indiquées, renvoie False sinon
    		#Post-conditions: bool

    	def verificationCoordonnees(self, x, y):
    		#Données: Grille et coordonnées (x,y)
    		#Pré-conditions: x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Renvoie True si la position indiquée indiquée par (x,y) est dans la grille et non-occupée par un bateau, renvoie False sinon
    		#Post-conditions: bool

    	def estValide(self, numBat, x, y):
    		#Données: Grille, numéro du bateau, et coordonnées (x,y)
    		#Pré-conditions: numBat:int, x:int, y:int
    		#Resultat: Renvoie True si verificationCoordonnees est true et si la position indiquée par (x,y) est juxtaposée à un bateau de même numéro et que toutes les autres position de ce bateau sont sur la même ligne ou la même colonne, renvoie False sinon
    		#Post-conditions: bool

        def noSpace(self,taille,numBat,x,y):
            #Données: Grille,taille du bateau, et coordonnées (x,y)
    		#Pré-conditions: numBat:int, x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Renvoie True si après vérification, il y a suffisament de place pour inserer le bateau à l'horizontale ou à la verticale après analyse de la direction du bateau si il y a déjà des cases ajoutées pour le numBat donné en paramètre
    		#Post-conditions: bool

    	def estVide(self):
    		#Données: Grille
    		#Pré-conditions: ---
    		#Resultat: Renvoie True si la grille ne comporte plus aucun bateau, renvoie False sinon
    		#Post-conditions: bool

    	def tirer(self, xTir, yTir):
    		#Données: Grille et coordonnées (xTir,yTir)
    		#Pré-conditions: xTir:int, yTir:int avec estDansGrille(xBat) et estDansGrille(yBat)
    		#Resultat: Renvoie le résultat du tir (à l'eau, en vue, touché ou coulé)
    		#Post-conditions: resultatTir:string



