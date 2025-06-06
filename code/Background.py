from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background (Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade com que a imagem se move

        if self.rect.right <= 0:  # se a ponta direita da imagem chegar na posição 0 do eixo x,
            self.rect.left = WIN_WIDTH  # a ponta esquerda vai para a ponta direita (largura da tela)
