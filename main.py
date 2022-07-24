import pygame
import random

# INITIALIZE THE PYGAME
pygame.init()

#CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (800, 600))
#TITLE AND ICON
#isso muda o título que aparece no pygame
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('iconspaceship.png')
#isso coloca a variável icon como icone do pygame
pygame.display.set_icon(icon)

#PLAYER
playerImg = pygame.image.load('spaceship.png')
#essa parte muda o tamanho do player
playerImg = pygame.transform.scale(playerImg, (70, 70))
playerX = 365
playerY = 480
playerX_change = 0

#ENEMY
enemyImg = pygame.image.load('alien.png')
enemyImg = pygame.transform.scale(enemyImg, (50, 50))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#GAME LOOP
running = True
#enquanto a variável running for verdade a janela do pygame vai ficar aberta
while running:
    # isso escolhe a cor do background do pygame
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0,0))
    #esse for quer dizer para todos os eventos dentro da tela do pygamer
    for event in pygame.event.get():
        #se o evento clicado dentro do pygame for o x a tela vai fechar
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether it is right or left
        elif event.type == pygame.KEYDOWN:
            #se pressionarmos o a ou a seta para a esquerda
            if(event.key == pygame.K_a):
                playerX_change = -0.3

            elif (event.key == pygame.K_d):
                playerX_change = 0.3


        elif event.type == pygame.KEYUP:
            if(event.key == pygame.K_a or event.key == pygame.K_d):
               playerX_change = 0

    #Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730
    #Enemy movement
    enemyX += enemyX_change


    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 760:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()







