# coding: utf8
"""
Programme principal du projet bataille navale 

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------------------
"""

# Imports des fichiers
from Flotte import *
from Bateau import *
from Position import *

# Programme principal bataille navale
def main():

	print "Entrez le nom du premier joueur"
	j1_nom = input()
	j1_flotte = Flotte()

	print "Entrez le nom du deuxième joueur"
	j2_nom = input()
	j2_flotte = Flotte()

	# Sauvegarde des données
	flottes = [j1_flotte, j2_flotte]
	noms = [j1_nom, j2_nom]	

	# Construction des flottes
	for j in range (2):
		print "Au joueur ",noms[j]," de saisir ses bateaux."
		for i in range (1,6):

			nb_bat_final = flottes[j].nbBat()
			nb_bat_initial = flottes[j].nbBat()

			# Contrôle ajouterBateau (le nombre de bateau doit varier)
			while (nb_bat_initial == nb_bat_final):

				pos_x = -1
				pos_y = -1
				# Contrôle position
				while (pos_x > 20 and pos_x < 0 and pos_y > 20 and pos_y < 0):
					print noms[j]," saisit la coordonée x (comprise entre 0 et 20) d'une extrémité du bateau ", i
					pos_x = input()

					print noms[j]," saisit la coordonée y (comprise entre 0 et 20) d'une extrémité du bateau  ", i
					pos_y = input()
				# sortie de boucle : 0 <= pos_x <= 20 ET 0 <= pos_y <= 20

				bat_pos = Position(pos_x,pos_y)

				bat_dir = -1
				# Contrôle direction
				while (bat_dir < 0 and bat_dir > 3):
					print "Saisir la direction du bateau (0 bas, 1 gauche, 2 haut, 3 droite)"
					bat_dir = input()
				# sortie de boucle : 0 <= bat_dir <= 3
			
				# il n'y a pas de bateau de taille 5, on en saisit un de taille 3 supplémentaire
				if (i == 5):
					bat = Bateau(3,bat_dir,bat_pos)
				else:
					bat = Bateau(i,bat_dir,bat_pos)

				flottes[j].ajouterBateau(bat)
				nb_bat_final = flottes[j].nbBat()
			# sortie de boucle : on a bien ajouté un bateau supplémentaire (nb_bat_initial < nb_bat_final)

	# Déroulement de la partie

	# compteur_tour % 2 == 1 => c'est au joueur 1 de jouer
	# compteur_tour % 2 == 0 => c'est au joueur 2 de jouer
	compteur_tour = 1

	# Test fin de partie
	while (not(flottes[0].flotteDetruite()) and not(flottes[1].flotteDetruite())):
		joueur_actif = compteur_tour % 2
		joueur_passif = (compteur_tour+1) % 2

		print "Au tour de ", noms[joueur_actif]

		pos_x = -1
		pos_y = -1
		# Contrôle position
		while (pos_x > 20 and pos_x < 0 and pos_y > 20 and pos_y < 0):
			print "Saisit la coordonée x de ton tir :"
			pos_x = input()
			print "Saisit la coordonée y de ton tir :"
			pos_y = input()
			
		# sortie de boucle : 0 <= pos_x <= 20 ET 0 <= pos_y <= 20
		pos = Position(pos_x,pos_y)

		# Résultat du tir sur la flotte de l'adversaire
		resultat = flottes[joueur_passif].verifTir(pos)

		# resultat est de la forme : [statut_tir, indice bateau touché]
		# statut_tir : 1=touché, 2=en vue, 3=à l'eau

		# touché
		if (resultat[0] == 1):
			
			# On accède au bateau touché de l'adversaire
			bateau_touche = flottes[joueur_passif].bateaux()[resultat[1]]
			bateau_touche.touchePosition(pos)

			if bateau_touche.estCoule() :
				print "Coulé !"
			else:
				print "Touché !"

		elif resultat[0] == 2 :
			print "En vue !"
		else: 
			print "A l'eau"

		compteur_tour += 1

	# sortie de boucle : fin de partie	

	print "Fin de la partie !"

	if(flottes[0].flotteDetruite()):
		print noms[1]," a gagné !"
	else:
		print noms[0]," a gagné !"

