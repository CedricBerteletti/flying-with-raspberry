// @author: Cédric BERTELETTI
// @author: Ulysse BERTELETTI

include <corps.scad>
include <parametres.scad>

pos_rel_moteur_hauteur = 0.46;
moteur_baie_rayon = moteur_trou_rayon+5;

module moteur_trou() {
    rotate([88, 0, 00])
        translate([moteur_position_relative*aile_longueur, aile_hauteur*pos_rel_moteur_hauteur, -aile_largeur*0.3])
            cylinder(h=2*aile_largeur, r1=moteur_trou_rayon, r2=moteur_trou_rayon, center=true, $fn=30);
}
module moteur_nacelle() {
    difference() {
        rotate([88, 0, 0])
            translate([moteur_position_relative*aile_longueur, aile_hauteur*pos_rel_moteur_hauteur, -aile_largeur*0.40])
                cylinder(h=moteur_longueur, r1=moteur_baie_rayon, r2=moteur_baie_rayon, center=true, $fn=30);
        rotate([88, 0, 0])
            translate([moteur_position_relative*aile_longueur, aile_hauteur*(pos_rel_moteur_hauteur+0.1), -aile_largeur*0.2])
                cube([2*moteur_baie_rayon, 2*moteur_baie_rayon, moteur_longueur/2], center=true);
    }
}


difference() {
    union() {
        //moteur_trou();
        corps();
        moteur_nacelle();
        mirror([1, 0, 0]) moteur_nacelle();
    }
    moteur_trou();
    mirror([1, 0, 0]) moteur_trou();
}