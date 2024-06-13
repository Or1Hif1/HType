import pygame
import keyboard
import random
import pygame.freetype

pygame.init()


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def random_words(length):
    f = open("dictionary.txt", "r")
    l = str(f.read()).split()
    new_text = ""
    for x in range(int(length/2)):
        index = random.randint(0, 10000)
        new_text += l[index] + " "
    for x in range(int(length/2)):
        index = random.randint(0, 10000)
        new_text += l[index] + " "
    return new_text


screen_width = 1200
screen_height = 700
canvas = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
background = pygame.image.load("Images/background.png")
pygame.display.set_caption("HTYPE")
running = True
clock = pygame.time.Clock()

canvas.blit(background, (0, 0))

font = pygame.font.Font('Fonts/Barlow-Light.ttf', 20)

white = (255, 255, 255)
grey = (104, 109, 118)
blue = (39, 139, 255)

ft_font = pygame.freetype.SysFont('Barlow', 50)
ft_font2 = pygame.freetype.SysFont('Barlow', 25)


words = random_words(12)
text_str = 'Type As Fast As You Can'
enter_text = " "*(len(words)+1)
i = 0
while running and i < len(words):

    clock.tick(60)

    if i == len(words):
        running = False

    text_rect = ft_font.get_rect(text_str)
    text_rect.center = (screen_width//2, 234)
    ft_font.render_to(canvas, text_rect.topleft, text_str, blue)

    text2_rect = ft_font2.get_rect(words)
    text2_rect.center = (screen_width // 2, screen_height//2)
    ft_font2.render_to(canvas, text2_rect.topleft, words, white)
    ft_font2.render_to(canvas, text2_rect.topleft, enter_text, grey)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == ord(words[i]):
                enter_text = replacer(enter_text, words[i], i)
                i += 1
                grey = (104, 109, 118)
            if event.key == pygame.K_BACKSPACE:
                enter_text = replacer(enter_text, " ", i-1)
                i -= 1
                grey = (104, 109, 118)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
