import pygame

print('Setup start')
pygame.init()
janela = pygame.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop start')
while True:
    # Checar por todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fecha a janela
            quit()  # fecha o pygame
