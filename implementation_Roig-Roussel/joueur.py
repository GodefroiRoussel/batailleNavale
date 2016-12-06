#!/usr/bin/python
# -*- coding: utf8 -*-
#from grille import *
#from flotte import *



class Joueur:
	# STRUCTURE DE DONNEES
	# nom : String
	# tailleGrille : int


	def __init__(self, nomJoueur, tailleGrille): 
	#Initialise un joueur avec son nom passé en paramètre
	#Renvoie erreur si le joueur n'a pas été créé
		self.nom=nomJoueur
		self.tailleGrille= tailleGrille

	def name(self): 
	#Données: Joueur
	#Pré-conditions: ---
	#Resultat: renvoie Nom du joueur
	#Post-conditions: String
		return self.nom











