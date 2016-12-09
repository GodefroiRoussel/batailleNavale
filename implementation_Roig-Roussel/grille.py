#!/usr/bin/python
# -*- coding: utf8 -*-
class Grille :

# Structure de données choisie
# taille: int           taille de la grille
# positions[][]         tableau des positions de la grille

        def __init__(self, tailleGrille):
        #Initialise une grille, avec comme paramètre la taille de celle-ci.
        #Renvoie erreur si grille n'a pas été initialisée
                self.taille = tailleGrille
                self.positions = [[0 for i in range(tailleGrille)] for y in range(tailleGrille)]

        def placerPositionBateau(self, numBat, xBat, yBat):
        #Données: Grille, numéro du bateau à placer, et coordonnées indiquant où on veut le placer
        #Pré-conditions: numBat:int, xBat:int, yBat:int
        #Resultat: Ajoute le bateau de numéro numBat à la position (xBat,yBat) sur la grille du joueur et renvoie la grille.
        # Renvoie erreur si la position n'est pas ajoutée !
        #Post-conditions:
                try:
                        self.positions[xBat][yBat] = numBat
                except IndexError:
                        print("Erreur placement bateau : cordonnées hors grille.")

        def getBateau (self, xBat, yBat):
        #Données: Grille et coordonnées étudiées
        #Pré-conditions: xBat:int, yBat:int
        #Resultat: Renvoie le numéro du bateau correspondant aux coordonnées xBat, yBat, ou renvoie 0 s'il n'y pas de bateau
        #Post-conditions: numBat:int
                try:
                        numBat = self.positions[xBat][yBat]
                except IndexError:
                        numBat = 0
                return numBat

        def supprimerPosition(self, xBat, yBat):
        #Données: Grille et cordonnées (xBat,yBat)
        #Pré-conditions: xBat:int, yBat:int , on suppose vérfifiée le fait que la postion contient un bateau
        #Resultat: Supprime la position indiquée par les coordonnées (xBat,yBat) et renvoie la grille modifiée
        #Post-conditions:
                self.positions[xBat][yBat] = 0


        def envue(self, xTir, yTir):
        #Données: Grille et coordonnées(xTir,yTir)
        #Pré-conditions: xTir:int, yTir:int
        #Resultat:Renvoie True si il y a un bateau sur la coordonnée xTir ou sur la coordonnée yTir, renvoie False sinon
        #Post-conditions: bool
                res = False
                for i in range (0,self.taille):
                        if(self.positions[xTir][i] != 0):
                                res = True
                for i in range (0, self.taille):
                        if(self.positions[i][yTir] != 0):
                                res = True
                return res

        def estDansGrille(self, x, y):
        #Données: Grille et coordonnées (x,y)
        #Pré-conditions: x:int, y:int
        #Resultat: Renvoie True si la position indiquée par (x,y) se trouve dans la grille, renvoie False sinon
        #Post-conditions: bool
                res = False
                if(x <= self.taille and y <= self.taille and x >= 0 and y >= 0):
                        res = True
                return res

        def estBateau(self, x, y):
        #Données: Grille et coordonnées (x,y)
        #Pré-conditions: x:int, y:int
        #Resultat: Renvoie True s'il y a un bateau aux coordonnées (x,y) indiquées, renvoie False sinon
        #Post-conditions: bool
                res = False
                if(self.estDansGrille(x,y)):
                        if(self.positions[x][y] != 0):
                                res = True
                return res

        def verificationCoordonnees(self, x, y):
        #Données: Grille et coordonnées (x,y)
        #Pré-conditions: x:int, y:int
        #Resultat: Renvoie True si la position indiquée indiquée par (x,y) est dans la grille et non-occupée par un bateau,
        # renvoie False sinon
        #Post-conditions: bool
                return not(estBateau(x,y)) and estDansGrille(x,y)

        def estValide(self, numBat, x, y):
        #Données: Grille, numéro du bateau, et coordonnées (x,y)
        #Pré-conditions: numBat:int, x:int, y:int
        #Resultat: Renvoie True si verificationCoordonnees est true et si la position indiquée par (x,y) est
        # juxtaposée à un bateau de même numéro et que toutes les autres position de ce bateau
        # sont sur la même ligne ou la même colonne, renvoie False sinon
        #Post-conditions: bool
                res = False
                if(verificationCoordonnees(x,y)):
                        # getBateau() gère déjà les erreurs d'index
                        if(getBateau(x+1,y) == numBat):
                                if(getBateau(x+2,y) == numBat):
                                        res = True
                                elif(getBateau(x+1,y+1) != numBat and getBateau(x+1,y-1) != numBat):
                                        res = True

                        if(getBateau(x-1,y) == numBat):
                                if(getBateau(x-2,y) == numBat):
                                        res = True
                                elif(getBateau(x-1,y+1) != numBat and getBateau(x-1,y-1) != numBat):
                                        res = True

                        if(getBateau(x,y+1) == numBat):
                                if(getBateau(x,y+2) == numBat):
                                        res = True
                                elif(getBateau(x+1,y+1) != numBat and getBateau(x-1,y+1) != numBat):
                                        res = True

                        if(getBateau(x,y-1) == numBat):
                                if(getBateau(x,y-2) == numBat):
                                        res = True
                                elif(getBateau(x+1,y-1) != numBat and getBateau(x+1,y-1) != numBat):
                                        res = True
                return res

        def estVide(self):
        #Données: Grille
        #Pré-conditions: ---
        #Resultat: Renvoie True si la grille ne comporte plus aucun bateau, renvoie False sinon
        #Post-conditions: bool
                res = True
                i = 0
                j = 0
                while(res and i < self.taille):
                        j=0
                        while(res and j < self.taille):
                            res = not(estBateau(i,j))
                            j+=1
                        i+=1
                return res

        def tirer(self, xTir, yTir):
                return
        #Données: Grille et coordonnées (xTir,yTir)
        #Pré-conditions: xTir:int, yTir:int
        #Resultat: Renvoie le résultat du tir (en vue, touché ou coulé)
        #Post-conditions: resultatTir:string
