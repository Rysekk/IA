import pygame
from math import *
import sys
pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
R = 254
V = 0
B = 0
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BG_COLOR = BLACK
voiture_pos = [100, 100]
voiture_largeur = 25
voiture_longueur = 50
game_over = False
speed = 2
voiture_x = WIDTH/2
voiture_y = HEIGHT/2
a_droite = False
a_gauche = False
en_haut = False
en_bas = False
angle = -90
haut_gauche_ex = (10,10)
haut_droit_ex = (990,10)
bas_gauche_ex = (10,590)
bas_droit_ex = (990,590)
liste_point_exterieur = [haut_gauche_ex, haut_droit_ex, bas_droit_ex, bas_gauche_ex]
haut_gauche_in = (100,100)
haut_droit_in = (890,100)
bas_gauche_in = (100,490)
bas_droit_in = (890,490)
liste_point_interieur = [haut_gauche_in, haut_droit_in, bas_droit_in, bas_gauche_in]
Start_x = (10,295)
Start_y = (100,295)
liste_point_start = [Start_x,Start_y]


# définie surface rectangle ou la voiture est dedans 
voiture = pygame.Surface((voiture_largeur , voiture_longueur),pygame.SRCALPHA, 32)
voiture = voiture.convert_alpha()
# couleur de la surface
voiture.fill(BLACK)
# frame suivante avec rotation 
voiture_tourne = voiture.copy()
# déssine la voiture
RAINBOW = (R,V,B)
pygame.draw.rect(voiture_tourne,RAINBOW, (1, 1, voiture_largeur,voiture_longueur))
pygame.draw.lines(screen, GREEN, True, liste_point_start, 10)
pygame.draw.lines(screen, WHITE, False, liste_point_exterieur, 10)
pygame.draw.lines(screen, BLUE, False, liste_point_interieur, 10)




while not game_over:

	#regarde les touches qu'on appui
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(1)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				en_haut = True
			elif event.key == pygame.K_DOWN:
				en_bas = True
			elif event.key == pygame.K_LEFT :#and en_haut == True: pour tourner seulement quand on avance
				a_droite = True
			elif event.key == pygame.K_RIGHT :#and en_haut == True: pour tourner seulement quand on avance
				a_gauche = True

		#regarde les touche qu'on qu'on désappui
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				a_droite = False
			elif event.key == pygame.K_RIGHT:
				a_gauche = False
			elif event.key == pygame.K_UP:
				en_haut = False
			elif event.key == pygame.K_DOWN:
				en_bas = False




	# dessine la voiture
	RAINBOW = (R,V,B)
	pygame.draw.rect(voiture,RAINBOW, (1, 1, voiture_largeur,voiture_longueur))
	
	# efface tout
	screen.fill(BG_COLOR)
	pygame.draw.lines(screen, GREEN, True, liste_point_start, 10)
	pygame.draw.lines(screen, WHITE, True, liste_point_exterieur, 10)
	pygame.draw.lines(screen, BLUE, True, liste_point_interieur, 10)
	# pygame.draw.rect(screen, RED, (voiture_x, voiture_y, voiture_largeur, voiture_longueur))
	centre_x = voiture_x - voiture_tourne.get_rect().width/2
	centre_y = voiture_y - voiture_tourne.get_rect().height/2
	voiture_centre = (centre_x, centre_y)
	# remplace l'ancienne image de la voiture par la nouvelle rotationné
	screen.blit(voiture_tourne, voiture_centre)
	# met à jour les bailles
	pygame.display.update()




	# action selon les touches appuiyé
	if a_droite is True:
		angle = (angle-2)%360
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if a_gauche is True:
		angle = (angle+2)%360
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if en_haut is True:
		voiture_y += speed * sin(angle / (180 / 3.14))
		voiture_x += speed * cos(angle / (180 / 3.14))
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if en_bas is True:
		voiture_y += speed
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)

		# ramène la voiture au milieu quand elle sort
	if  WIDTH < voiture_x or voiture_x < 0 or HEIGHT < voiture_y or voiture_y < 0: 
		# change les couleurs
		# R = R+B
		# B = R-B
		# R = R-B
		# B = B+V
		# V = B-V
		# B = B-V
		print("dehors")
		voiture_x = 55
		voiture_y = 290
		angle = -90