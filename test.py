import pygame
from math import *
pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
BG_COLOR = BLACK
voiture_pos = [100, 100]
voiture_largeur = 50
voiture_longueur = 100
game_over = False
speed = 6
voiture_x = WIDTH/2
voiture_y = HEIGHT/2
a_droite = False
a_gauche = False
en_haut = False
en_bas = False
angle = -90




# définie surface rectangle ou la voiture est dedans 
voiture = pygame.Surface((voiture_largeur , voiture_longueur))
# couleur de la surface
voiture.fill(BLACK)
# frame suivante avec rotation 
voiture_tourne = voiture.copy()
# déssine la voiture
pygame.draw.rect(voiture_tourne,RED, (1, 1, voiture_largeur,voiture_longueur))



while not game_over:

	#regarde les touches qu'on appui
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				a_droite = True
			elif event.key == pygame.K_RIGHT:
				a_gauche = True
			elif event.key == pygame.K_UP:
				en_haut = True
			elif event.key == pygame.K_DOWN:
				en_bas = True

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
	pygame.draw.rect(voiture,RED, (1, 1, voiture_largeur,voiture_longueur))
	# efface tout
	screen.fill(BG_COLOR)
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
		angle = (angle-3)%360
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if a_gauche is True:
		angle = (angle+3)%360
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if en_haut is True:
		voiture_y += speed * sin(angle / (180 / 3.14))
		voiture_x += speed * cos(angle / (180 / 3.14))
	if en_bas is True:
		voiture_y += speed

	if  WIDTH < voiture_x or voiture_x < 0 or HEIGHT < voiture_y or voiture_y < 0:
		print("dehors")
		voiture_x = WIDTH/2
		voiture_y = HEIGHT/2