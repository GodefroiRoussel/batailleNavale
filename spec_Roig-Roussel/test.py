# coding: utf8
"""
Programme de test du projet bataille navale 

@author Godefroi ROUSSEL
@author Clément ROIG

INDICATIONS : 
Les lignes retournant des erreurs sont annotées d'un commentaire "# retourne une erreur". 
Vous vérifierez qu'une erreur apparaît bien puis passerez toute la ligne en commentaire pour poursuivre les tests. 
---------------------------------------------
"""

# Imports des fichiers
from Flotte import * 
from Bateau import *
from Position import *

"""
---- Tests Position ----
6 tests au total
"""
def testPosition():
	nb_test_pos = 6
	nb_test_pos_reussi = 0

	# Tests constructeur
	if (testPos_creerMauvaisePositionX()):	# doit retourner une erreur
		nb_test_pos_reussi += 1
	else:
		print "Echec test : position incorrecte en X, elle n'aurait pas dû être créée"

	if (testPos_creerMauvaisePositionY()):	# doit retourner une erreur
		nb_test_pos_reussi += 1
	else:
		print "Echec test : position incorrecte en Y, elle n'aurait pas dû être créée"

	pos = Position(3,7)	

	if testPos_x():
		nb_test_pos_reussi += 1
	if testPos_y():
		nb_test_pos_reussi += 1
	if testPos_touche():
		nb_test_pos_reussi += 1
	if testPos_devientTouche():
		nb_test_pos_reussi += 1

	return ((float)(nb_test_pos_reussi)/(float)(nb_test_pos)) * 100

def testPos_creerMauvaisePositionX():
	try:
		pos2 = Position(-5,10)
	except Exception:
		return True
	else:
		return False

def testPos_creerMauvaisePositionY():
	try:
		pos2 = Position(5,100)
	except Exception:
		return True
	else:
		return False		

def testPos_x():
	pos = Position(3,7)
	return pos.x()==3

def testPos_y():
	pos = Position(10,7)
	return pos.y()==7

def testPos_touche():
	pos = Position(12,2)
	return not(pos.touche())

def testPos_devientTouche():
	pos = Position(5,2)
	pos.devientTouche()
	return pos.touche()


"""
---- Test Bateau ----
8 tests au total
"""
def testBateau(): 
	nb_test_bat = 8
	nb_test_bat_reussi = 0

	pos = Position(3,7)

	# Tests constructeur
	bat = Bateau(2,2,pos)

	if testBat_creerBateauMauvaiseTaille():
		nb_test_bat_reussi += 1
	else:
		print "Echec test : Le bateau a été créée alors que la taille n'est pas comprise entre 0 et 4 "

	if testBat_creerBateauMauvaisePosition():
		nb_test_bat_reussi += 1
	else:
		print "Echec test : Le bateau n'aurait pas du être créer (dépassement de grille)"
	if testBat_creerBateauMauvaiseDirection():
		nb_test_bat_reussi += 1
	else:
		print "Echec test : Le bateau a été créée alors que la direction n'est pas comprise entre 0 et 3"

	if testBat_taille():
		nb_test_bat_reussi += 1
	if testBat_positions():
		nb_test_bat_reussi += 1
	if testBat_nbPosTouche():
		nb_test_bat_reussi += 1
	if testBat_touchePosition():
		nb_test_bat_reussi += 1
	if testBat_estCoule():
		nb_test_bat_reussi += 1

	return ((float)(nb_test_bat_reussi)/(float)(nb_test_bat)) * 100

def testBat_creerBateauMauvaiseTaille():
	pos = Position(3,7)
	try:
		bat = Bateau(10,0,pos)		# retourne une erreur
	except Exception:
		return True
	else:
		return False
		

def testBat_creerBateauMauvaisePosition():
	pos2 = Position(1,1)
	try:
		bat = Bateau(4,0,pos2) 		# retourne une erreur
	except Exception:
		return True
	else:
		return False

def testBat_creerBateauMauvaiseDirection():
	pos = Position(3,7)
	try:
		bat = Bateau(2,-5,pos) 		# retourne une erreur
	except Exception:
		return True
	else:
		return False	

def testBat_taille():
	pos = Position(3,7)
	bat = Bateau(3,0,pos)
	return bat.taille()==3

def testBat_positions():
	pos = Position(8,12)
	bat = Bateau(3,0,pos)
	# Impossible de tester toutes les valeurs, on en teste deux aléatoires
	return (bat.positions()[1].x()==8) and (bat.positions()[2].y()==10)

def testBat_nbPosTouche():
	pos = Position(3,7)
	bat = Bateau(3,0,pos)
	return bat.nbPosTouche()==0

def testBat_touchePosition():
	pos = Position(9,7)
	bat = Bateau(4,0,pos)
	bat.touchePosition(pos)
	return bat.nbPosTouche()==1

def testBat_estCoule():
	pos = Position(9,7)
	pos2 = Position(9,6)
	bat = Bateau(2,0,pos)
	bat.touchePosition(pos)
	bat.touchePosition(pos2)
	return bat.estCoule()


"""
---- Test Flotte ----
13 tests au total
"""
def testFlotte(): 
	nb_test_flot = 13
	nb_test_flot_reussi = 0

	# Tests constructeurs
	flot = Flotte()

	if testFlotte_nbBat1():
		nb_test_flot_reussi += 1
	if testFlotte_nbBat2():
		nb_test_flot_reussi += 1
	if testFlotte_ajouterBateau1():
		nb_test_flot_reussi += 1
	if testFlotte_ajouterBateau2():
		nb_test_flot_reussi += 1
	if testFlotte_ajouterBateau3():
		nb_test_flot_reussi += 1
	if testFlotte_bateaux():
		nb_test_flot_reussi += 1
	if testFlotte_nbBatCoule1():
		nb_test_flot_reussi += 1
	if testFlotte_nbBatCoule2():
		nb_test_flot_reussi += 1
	if testFlotte_nbBatCoule3():
		nb_test_flot_reussi += 1
	if testFlotte_flotteDetruite():
		nb_test_flot_reussi += 1
	if testFlotte_verifTir1():
		nb_test_flot_reussi += 1
	if testFlotte_verifTir2():
		nb_test_flot_reussi += 1
	if testFlotte_verifTir3():
		nb_test_flot_reussi += 1

	return ((float)(nb_test_flot_reussi)/(float)(nb_test_flot)) * 100

def testFlotte_nbBat1():
	flot = Flotte()
	return flot.nbBat() == 0

def testFlotte_nbBat2():
	flot = Flotte()
	pos = Position(9,7)
	bat = Bateau(4,0,pos)
	return flot.nbBat() == 1

def testFlotte_ajouterBateau1():
	flot = Flotte()
	pos1 = Position(9,7)
	bat1 = Bateau(4,0,pos1)	
	pos2 = Position(15,4)
	bat2 = Bateau(1,2,pos2)	
	flot.ajouterBateau(bat1)
	flot.ajouterBateau(bat2)
	# Les deux bateaux sont ajoutés à la flotte.
	return flot.nbBat()==2

def testFlotte_ajouterBateau2():
	flot = Flotte()
	pos1 = Position(9,7)
	bat1 = Bateau(4,2,pos1)	
	flot.ajouterBateau(bat1)

	pos2 = Position(9,8)
	bat2 = Bateau(3,0,pos2)	
	flot.ajouterBateau(bat2)
	# Le bateau2 empiète sur le bateau1 dans la flotte, il ne doit pas être ajouté.
	return flot.nbBat()==1	

def testFlotte_ajouterBateau3():
	flot = Flotte()
	pos1 = Position(9,7)
	bat1 = Bateau(4,0,pos1)	
	flot.ajouterBateau(bat1)
	flot.ajouterBateau(bat1)
	# Le bateau 1 ne peut pas être ajouté 2 fois à la même flotte.
	return flot.nbBat()==1

def testFlotte_bateaux():
	flot = Flotte()
	pos = Position(9,7)
	bat = Bateau(4,0,pos)
	flot.ajouterBateau(bat)
	return flot.bateaux()[0] is bat

def testFlotte_nbBatCoule1():
	flot = Flotte()
	return flot.nbBatCoule() == 0

def testFlotte_nbBatCoule2():
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(4,0,pos)
	flot.ajouterBateau(bat)
	return flot.nbBatCoule == 0

def testFlotte_nbBatCoule3():
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(1,0,pos)
	flot.ajouterBateau(bat)
	flot.bateaux()[0].touchePosition(pos)
	return flot.nbBatCoule == 1

def testFlotte_flotteDetruite():
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(1,0,pos)
	flot.ajouterBateau(bat)
	flot.bateaux()[0].touchePosition(pos)
	return flot.flotteDetruite()

def testFlotte_verifTir1(): 
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(1,0,pos)
	flot.ajouterBateau(bat)
	# Bateau 0 touché 
	return flot.verifTir(flot,pos)[0]==1 and flot.verifTir(flot,pos)[1]==0

def testFlotte_verifTir2(): 
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(1,0,pos)
	flot.ajouterBateau(bat)

	pos2 = Position(8,15)
	# Bateau 0 en vue
	return flot.verifTir(flot,pos2)[0]==2 and flot.verifTir(flot,pos2)[1]==-1

def testFlotte_verifTir3(): 
	flot = Flotte()
	pos = Position(8,7)
	bat = Bateau(1,0,pos)
	flot.ajouterBateau(bat)

	pos2 = Position(14,15)
	# A l'eau
	return flot.verifTir(flot,pos2)[0]==3 and flot.verifTir(flot,pos2)[1]==-1

# ----------------------------------------------------------------------------
# Programme de test général bataille navale
def main():
	sc_pos = testPosition()
	print "Test Position :",sc_pos," % de reussite"
	print "\n --------------------------- \n"

	sc_bat = testBateau()
	print "Test Bateau : ",sc_bat,"% de reussite"
	print "\n --------------------------- \n"

	sc_flot = testFlotte()
	print "Test Flotte : ",sc_flot,"% de reussite"

main()