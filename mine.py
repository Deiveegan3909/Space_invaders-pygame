
import pygame 
import random

pygame.init()
#screen display
screen = pygame .display. set_mode ((800,600))
# Background
background = pygame.image.load('background.png')
#top icon and caption
pygame.display.set_caption("space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 400
playerX_change = 0

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0
enemyY_change = 0

#enemy
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#define player
def player(x,y):
	screen.blit(playerImg , (x,y))
	
#define player
def enemy(x,y):
	screen.blit(enemyImg , (x,y))	

#define player
def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))	

###
running = True
while running:
	screen.fill ((255,30,0))
	#playerX -= 0.1
	#print(playerX)
	pygame.display.update()
    	
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#keystroke
			if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_LEFT:
									playerX_change -= 5
						    	if event.key == pygame.K_RIGHT:
						    		playerX_change += 5
						    	if event.key == pygame.K_SPACE:
						    		if player_state = "ready":
						    			bulletX = playerX
						    			fire_bullet(bulletX,bulletY)
	        if event.type == pygame.KEYUP:
	        	if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
	        								playerX_change = 0		
    	    								
    playerX += playerX_change
	if playerX <= 0:
	   playerX = 0
    elif playerX >= 736:
        		playerX = 736       		
      
	if enemyX <= 0:
	   enemyX_change = 0
    elif enemyX >= 736:
        		enemyY_change = 736  	
        		
    if bulletY <= 0:
        		         			  		bulletY = 480
        		         			  		bullet_state = "ready"      

    elif bullet_state = "fire":
    	fire_bullet(bulletX,bulletY)
    	bulletY -= bulletY_change
    	
    player(playerX,playerY)
	pygame.display.update()
			
	
	