#!/usr/bin/python
# -*- coding: utf8 -*-
from tests_unitaires import *

def main():

    if not (test_creation_flotte()):
        print('Erreur fonction creation flotte');


    if not (test_ajouter_bateau()):
        print('Erreur fonction ajouter bateau');


    if not (test_taille()):
        print('Erreur fonction taille');

    if not (test_touche()):
        print('Erreur fonction touche');


    if not (test_coule_false()):
        print('Erreur fonction coule false');


    if not (test_coule_true()):
        print('Erreur fonction coule true');

    if not (test_Joueur()):
        print('Erreur fonction Joueur');


    if not (test_name()):
        print('Erreur fonction name');


    if not (test_grille()):
        print('Erreur fonction grille');

    if not (test_placerPositionBateau()):
        print('Erreur fonction placer position bateau');


    if not (test_placerPositionBateau_trop_eloigne()):
        print('Erreur fonction placer position : cas du bateau trop eloigne');


    if not (test_getBateau()):
        print('Erreur fonction get bateau');

    if not (test_supprimerPosition()):
        print('Erreur fonction supprimer position');


    if not (test_envue()):
        print('Erreur fonction en vue');

    if not (test_non_envue()):
        print('Erreur fonction en vue');

    if not (test_est_Pas_DansGrille()):
        print('Erreur fonction est dans grille');

    if not (test_estDansGrille()):
        print('Erreur fonction est dans grille');

    if not (test_estBateau()):
        print('Erreur fonction est bateau');

    if not (test_est_Pas_Bateau()):
        print('Erreur fonction est bateau');

    if not (test_verificationCoordonnee()):
        print('Erreur fonction verification coordonnees');

    if not (test_non_verificationCoordonnee()):
        print('Erreur fonction verification coordonnees');

    if not (test_estValide()):
        print('Erreur fonction est valide');

    if not (test_est_Non_Valide()):
        print('Erreur fonction est valide');

    if not (test_non_estVide()):
        print('Erreur fonction est vide');

    if not (test_estVide()):
        print('Erreur fonction est vide');


    if not (test_tirer()):
        print('Erreur fonction tirer');

    if not (test_coule()):
        print('Erreur fonction coule');



print("");
print('Tests Terminés');
