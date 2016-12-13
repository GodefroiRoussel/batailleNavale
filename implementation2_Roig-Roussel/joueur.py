#!/usr/bin/python
# -*- coding: utf8 -*-
from grille import *
from flotte import *



class Joueur:
	# STRUCTURE DE DONNEES
	# nom : String
	# grille : Grille
	# flotte : Flotte

    def __init__(self, nomJoueur, tailleGrille):
	#Initialise un joueur avec son nom passé en paramètre
	#Initialise sa grille et sa flotte
	#Renvoie erreur si le joueur n'a pas été créé
		self.nom = nomJoueur
		self.grille = Grille(tailleGrille)
		self.flotte = Flotte()

    def name(self):
	#Données: Joueur
	#Pré-conditions: ---
	#Resultat: renvoie Nom du joueur
	#Post-conditions: String
        return self.nom

	def grille(self):
	#Données: Joueur
	#Pré-conditions: ---
	#Resultat: renvoie la Grille du joueur
	#Post-conditions: type Grille
		return self.grille

	def flotte(self):
	#Données: Joueur
	#Pré-conditions: ---
	#Resultat: renvoie la Flotte du joueur
	#Post-conditions: type Flotte
		return self.flotte
