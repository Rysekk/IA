import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))
RED = (255,0,0)
BG_COLOR = (0,0,0)
voiture_pos = [100, 100]
voiture_largeur = 100
voiture_longueur = 250
game_over = False
speed = voiture_largeur

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x = voiture_pos[0]
			y = voiture_pos[1]
			if event.key == pygame.K_LEFT:
				x -= speed
			elif event.key == pygame.K_RIGHT:
				x += speed
			elif event.key == pygame.K_UP:
				y -= speed
			elif event.key == pygame.K_DOWN:
				y += speed
			voiture_pos = [x,y]

		screen.fill(BG_COLOR)
	pygame.draw.rect(screen, RED, (voiture_pos[0], voiture_pos[1], voiture_largeur, voiture_longueur))

	pygame.display.update()