import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        # carregar a imagem selecionada
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # "surf" é o nome criado para a variável / convert_alpha otimiza os píxeis transparentes da imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # get_rect() serve para dizer onde começa o retângulo criado
        # "left=0" e "top=0" já é a posição padrão de onde começa o retângulo

    def run(self):
        menu_option = 0  # começa com a primeira opção já selecionada
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # 0 "(-1)" serve para a música ficar em loop

        while True:
            # coloca as imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))  # MIN_WIDTH / 2 para o texto ficar no centro da tela e altura de 70
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # faz parte para aparecer o background na tela

            # Checar por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha a janela
                    quit()  # fecha o pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # caso apertar a tecla para baixo, o texto selecionado do menu vai para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # caso apertar a tecla para cima, o texto selecionado do menu vai para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    # fonte
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
