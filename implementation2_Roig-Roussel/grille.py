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
		self.positions = [[-1 for j in range(0, tailleGrille+1)] for i in range(0, tailleGrille+1)]

	def placerPositionBateau(self, numBat, xBat, yBat):
	#Données: Grille, numéro du bateau à placer, et coordonnées indiquant où on veut le placer
	#Pré-conditions: numBat:int, xBat:int, yBat:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Ajoute le bateau de numéro numBat à la position (xBat,yBat) sur la grille du joueur et renvoie la grille. Renvoie erreur si la position n'est pas ajoutée !
	#Post-conditions:
		try:
			self.positions[xBat][yBat] = numBat
		except IndexError:
			print("Erreur placement bateau : cordonnées hors grille.")

	def getBateau(self, xBat, yBat):
	#Données: Grille et coordonnées étudiées
	#Pré-conditions: xBat:int, yBat:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Renvoie le numéro du bateau correspondant aux coordonnées xBat, yBat, ou renvoie -1 s'il n'y pas de bateau
	#Post-conditions: numBat:int
		try:
			numBat = self.positions[xBat][yBat]
		except IndexError:
			numBat = -1
		return numBat

	def supprimerPosition(self, xBat, yBat):
	#Données: Grille et cordonnées (xBat,yBat)
	#Pré-conditions: xBat:int, yBat:int , on suppose vérfifiée le fait que la postion contient un bateau et avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Supprime la position indiquée par les coordonnées (xBat,yBat) et renvoie la grille modifiée
	#Post-conditions:
		self.positions[xBat][yBat] = -1

	def envue(self, xTir, yTir):
	#Données: Grille et coordonnées(xTir,yTir)
	#Pré-conditions: xTir:int, yTir:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat:Renvoie True si il y a un bateau sur la coordonnée xTir ou sur la coordonnée yTir, renvoie False sinon
	#Post-conditions: bool
		res = False
		for i in range (0,self.taille):
				if(self.positions[xTir][i] != -1):
						res = True
		for i in range (0, self.taille):
				if(self.positions[i][yTir] != -1):
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

	def estBateau (self, x, y):
	#Données: Grille et coordonnées (x,y)
	#Pré-conditions: x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Renvoie True s'il y a un bateau aux coordonnées (x,y) indiquées, renvoie False sinon
	#Post-conditions: bool
		res = False
		if(self.estDansGrille(x,y)):
				if(self.positions[x][y] != -1):
						res = True
		return res

	def verificationCoordonnees(self, x, y):
	#Données: Grille et coordonnées (x,y)
	#Pré-conditions: x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Renvoie True si la position indiquée indiquée par (x,y) est dans la grille et non-occupée par un bateau, renvoie False sinon
	#Post-conditions: bool
		return not(self.estBateau(x,y)) and self.estDansGrille(x,y)

	def estValide(self, numBat, x, y):
	#Données: Grille, numéro du bateau, et coordonnées (x,y)
	#Pré-conditions: numBat:int, x:int, y:int
	#Resultat: Renvoie True si verificationCoordonnees est true et si la position indiquée par (x,y) est juxtaposée à un bateau de même numéro et que toutes les autres position de ce bateau sont sur la même ligne ou la même colonne, renvoie False sinon
	#Post-conditions: bool
		res = False
		if(self.verificationCoordonnees(x,y)):
				# getBateau() gère déjà les erreurs d'index
				if(self.getBateau(x+1,y) == numBat):
						if(self.getBateau(x+2,y) == numBat):
								res = True
						elif(self.getBateau(x+1,y+1) != numBat and self.getBateau(x+1,y-1) != numBat):
								res = True

				if(self.getBateau(x-1,y) == numBat):
						if(self.getBateau(x-2,y) == numBat):
								res = True
						elif(self.getBateau(x-1,y+1) != numBat and self.getBateau(x-1,y-1) != numBat):
								res = True

				if(self.getBateau(x,y+1) == numBat):
						if(self.getBateau(x,y+2) == numBat):
								res = True
						elif(self.getBateau(x+1,y+1) != numBat and self.getBateau(x-1,y+1) != numBat):
								res = True

				if(self.getBateau(x,y-1) == numBat):
						if(self.getBateau(x,y-2) == numBat):
								res = True
						elif(self.getBateau(x+1,y-1) != numBat and self.getBateau(x+1,y-1) != numBat):
								res = True
		return res

	def noSpace(self,taille,numBat,x,y):
	#Données: Grille,taille du bateau, et coordonnées (x,y)
	#Pré-conditions: numBat:int, x:int, y:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Renvoie True si après vérification, il y a suffisament de place pour inserer le bateau à l'horizontale ou à la verticale
	#après analyse de la direction du bateau si il y a déjà des cases ajoutées pour le numBat donné en paramètre
	#Post-conditions: bool
		res = False
		placeVertical = False
		placeHorizontal = False

		if(self.verificationCoordonnees(x,y)):

			# Vérification horizontale
			cHorizontalPos = 0
			cHorizontalNeg = 0
			while(self.verificationCoordonnees(x+1+cHorizontalPos,y) or self.getBateau(x+1+cHorizontalPos,y) == numBat):
				cHorizontalPos += 1
			# Sortie : on rencontre une case soit prise par un bateau soit hors grille (sens positif horizontal)
			while(self.verificationCoordonnees(x-1-cHorizontalNeg,y) or self.getBateau(x-1-cHorizontalNeg,y) == numBat):
				cHorizontalNeg += 1
			# Sortie : on rencontre une case soit prise par un bateau soit hors grille (sens négatif horizontal)
			placeHorizontal = ((cHorizontalNeg + cHorizontalPos + 1) >= self.taille)

			# Vérification verticale
			cVerticalPos = 0
			cVerticalNeg = 0
			while(self.verificationCoordonnees(x,y+cVerticalPos+1) or self.getBateau(x,y+cVerticalPos+1) == numBat):
				cVerticalPos += 1
			# Sortie : on rencontre une case soit prise par un bateau soit hors grille (sens positif vertical)
			while(self.verificationCoordonnees(x,y-cVerticalNeg-1) or self.getBateau(x,y-cVerticalNeg-1) == numBat):
				cVerticalNeg += 1
			# Sortie : on rencontre une case soit prise par un bateau soit hors grille (sens négatif vertical)
			placeVertical = ((cVerticalNeg + cVerticalPos + 1) >= self.taille)


			# 1ère position à placer
			if(not self.estValide(numBat,x,y)):
				res = placeVertical or placeHorizontal

			# 2ème ou + position à placer
			else:
				# on cherche la case juxtaposée
				if(self.getBateau(x+1,y) == numBat or self.getBateau(x-1,y) == numBat):
					# case à droite ou à gauche (x)
					res = placeHorizontal

				if(self.getBateau(x,y-1) == numBat or self.getBateau(x,y+1) == numBat):
					# case en haut ou en bas (y)
					res = placeVertical

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
					res = not(self.estBateau(i,j))
					j+=1
				i+=1
		return res

	def tirer(self,flotte, xTir, yTir):
	#Données: Grille, flotte et coordonnées (xTir,yTir) du joueur sur lequel on tire
	#Pré-conditions: xTir:int, yTir:int avec estDansGrille(xBat) et estDansGrille(yBat)
	#Resultat: Renvoie le résultat du tir (à l'eau, en vue, touché ou coulé) et modifie la flotte et la grille en cas de tir reussi
	#Post-conditions: resultatTir:string
		res = ""
		if self.estBateau(xTir,yTir):
			# Touché ou coulé ?
			bateauTouche = self.getBateau(xTir,yTir)
			self.supprimerPosition(xTir,yTir)
			flotte.touce(bateauTouche)
			i=0
			# si une des cases alentours correspond au numéro du bateau, alors il n'est pas coulé
			if(self.getBateau(xTir+1,yTir) == bateauTouche or self.getBateau(xTir-1,yTir) == bateauTouche or self.getBateau(xTir,yTir+1) == bateauTouche or self.getBateau(xTir,yTir-1) == bateauTouche):
				res = "touché"
			else:
				res = "coulé"
		else:
			# A l'eau ou en vue ?
			if(self.envue(xTir,yTir)):
				res = "En vue"
			else:
				res = "A l'eau"
		return res
