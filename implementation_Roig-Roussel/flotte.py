#!/usr/bin/python
# -*- coding: utf8 -*-

class Flotte:

#Structure de données
#tailles: [int]


	def __init__(self): 
		#renvoie une nouvelle flotte vide
		#renvoie erreur si la flotte n'a pas été correctement remplacée
		self.tailles = []
		#TO DO : gestion erreur

	def ajouterBateau(self, tailleBat): 
		#Données: Flotte et taille du bateau
		#Pré-conditions: tailleBat:int
		#Resultat: Ajoute un bateau et sa taille à la flotte. Renvoie erreur si le bateau n'a pas été ajouté
		#Post-conditions: Flotte
		self.tailles.append(tailleBat)
		#TO DO : gestion erreur et ajouter le bateau?


	def taille(self, numBat):
		#Données: Flotte et numéro du bateau
		#Pré-conditions: numBat:int
		#Resultat: Renvoie la taille du bateau placé en paramètre
		#Post-conditions: tailleBat:
		return self.tailles[numBat]

	def touche(self, numBat):
		#Données: Flotte et numéro du bateau
		#Pré-conditions: numBat:int
		#Resultat: Décrémente la taille du bateau placé en paramètre et renvoie la flotte modifiée
		#Post-conditions: Flotte
		self.tailles[numBat]-=1

	def coule(self, numBat): 
		#Données: Flotte et numéro du bateau
		#Pré-conditions: numBat:int
		#Resultat: Renvoie True si la taille du bateau est égale à 0, renvoie False sinon
		#Post-conditions: bool
		return self.tailles[numBat]==0
