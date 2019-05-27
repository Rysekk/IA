import pygame
from math import *
import sys
import time
pygame.init()
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))


#couleur
R = 254
V = 0
B = 0
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (120,120,120)
BG_COLOR = GREY


#initialisation paramètre voiture
dehors = False
dedans = False
arrive = True
score = 0
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

#initialisation paramètre circuit
trait_large = 10
largeur_circuit = 600
longeur_circuit = 1000
circuit_x = 50+trait_large
circuit_y = 50+trait_large
route_T = 100
c_droite = circuit_x + longeur_circuit
c_bas = circuit_y + largeur_circuit
c_milieu_hauteur = ((c_bas - route_T)/2) + circuit_y


haut_gauche_ex = (circuit_x, circuit_y)
haut_droit_ex = (c_droite, circuit_y)
bas_gauche_ex = (circuit_x, c_bas)
bas_droit_ex = (c_droite, c_bas)

liste_point_exterieur = [haut_gauche_ex, haut_droit_ex, bas_droit_ex, bas_gauche_ex]



haut_gauche_in = (circuit_x + route_T, circuit_y + route_T)
haut_droit_in = (c_droite - route_T, circuit_y + route_T)
bas_gauche_in = (circuit_x + route_T, c_bas - route_T)
bas_droit_in = (c_droite - route_T, c_bas - route_T)

liste_point_interieur = [haut_gauche_in, haut_droit_in, bas_droit_in, bas_gauche_in]



Start_p1 = (circuit_x, c_milieu_hauteur)
Start_p2 = (route_T + circuit_x, c_milieu_hauteur)
Milieu_p1 = (c_droite - route_T, c_milieu_hauteur)
Milieu_p2 = (c_droite, c_milieu_hauteur)

liste_point_start = [Start_p1,Start_p2]
liste_point_milieu = [Milieu_p1, Milieu_p2]



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
pygame.draw.lines(screen, GREEN, True, liste_point_start, trait_large)
pygame.draw.lines(screen, WHITE, False, liste_point_exterieur, trait_large)
pygame.draw.lines(screen, BLUE, False, liste_point_interieur, trait_large)




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
			elif event.key == pygame.K_r :
				#restart de la voiture
				voiture_x = circuit_x + route_T/2
				voiture_y = (c_bas - route_T)/2 + circuit_y + voiture_longueur
				angle = -90
				voiture_tourne = pygame.transform.rotate(voiture, -angle-90)


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
	pygame.draw.lines(screen, GREEN, True, liste_point_start, trait_large)
	pygame.draw.lines(screen, GREEN, True, liste_point_milieu, trait_large)
	pygame.draw.lines(screen, WHITE, True, liste_point_exterieur, trait_large)
	pygame.draw.lines(screen, BLUE, True, liste_point_interieur, trait_large)
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

		# colision extérieur et intérieur
	if  c_droite < voiture_x or voiture_x < circuit_x or c_bas < voiture_y or voiture_y < circuit_y: 
		R = 0
		V = 0
		B = 255
		if dehors is False:
			print("dehors")
			dehors = True
	elif  c_droite - route_T > voiture_x and voiture_x > circuit_x + route_T and c_bas - route_T > voiture_y and voiture_y > circuit_y + route_T: 
		R = 0
		V = 255
		B = 0
		if dedans is False:
			print("dedans")
			dedans = True
	else:
		dehors = False
		dedans = False
		#ligne d'arrivé et ligne du milieu de course
		if voiture_x > circuit_x and voiture_x < circuit_x+route_T and voiture_y > c_milieu_hauteur and voiture_y < c_milieu_hauteur + 50:#trait_large:
			if arrive is False:
				score = score+1
				print("tour n°"+str(score))
				arrive = True
			R = 255
			V = 255
			B = 255
		elif voiture_x > c_droite - route_T and voiture_x < c_droite and voiture_y > c_milieu_hauteur and voiture_y < c_milieu_hauteur + 50:#trait_large:
			if arrive is True:
				print("milieu du tour n°"+str(score))
				arrive = False
			R = 255
			V = 255
			B = 255
		else:
			R = 255
			V = 0
			B = 0
