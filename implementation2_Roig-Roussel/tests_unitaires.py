#!/usr/bin/python
# -*- coding: utf8 -*-
from joueur import *
from grille import *
from flotte import *
from main import *

#===============================================================
#--------------------------FLOTTE-------------------------------


#---------------------------creation_flotte----------------------
def test_creation_flotte():
    try:
        FlotteTest=Flotte();
        return True;

    except:
        return False;


#FlotteTest=[2,1,6,8,3]

#-------------------------------ajouter_bateau---------------------
def test_ajouter_bateau():
    try:
        FlotteTest.ajouterBateau(2);
        return True;
    except:
        return False;




#-----------------------------taille---------------------
def test_taille():
    FlotteTest.ajouterBateau(1);
    FlotteTest.ajouterBateau(6);
    FlotteTest.ajouterBateau(8);
    FlotteTest.ajouterBateau(3);
    if (FlotteTest.taille(2)!=6):
        return False;
    else :
        return True;

#--------------------------touche------------------------------
def test_touche():
    FlotteTest.touche(2);

    if (FlotteTest.taille(2)!=5):
        return False;
    else :
        return True;


#-----------------------------coule_False----------------
def test_coule_False():
    if (FlotteTest.coule(1)!=False):
        return False;
    else :
        return True;


#--------------------------------coule_True---------------
def test_coule_True():
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);

    if (FlotteTest.coule(1)!=True):
        return False;
    else :
        return True;







#==================================================================
#---------------------------JOUEUR------------------------------
#Joueur


def test_Joueur():
    try:
        joueur1=Joueur(ilias)
        return True;
    except:
        return False;


#---------------------------name--------------------

def test_name():
    if (joueur1.name()!='ilias'):
        return False;
    else :
        return True;








#==================================================================
#---------------------------GRILLE------------------------------
#Grille





#---------------------------Création Grille-------------------------

def test_grille():
    try:
        GrilleTest=Grille(4)
        return True;
    except:
        return False;



#-------------------------AjouterPositionBateau-------------------

def test_placerPositionBateau():
    try:
        GrilleTest.placerPositionBateau(0,0,0);
        return True;
    except:
        return False;


def test_placerPositionBateau_trop_eloigne():
    try:
        GrilleTest.placerPositionBateau(0,0,2);
        return False;
    except:
        return True;




#-------------------------GetBateau-------------------

GrilleTest.placerPositionBateau(0,0,1);
GrilleTest.placerPositionBateau(1,2,0);
GrilleTest.placerPositionBateau(1,2,1);
GrilleTest.placerPositionBateau(1,2,2);

#Grille[[0,-1,1,-1],[0,-1,1,-1],[-1,-1,1,-1]]

def test_getBateau():
    if (GrilleTest.getBateau(2,2)!=1):
        return False;
    else :
        return True;





#-------------------------supprimerPosition-------------------


def test_supprimerPosition():
    GrilleTest.supprimerPosition(2,0)

    if (GrilleTest.estBateau(2,0)==True):
         return False;
    else :
        return True;





#------------------------------envue-----------------------

def test_envue():
    if (GrilleTest.envue(1,2)!=True):
        return False;
    else :
        return True;


def test_non_envue():
    if (GrilleTest.envue(1,3)!=False):
        return False;
    else :
        return True;

#-------------------------estDansGrille-------------------

def test_est_Pas_DansGrille():
    if (GrilleTest.estDansGrille(4,2)!=False):
        return False;
    else :
        return True;


def test_estDansGrille():
    if (GrilleTest.estDansGrille(3,2)!=True):
        return False;
    else :
        return True;



#-------------------------estBateau-------------------

def test_estBateau():
    if (GrilleTest.estBateau(0,1)!=True):
        return False;
    else :
        return True;

def test_est_Pas_Bateau():
    if (GrilleTest.estBateau(0,2)!=False):
        return False;
    else :
        return True;



#-------------------------verificationCoordonées-------------------

def test_verificationCoordonnee():
    if (GrilleTest.verificationCoordonnee(2,1)!=False):
        return False;
    else :
        return True;

def test_non_verificationCoordonnee():
    if (GrilleTest.verificationCoordonnee(1,1)!=True):
        return False;
    else :
        return True;



#------------------------------estValide -------------------

def test_estValide():
    if (GrilleTest.estValide(1,2,0)!=True):
        return False;
    else :
        return True;

def test_est_Non_Valide():
    if (GrilleTest.estValide(1,3,3)!=False):
        return False;
    else :
        return True;




#----------------------------Tirer-----------------------

def test_tirer():
    if (GrilleTest.tirer(0,0)!='touché'):
        return False;
    else :
        return True;


def test_coule():
    if (GrilleTest.tirer(0,1)!='coulé'):
        return False;
    else :
        return True;


#----------------------------estVide------------------------

def test_non_estVide():
    if (GrilleTest.estVide()!=False):
        return False;
    else :
        return True;


def test_estVide():
    GrilleTest.supprimerPosition(0,0);
    GrilleTest.supprimerPosition(0,1);
    GrilleTest.supprimerPosition(2,0);
    GrilleTest.supprimerPosition(2,1);
    GrilleTest.supprimerPosition(2,2);
    if (GrilleTest.estVide()!=True):
        return False;
    else :
        return True;


#EEEEENNNNDDDD
