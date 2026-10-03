
module m2_trou_vis(hauteur=10) {
    cylinder(h=hauteur, r1=1, r2=1, center=true, $fn=30);
}

module m2_trou_insert(hauteur=10) {
    cylinder(h=hauteur, r1=1.6, r2=1.6, center=true, $fn=30);
}

module m3_trou_vis(hauteur=10) {
    cylinder(h=hauteur, r1=1.5, r2=1.5, center=true, $fn=30);
}

module m3_trou_insert(hauteur=10) {
    cylinder(h=hauteur, r1=2, r2=2, center=true, $fn=30);
}


m2_trou_vis();