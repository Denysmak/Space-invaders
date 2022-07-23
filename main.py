import pygame

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))



running = True
#enquanto a variável running for verdade a janela do pygame vai ficar aberta
while running:
    #esse for quer dizer para todos os eventos dentro da tela do pygamer
    for event in pygame.event.get():
        #se o evento clicado dentro do pygame for o x a tela vai fechar
        if event.type == pygame.QUIT:
            running = False









