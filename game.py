import pygame

pygame.init()

#This creates the size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#This creates and show the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#This is our base model a rectangle and is our player
player = pygame.Rect((250, 200, 25, 25))

#Lets the window keep on running
run = True
while run == True:

#updates the screen to game back to the original state so there is no trail left behind
	screen.fill((0, 0, 0))

#draws the charater and the color
	pygame.draw.rect(screen, (255, 0, 0), player)

#binding the wasd keys to move
	key = pygame.key.get_pressed()
	if key[pygame.K_a] == True:
		player.move_ip(-1, 0)
	elif key[pygame.K_d] == True:
		player.move_ip(1, 0)
	elif key[pygame.K_w] == True:
		player.move_ip(0, -1)
	elif key[pygame.K_s] == True:
		player.move_ip(0, 1)
		
#Allows us to exits out the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
