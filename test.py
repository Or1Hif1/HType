import pygame
import pygame.freetype

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
ft_font = pygame.freetype.SysFont('Fonts/Bn Barak.ttf', 50)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    text_str = 'Player 1    9:8    Player 2'
    text_rect = ft_font.get_rect(text_str)
    text_rect.center = window.get_rect().center
    ft_font.render_to(window, text_rect.topleft, text_str, (100, 200, 255))
    pygame.display.flip()

pygame.quit()
exit()
