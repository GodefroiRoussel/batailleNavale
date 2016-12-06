# coding: utf8
""" 
Classe Bateau

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------
"""

class Bateau:

	def __init__(self, taille, dir, pos): return
	#		int x int x position --> Bateau

	"""
	Place le bateau en partant de la position passée en paramètre et en se dirigeant vers 
	la direction souhaitée (0 pour le bas, 1 pour la gauche, 2 pour le haut, 3 pour la droite)
	en fonction de la taille du bateau (compris entre 1 et 4).

	On se place dans le "repère" suivant : 

		y
	    ^
		|
		|
		|
		|
	  0-|------------> x
		0

	On vérifie si les positions calculées du bateau sont comprises entre 0 et 20. 
	Sinon, on renvoie une erreur et on annule la création du bateau.
	"""

	def taille(self): return
	# 		Bateau --> int		

	# Renvoie la taille du bateau (comprise entre 1 et 4).

	def positions(self): return
	#		Bateau --> [Position]

	# Renvoie le tableau des Positions du bateau.

	def nbPosTouche(self): return
	#		Bateau --> int

	# Renvoie le nombre de position touché sur le bateau.

	def touchePosition(pos,self): return
	#		Bateau x Position --> Bateau

	# pos doit être une Position du bateau. Renvoie le Bateau avec cette position touchée.

	def estCoule(self): return
	# 		Bateau --> boolean

	# Renvoie True si nbPosTouche() == taille() sinon False.


	"""
	# ------------------------------------ #
	# ------------ PROPRIETES ------------ #
	# ------------------------------------ #

	Soit bat = Bateau(taille, dir, pos) :

	1/ 	1 <= taille(bat) <= 4
	2/ 	nbPosTouche(bat) == 0 et nbPosTouche(bat) <= taille(bat)
	3/	estCoule(bat) == false
	4/ 	nbPostTouche(touchePosition(bat)) == nbPosTouche(bat) + 1
	5/	(nbPosTouche(bat) == taille(bat)) 
		implique 
		estCoule(bat) == True

	""" 