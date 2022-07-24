import pygame

# INITIALIZE THE PYGAME
pygame.init()

#CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

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


def player(x, y):
    screen.blit(playerImg, (x, y))
#GAME LOOP
running = True
#enquanto a variável running for verdade a janela do pygame vai ficar aberta
while running:
    # isso escolhe a cor do background do pygame
    screen.fill((0, 0, 0))
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


    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()







