
def A_star(graph, goal, start):
	mouvement = [ (0,1) , (1,0), (-1,0), (0,-1) ] #symetrique
	tmp = []
	frontier = [(start, 0)] #Coordonnee et g
	matrice = graph
	while(frontier):
		current = frontier.pop()
		matrice[ current[0][0]][ current[0][1] ] = current[1] + distance(goal, current[0])
		if current[0] == goal :
			break
		for x in mouvement:
			edge = (current[0][0] + x[0], current[0][1] + x[1])
			if ( 0<= edge[0] < len(graph) ) and ( 0 <= edge[1] < len(graph[0]) ) :
				if graph[edge[0]][edge[1]] == 0:
					frontier.append( (edge , distance(start, current[0]) + distance(goal, edge)) )	#sois on trie tmp sois tout

		frontier = trie_priorite(frontier)
	
	print("\n")
	for i in range(len(matrice)):
		print(matrice[i])
		
	current = goal
	chemin=[]
	visite=[]
	precedent = goal

	tmp=[]

	while (current != start):
		tmp=[]
		for x in range(len(mouvement)):
			#print(current[1], current[0])
			edge = (current[0] + mouvement[x][0], current[1] + mouvement[x][1])
			if ( 0<= edge[0] < len(graph) ) and ( 0 <= edge[1] < len(graph[0]) ) :	
			
				if graph[edge[0]][edge[1]] != -1 and graph[edge[0]][edge[1]] != 0 and edge != precedent and not(edge in chemin) and not(edge in visite) :
					tmp.append( ( (edge), graph[edge[0]][edge[1]] ) )
		
		precedent=current
		
		if ( len(tmp) > 0 ):
			tmp=trie(tmp)
			chemin.append(current)
			visite.append(current)
			current = tmp[0][0]
			print(tmp,end="   ")
		else:
			print(current, " ", visite)
			element=chemin.pop()
			visite.append(element)
			current=element

		print("")
	return(chemin)	

def trie(liste):
	trie=1
	while(trie != 0):
		trie=0
		for i in range (1, len(liste)) :
			if liste[i-1][1] > liste[i][1] : 
				tmp = liste[i-1]
				liste[i-1] = liste[i]
				liste[i] = tmp
				trie+=1
	return(liste)	
		
def trie_priorite( liste ):
	trie=1
	while(trie != 0):
		trie=0
		for i in range (1, len(liste)) :
			if liste[i-1][1] < liste[i][1] : 
				tmp = liste[i-1]
				liste[i-1] = liste[i]
				liste[i] = tmp
				trie+=1
	return(liste)


def distance( coordonne1, coordonne2):
	#Permet de calculer 
	x1,y1= coordonne1
	x2,y2= coordonne2
	return ( max(x1,x2) - min(x1,x2) + max(y1,y2) - min(y1,y2) )

