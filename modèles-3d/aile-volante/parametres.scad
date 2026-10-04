// @author: Cédric BERTELETTI
// @author: Ulysse BERTELETTI

// Jeu standard des pièces
jeu_standard = 0.5;

// Taille de l'aile et pas d'intégration
aile_longueur = 1000;
aile_largeur = 700;
aile_hauteur = 120;
pas_integration = 1;
nb_pas = aile_longueur/pas_integration;

// Permet d'avoir une vue éclatée de l'aile pour visualiser les différentes sections
eclate = 0;

// Moteur - Turbine électrique 70mm
moteur_rayon = 70/2;
moteur_longueur = 500;
moteur_position_relative = 0.3; // Position du moteur par rapport à la longueur de l'aile
moteur_trou_rayon = moteur_rayon + jeu_standard;