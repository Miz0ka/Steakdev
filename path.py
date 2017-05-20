import math as ma

maze_1 = [ ["0","0","0","0","0"],
	 ["1","1","0","1","0"],
         ["1","0","0","1","0"],
         ["1","0","1","1","0"],
         ["1","0","0","1","0"],
         ["1","0","0","0","0"],
         ["1","1","1","1","0"],
         ["1","0","0","0","0"],
         ["1","0","0","1","0"],
         ["1","0","1","1","0"],
         ["1","0","0","1","0"],
         ["1","0","0","1","0"],
         ["1","0","0","0","0"],
         ["1","0","1","1","0"],
	 ["0","0","0","0","0"] ]


maze_2=[[0,0,0,0,0,0,0,0,0,0,1,0,0,1,0],
        [1,1,0,1,0,0,0,0,1,0,1,0,0,1,0],
        [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
        [1,0,1,1,0,1,0,1,1,1,0,0,0,1,1],
        [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
        [1,1,1,1,0,0,0,1,0,1,0,0,0,0,0],
        [1,0,0,0,0,1,1,1,0,1,0,0,0,0,0],
        [1,0,0,1,0,1,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,0,0,0,1,0,0,0,1,1,0,1],
        [1,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
        [1,0,0,0,0,1,0,1,1,1,0,1,0,0,0],
        [1,0,1,1,0,1,0,1,0,0,0,0,1,0,1],
		[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0,0,1,0]]

def distance (x1, y1, x2, y2):
	return ma.fabs(x1-x2) + ma.fabs(y1-y2)

def ajouteHeuri(liste, noeud):
	for index in range (len(liste)):
		if liste[index].h > noeud.h:
			liste.insert(index, noeud)
			return liste
	liste.append(noeud)
	return liste

def notInHisto ( historique, coordonnee, heuri):
	exit=True
	for ele in historique :
		if coordonnee == ele[0] and heuri >= ele [1] :
			exit = False
			break
	return exit

class noeud():
	def __init__(self, x, y, h, c, prec = None):
		self.x = x
		self.y = y
		self.h = h
		self.c = c #couts
		self.prec = prec
	def coordonnee(self):
		print(self.x,self.y,"\n")
	
def chemin( depart, arriver, terrain) : #depart = (x0, y0) #Arriver= (x1, y1)
	xMax = len(terrain)
	yMax = len(terrain[0])
	historique = [] #liste de tuple ((x,y), h)
	avoir=[] # A Voir
	avoir.append( noeud(depart[0],depart[1], 0, 0) )
	while avoir :
		courrant = avoir.pop(0)
		if (courrant.x == arriver[0] and courrant.y==arriver[1]):
			break
		for x in [-1, 0, 1] :
			for y in [-1, 0, 1] :
				if x*y == 0 and x!=y and  0 <= courrant.x + x < xMax and 0 <= courrant.y + y < yMax:
					#Init values
					x_tmp = courrant.x + x
					y_tmp = courrant.y + y
					cout = courrant.c + 1
					
					heuri = cout + distance( x_tmp, y_tmp, arriver[0], arriver[1] )
					#print(cout, distance( x_tmp, y_tmp, arriver[0], arriver[1]),sep=" + ", end=" = ")
					#print(heuri)
					
					#Add to ToSee
					#TODO != 1 become not(terrain[x_tmp][y_tmp] in mur)
					if ( terrain[x_tmp][y_tmp] != 1 )  and notInHisto(historique, (x_tmp, y_tmp), heuri): #[0]) or courrant.h < historiqye[1]) : #Valeur a modifier		
						avoir = ajouteHeuri( avoir, noeud(x_tmp, y_tmp, heuri, cout, courrant) )

		historique.append( ((courrant.x, courrant.y), courrant.h) ) # ( (x,y), h )

	path = [(courrant.x, courrant.y)]
	while courrant.prec :
		courrant = courrant.prec
		path.append( (courrant.x, courrant.y) )
	return path	

#chemin((0,0), (2,2), maze)
