import pygame
from math import *
import sys
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
ORANGE = (255,255,0)
GREY = (120,120,120)
BG_COLOR = GREY


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


#initialisation paramètre voiture
arrive = True
score = 0
voiture_pos = [100, 100]
voiture_largeur = 25
voiture_longueur = 50
game_over = False
distance_vision = 1200
nb_angle_vision = 20
speed = 2
rayon = sqrt(((voiture_longueur/2) * (voiture_longueur/2)) + ((voiture_largeur/2) * (voiture_largeur/2)))


voiture_x = int(circuit_x + route_T/2)
voiture_y = int((c_bas - route_T)/2 + circuit_y + voiture_longueur)
angle = -90


a_droite = False
a_gauche = False
en_haut = False
en_bas = False



#circuit responsive

haut_gauche_ex = (circuit_x, circuit_y)
haut_droit_ex = (c_droite, circuit_y)
bas_gauche_ex = (circuit_x, c_bas)
bas_droit_ex = (c_droite, c_bas)

liste_point_exterieur = [haut_gauche_ex, haut_droit_ex, bas_droit_ex, bas_gauche_ex]
ligne_ext1 = [haut_gauche_ex, haut_droit_ex]
ligne_ext2 = [haut_droit_ex, bas_droit_ex]
ligne_ext3 = [bas_gauche_ex, bas_droit_ex]
ligne_ext4 = [haut_gauche_ex,bas_gauche_ex]


haut_gauche_in = (circuit_x + route_T, circuit_y + route_T)
haut_droit_in = (c_droite - route_T, circuit_y + route_T)
bas_gauche_in = (circuit_x + route_T, c_bas - route_T)
bas_droit_in = (c_droite - route_T, c_bas - route_T)

liste_point_interieur = [haut_gauche_in, haut_droit_in, bas_droit_in, bas_gauche_in]
ligne_inté1 = [haut_gauche_in, haut_droit_in]
ligne_inté2 = [haut_droit_in, bas_droit_in]
ligne_inté3 = [bas_gauche_in, bas_droit_in]
ligne_inté4 = [haut_gauche_in, bas_gauche_in]
liste_ligne = [ligne_ext1, ligne_ext2, ligne_ext3, ligne_ext4, ligne_inté1, ligne_inté2, ligne_inté3, ligne_inté4]


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
# voiture.fill(BLACK)
# frame suivante avec rotation 
voiture_tourne = voiture.copy()
# déssine la voiture
RAINBOW = (R,V,B)
pygame.draw.rect(voiture_tourne,RAINBOW, (1, 1, voiture_largeur,voiture_longueur))
pygame.draw.lines(screen, GREEN, True, liste_point_start, trait_large)
pygame.draw.lines(screen, WHITE, False, liste_point_exterieur, trait_large)
pygame.draw.lines(screen, BLUE, False, liste_point_interieur, trait_large)



pygame.joystick.init()
stick = [pygame.joystick.Joystick(x) for _x in range(pygame.joystick.get_count())]


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



		elif event.type == pygame.JOYBUTTONDOWN:
			if event.button == 2:
				en_haut = True
			elif event.button == 1:
				en_bas = True
			elif event.button == 9:
				voiture_x = circuit_x + route_T/2
				voiture_y = (c_bas - route_T)/2 + circuit_y + voiture_longueur
				angle = -90
				voiture_tourne = pygame.transform.rotate(voiture, -angle-90)



		elif event.type == pygame.JOYBUTTONUP:
			if event.button == 2:
				en_haut = False
				a_droite = False
				a_gauche = False
			if event.button == 1:
				en_bas = False



		elif event.type == pygame.JOYAXISMOTION:
			if event.axis == 1:
				if en_haut is True:
					if event.value < -0.001:
						a_droite = True
					elif event.value > 0.001:
						a_gauche = True
					else:
						a_droite = False
						a_gauche = False
		elif event.type == pygame.JOYHATMOTION:
			if event.value == (-1,0):
				a_droite = True
				a_gauche = False
			elif event.value == (1,0):
				a_gauche = True
				a_droite = False
			else:
				a_droite = False
				a_gauche  = False

		




	# dessine la voiture
	RAINBOW = (R,V,B)
	pygame.draw.rect(voiture,RAINBOW, (1, 1, voiture_largeur,voiture_longueur))
	pygame.draw.rect(screen,BLUE,(voiture_x,voiture_y,voiture_largeur,voiture_longueur))
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

	rad_angle = angle/ (180 / 3.14)
	rad = (angle-90)/ (180 / 3.14)
	x = 1.1
	pi = 3.14
	décalage = 3
	taille_angle_voiture = 10
	# position angulaire des 4 coins de la voiture
	voiture_angle1 = (voiture_x-décalage + cos(x+rad)*rayon, voiture_y-décalage + sin(x+rad)*rayon)
	voiture_angle2 = (voiture_x-décalage + cos((pi-x)+rad)*rayon, voiture_y-décalage + sin((pi-x)+rad)*rayon)
	voiture_angle3 = (voiture_x-décalage + cos(-x+rad)*rayon, voiture_y-décalage + sin(-x+rad)*rayon)
	voiture_angle4 = (voiture_x-décalage + cos((pi+x)+rad)*rayon, voiture_y-décalage + sin((pi+x)+rad)*rayon)
	list_angle_voiture = [voiture_angle1,voiture_angle2,voiture_angle3, voiture_angle4]
	# pygame.draw.rect(screen, BLUE, (voiture_angle1[0], voiture_angle1[1], taille_angle_voiture, taille_angle_voiture))
	# pygame.draw.rect(screen, RED, (voiture_angle2[0], voiture_angle2[1], taille_angle_voiture, taille_angle_voiture))
	# pygame.draw.rect(screen, BLACK, (voiture_angle3[0], voiture_angle3[1], taille_angle_voiture, taille_angle_voiture))
	# pygame.draw.rect(screen, WHITE, (voiture_angle4[0], voiture_angle4[1], taille_angle_voiture, taille_angle_voiture))
	# pygame.draw.rect(screen,BLUE,(voiture_x - voiture_largeur/2,voiture_y - voiture_longueur/2,voiture_largeur,voiture_longueur))
	# pygame.draw.rect(screen, WHITE, (voiture_x-décalage, voiture_y-décalage, 5, 5))





	#vision
	centre_voiture = (voiture_x, voiture_y)
	for truc in range(0, nb_angle_vision+1) :
		résolution = 180/nb_angle_vision
		rad_vision = (truc * résolution)/ (180 / 3.14)
		p2_x = centre_voiture[0] + cos(rad_vision+rad)*distance_vision
		p2_y = centre_voiture[1] + sin(rad_vision+rad)*distance_vision
		p2 = (p2_x, p2_y)
		distance_centre = distance_vision
		for ligne in liste_ligne :
			x1 = voiture_x
			y1 = voiture_y
			x2 = p2_x
			y2 = p2_y
			x3 = ligne[0][0]
			y3 = ligne[0][1]
			x4 = ligne[1][0]
			y4 = ligne[1][1]
			if x2 == x1:
				coef1 = 10000000000
			else:
				coef1 = (y2 - y1)/(x2 - x1)
			if x4 == x3:
				coef2 = 10000000000
			else:
				coef2 = (y4 - y3)/(x4 - x3)
			ord1 = (-x1*coef1) + y1
			ord2 = (-x3*coef2) + y3
			if coef1 == coef2 :
				para = True
			else:
				inter_x = (ord2 - ord1)/(coef1-coef2)
				inter_y = coef1*inter_x + ord1
				inter = (inter_x,inter_y)
				new_dist = sqrt((voiture_x - inter_x)*(voiture_x - inter_x) + (voiture_y - inter_y)*(voiture_y - inter_y))
				pos1 = inter_x >= x1 and inter_x <= x2 and inter_y >= y1 and inter_y <= y2
				pos2 = inter_x <= x1 and inter_x >= x2 and inter_y <= y1 and inter_y >= y2
				pos3 = inter_x <= x1 and inter_x >= x2 and inter_y >= y1 and inter_y <= y2
				pos4 = inter_x >= x1 and inter_x <= x2 and inter_y <= y1 and inter_y >= y2

				range1 = inter_y >= y3-1 and inter_y <= y4+1 and inter_x >= x3-1 and inter_x <= x4+1

				if pos1 or pos2 or pos3 or pos4:
					if new_dist < distance_centre and range1:
						distance_centre = new_dist
						p2 = inter

		pygame.draw.line(screen, WHITE, centre_voiture, p2, 2)
		pygame.draw.rect(screen, GREEN, (p2[0], p2[1], 5, 5))






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
		voiture_y += speed * sin(rad_angle)
		voiture_x += speed * cos(rad_angle)
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)
	if en_bas is True:
		voiture_y += speed
		voiture_tourne = pygame.transform.rotate(voiture, -angle-90)

		# colision extérieur et intérieur
	dehors_compt = 0
	dedans_compt = 0
	for angles in list_angle_voiture:
		if  c_droite < angles[0] or angles[0] < circuit_x or c_bas < angles[1] or angles[1] < circuit_y: 
				dehors_compt = dehors_compt+1
		elif  c_droite - route_T > angles[0] and angles[0] > circuit_x + route_T and c_bas - route_T > angles[1] and angles[1] > circuit_y + route_T: 
				dedans_compt = dedans_compt+1
		#ligne d'arrivé et ligne du milieu de course
		if angles[0] > circuit_x and angles[0] < circuit_x+route_T and angles[1] > c_milieu_hauteur and angles[1] < c_milieu_hauteur + 50:#trait_large:
			if arrive is False:
				score = score+1
				print("tour n°",score)
				arrive = True
			R = 255
			V = 255
			B = 255
		elif angles[0] > c_droite - route_T and angles[0] < c_droite and angles[1] > c_milieu_hauteur and angles[1] < c_milieu_hauteur + 50:#trait_large:
			if arrive is True:
				print("milieu du tour n°",score)
				arrive = False
			R = 255
			V = 255
			B = 255
		else:
			R = 255
			V = 0
			B = 0
	if dehors_compt > 0:
		R = 0
		V = 0
		B = 255
	elif dedans_compt >0:
		R = 0
		V = 255
		B = 0
	else:
		R = 255
		V = 0
		B = 0