import pygame
from pygame.locals import *
#import maze as mz
import path as pa
import time

def drawn( fenetre, pos, playerPos, mur, sol, goal, player, taille_sprite, lvl):
	for x in range(len(lvl)):
		for y in range(len(lvl[x])):
			if lvl[x][y] == 1:
				fenetre.blit( mur, ( x*(taille_sprite), y*(taille_sprite) ) )
			else :
				fenetre.blit( sol, ( x*(taille_sprite), y*(taille_sprite) ) )
	fenetre.blit( goal, ( pos[0]*(taille_sprite), pos[1]*(taille_sprite) ) )
	fenetre.blit( player, ( playerPos[0]*(taille_sprite), playerPos[1]*(taille_sprite) ) )
	
def act(playerpath, playerPos, taille_sprite):
	
	if playerpath:
		playerPos = playerpath.pop()
	return playerPos
		

pygame.init()
fenetre = pygame.display.set_mode( (800, 800) )

pygame.key.set_repeat( 400 , 60 )

pygame.display.flip()

jeu = 1
taille_sprite = 50

#lvl = mz.mazeGenerator()
lvl = pa.maze_2

x_goal = 11
y_goal = 2
pos = (x_goal, y_goal)
playerPos = (0,0)

#ennemi_manager = ennemi_manager(player)

mur = pygame.image.load("red.png")
sol = pygame.image.load("test.png")
player = pygame.image.load("test2.png")
goal = pygame.image.load("goal.png")

playerpath=pa.chemin(playerPos, pos,lvl)
drawn( fenetre, pos, playerPos, mur, sol, goal, player, taille_sprite, lvl)
				
while(jeu):
	for event in pygame.event.get():
		if event.type == QUIT:
			jeu = 0
		elif event.type == KEYDOWN :	
			if event.key == K_SPACE:
				drawn( fenetre, pos, playerPos, mur, sol, goal, player, taille_sprite, lvl)
				playerPos = act(playerpath, playerPos, taille_sprite)
				
		elif event.type == MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			pos = (pos[0]//taille_sprite, pos[1]//taille_sprite)
			if lvl[pos[0] ][pos[1] ] != 1 :
				tmp = time.time()
				playerpath=pa.chemin(playerPos, pos, lvl)
				print(time.time() - tmp)
			drawn( fenetre, pos, playerPos, mur, sol, goal, player, taille_sprite, lvl)
		

	pygame.display.flip()



