// @author: Cédric BERTELETTI
// @author: Ulysse BERTELETTI

include <BOSL2/std.scad>
include <BOSL2/nurbs.scad>
include <parametres.scad>


module profil_aile() {
    //cube([pas_integration, aile_largeur, aile_hauteur], center=false);
    tab_profil = [
        // Profil inférieur
        [0, 0.1*aile_hauteur],
        [-0.1*aile_largeur, 0],
        [-0.3*aile_largeur, 0.3*aile_hauteur],
        [-0.9*aile_largeur, 0],
        [-aile_largeur, 0],
        // Profil supérieur
        [-0.5*aile_largeur, 0.9*aile_hauteur],
        [-0.25*aile_largeur, aile_hauteur],
        [-0.1*aile_largeur, aile_hauteur*0.85],
        ];
    profil = nurbs_curve(tab_profil, 2, type="closed");
    translate([0, aile_largeur, 0])
        rotate([90, 0, 90])
            linear_extrude(height = pas_integration, center = true)
                polygon(profil);
}


// Points de parcours des nurbs
u = [ for (i = [0 : nb_pas*2]) i/(nb_pas*2) ];


// Évolution de l'échelle verticale (aile_hauteur) de l'aile le long de l'extrusion

tab_echelle_z = [[0, 1.0],
[0.05, 0.95],
[0.15, 0.6],
[moteur_position_relative-0.05, 0.6],
[moteur_position_relative, 0.8],
[moteur_position_relative+0.05, 0.5],
[moteur_position_relative+0.1, 0.3],
[0.8, 0.1],
[0.95, 0.09],
[1.0, 0]];

courbe_echelle_z = nurbs_curve(tab_echelle_z,2,u=u);

// Debug / visualisation

control=[for (i = [0 : len(tab_echelle_z)-1])
    [tab_echelle_z[i][0]*1000, tab_echelle_z[i][1]*100] ];
curve = nurbs_curve(control,2,splinesteps=16);
pts = nurbs_curve(control,2,u=[0.537]);
//stroke(curve, 5);
//color("red")move_copies(pts) circle(r=1.5,$fn=16);


// Évolution de l'échelle horizontale (aile_largeur) de l'aile le long de l'extrusion

tab_echelle_y = [[0, 1.0],
[0.05, 1.05],
[0.15, 0.85],
[moteur_position_relative-0.05, 0.93],
[moteur_position_relative, 0.95],
[moteur_position_relative+0.05, 0.93],
[1.0, 0.5]];

courbe_echelle_y = nurbs_curve(tab_echelle_y,2,u=u);



//  la fonction point_plus_proche permet de trouver le point d'une liste ayant l'abscisse la plus proche de celle passée en paramètre.
function point_plus_proche(courbe, x, i=0, meilleur=undef) =
    len(courbe) == 0 ? undef :
    i >= len(courbe) ? meilleur :
    point_plus_proche(
        courbe,
        x,
        i + 1,
        is_undef(meilleur) || abs(courbe[i][0] - x) < abs(meilleur[0] - x)
            ? courbe[i]
            : meilleur
    );


module moitie () {
    union() {
        for (i = [0 : nb_pas - 1]) {
            index = i/nb_pas;

            translate([i * (pas_integration+eclate), -index*aile_largeur/2, 0])
                scale([1,
                    point_plus_proche(courbe_echelle_y, index)[1],
                    point_plus_proche(courbe_echelle_z, index)[1]])
                    profil_aile();
        }
    }
}

module corps () {
    union() {
        moitie();
        mirror([1,0,0]) moitie();
    }
}


//profil_aile();

//corps();




