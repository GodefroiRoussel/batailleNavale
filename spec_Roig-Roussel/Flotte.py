# coding: utf8
""" 
Classe Flotte

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------
"""

class Flotte:

  def __init__(self): return
  #         --> Flotte

  # Renvoie une flotte sans bateau. 

  def nbBat(self): return
  #         Flotte --> int

  # Renvoie le nombre de bateau dans la flotte.

  def bateaux(self): return
  #         Flotte --> [Bateau]

  # Renvoie le tableau des bateaux présents dans la flotte.

  def ajouterBateau(self, bateau): return
  #         Flotte x Bateau --> Flotte

  # Ajoute un bateau à la flotte si aucune position n'est déjà occupée par un autre bateau 
  # présent dans la flotte, sinon renvoie la flotte sans ajouter le bateau.  

  def nbBatCoule(self): return
  #         Flotte --> int

  # Renvoie le nombre de bateau(x) coulé(s).

  def flotteDetruite(self): return
  #         Flotte --> bool

  # Renvoie True si tous les bateaux de la flotte sont coulés, sinon False.

  def verifTir(self,pos): return  
  #         Flotte x Position --> [int](2)

  """
  La position doit être valide et :

  	- si le tir "touche" une position d'un bateau non-touchée au préalable
                => renvoie [1] et [indice du bateau touché]
  	- si une position non-touchée d'un bateau se trouve sur la même ligne ou colonne que le tir
  	 ("en vue")
                => renvoie [2] et [-1]
  	- sinon le tir est "à l'eau"    
                => renvoie [3] et [-1] 
  """


  """
  # ------------------------------------ #
  # ------------ PROPRIETES ------------ #
  # ------------------------------------ #

  Soit flotte = Flotte() :
  1/      nbBat(flotte) == 0 (quand construit) et nbBat(flotte) >= 0 (toujours valable)
  2/      nbBatCoule(flotte) >= 0 et nbBatCoule(flotte) <= nbBat(flotte) 

  Soit flotte = Flotte() et bat = Bateau(taille, pos, dir) et ajouterBateau(flotte,bat) :   
  3/     flotteDetruite(flotte) == False   
  4/     Si estCoule(bat) alors nbBatCoule(flotte) == 1
  5/     Si nbBatCoule(flotte) == nbBat(flotte) alors flotteDetruite(flotte) == True
  """
