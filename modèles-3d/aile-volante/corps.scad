
include <BOSL2/std.scad>
include <BOSL2/nurbs.scad>

// Taille de l'aile et pas d'intégration
longueur = 1000;
largeur = 700;
hauteur = 120;
pas_integration = 1;
nb_pas = longueur/pas_integration;


module profil_aile() {
    //cube([pas_integration, largeur, hauteur], center=false);
    tab_profil = [[0, 0],
        [0, hauteur],
        [largeur, hauteur],
        [largeur, 0]];
    profil = nurbs_curve(tab_profil, 2, type="closed");
    rotate([90, 0, 90])
        linear_extrude(height = 10, center = true)
            polygon(profil);
}


// Points de parcours des nurbs
u = [ for (i = [0 : nb_pas*2]) i/longueur/2 ];


// Évolution de l'échelle verticale (hauteur) de l'aile le long de l'extrusion

tab_echelle_z = [[0, 1.0],
[0.05, 0.95],
[0.15, 0.6],
[0.25, 0.6],
[0.30, 0.8],
[0.35, 0.5],
[0.4, 0.3],
[0.8, 0.1],
[1.0, 0]];

courbe_echelle_z = nurbs_curve(tab_echelle_z,2,u=u);

// Debug / visualisation

control=[for (i = [0 : len(tab_echelle_z)-1])
    [tab_echelle_z[i][0]*1000, tab_echelle_z[i][1]*100] ];
curve = nurbs_curve(control,2,splinesteps=16);
pts = nurbs_curve(control,2,u=[0.537]);
//stroke(curve, 5);
//color("red")move_copies(pts) circle(r=1.5,$fn=16);


// Évolution de l'échelle horizontale (largeur) de l'aile le long de l'extrusion

tab_echelle_y = [[0, 1.0],
[0.05, 1.05],
[0.15, 0.85],
[0.25, 0.93],
[0.30, 0.95],
[0.35, 0.93],
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


// Permet d'avoir une vue éclatée de l'aile pour visualiser les différentes sections
eclate = 0;


module wing() {
    union() {
        for (i = [0 : nb_pas - 1]) {
            index = i/nb_pas;

            //translate([i * (pas_integration+eclate), -largeur*facteur_y/2, 0])
            translate([i * (pas_integration+eclate), -i/2, 0])
                //scale([1, facteur_y, facteur_z])
                scale([1,
                    point_plus_proche(courbe_echelle_y, index)[1],
                    point_plus_proche(courbe_echelle_z, index)[1]])
                    profil_aile();
        }
    }
}


//profil_aile();

wing();
mirror([1,0,0]) wing();





