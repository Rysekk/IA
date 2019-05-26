import pygame
from math import *
pygame.init()
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
RED = (255,0,0)
BLACK = (0,0,0)
BG_COLOR = BLACK
voiture_pos = [100, 100]
voiture_largeur = 100
voiture_longueur = 250
game_over = False
speed = 6
voiture_x = WIDTH/2
voiture_y = HEIGHT/2
a_droite = False
a_gauche = False
en_haut = False
en_bas = False
angle = 0


#######pygame.draw.rect(screen, RED, (voiture_x, voiture_y, voiture_largeur, voiture_longueur))


# define a surface (RECTANGLE)  
voiture = pygame.Surface((voiture_largeur , voiture_longueur))
# fill the rectangle / surface with green color  
voiture.fill(BLACK)
# define rect for placing the rectangle at the desired position  
voiture_tourne = pygame.transform.rotate(voiture, angle)



while not game_over:
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


		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				a_droite = False
			elif event.key == pygame.K_RIGHT:
				a_gauche = False
			elif event.key == pygame.K_UP:
				en_haut = False
			elif event.key == pygame.K_DOWN:
				en_bas = False
	pygame.draw.rect(voiture,RED, (1, 1, voiture_largeur,voiture_longueur))
	screen.fill(BG_COLOR)
	# pygame.draw.rect(screen, RED, (voiture_x, voiture_y, voiture_largeur, voiture_longueur))
	voiture_centre = (voiture_x - voiture_tourne.get_rect().width/2, voiture_y - voiture_tourne.get_rect().height/2)
	screen.blit(voiture_tourne, voiture_centre)
	pygame.display.update()
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