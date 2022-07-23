import pygame

# INITIALIZE THE PYGAME
pygame.init()

#CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

#TITLE AND ICON
#isso muda o título que aparece no pygame
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
#isso coloca a variável icon como icone do pygame
pygame.display.set_icon(icon)

#GAME LOOP
running = True
#enquanto a variável running for verdade a janela do pygame vai ficar aberta
while running:
    #esse for quer dizer para todos os eventos dentro da tela do pygamer
    for event in pygame.event.get():
        #se o evento clicado dentro do pygame for o x a tela vai fechar
        if event.type == pygame.QUIT:
            running = False
    #isso escolhe a cor do background do pygame
    screen.fill((255, 0, 0))
    pygame.display.update()







