from BuildStructure.Fragment import Fragment, RING65
frag = Fragment("purine", [
	("C", (-4.4571, -4.57178, 2.10583)),
	("H", (-4.92092, -5.54919, 2.10578)),
	("N", (-5.2663, -3.49261, 2.10575)),
	("C", (-4.69416, -2.26739, 2.10584)),
	("H", (-5.37852, -1.42425, 2.10646)),
	("N", (-3.3888, -1.96405, 2.10532)),
	("C", (-2.60417, -3.05646, 2.10557)),
	("N", (-1.23509, -3.05646, 2.10557)),
	("C", (-0.894016, -4.32599, 2.1069)),
	("H", (0.118568, -4.70836, 2.10767)),
	("N", (-1.98968, -5.14671, 2.10759)),
	("H", (-1.97234, -6.15686, 2.10952)),
	("C", (-3.09908, -4.34928, 2.10621)),
	], [
	((0,1), None),
	((0,2), None),
	((3,2), (-3.91827, -3.28359, 2.10575)),
	((3,4), None),
	((5,3), None),
	((6,5), (-3.91827, -3.28359, 2.10575)),
	((6,7), None),
	((7,8), (-1.96441, -3.98698, 2.10637)),
	((8,9), None),
	((8,10), None),
	((10,11), None),
	((12,10), None),
	((12,6), None),
	((0,12), (-3.91827, -3.28359, 2.10575)),
	])

fragInfo = [RING65, frag]