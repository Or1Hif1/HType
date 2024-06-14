import pygame
import keyboard
import random
import pygame.freetype
import time
pygame.init()


def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img


def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img


def replacer(s, linestring, index, fail=False):
    if not fail and index not in range(len(s)):
        raise ValueError("index outside given string")

    if index < 0:  # add it to the beginning
        return linestring + s
    if index > len(s):  # add it to the end
        return s + linestring

    # insert the new string between "slices" of the original
    return s[:index] + linestring + s[index + 1:]


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


font = pygame.font.Font('Fonts/Barlow-Light.ttf', 20)

white = (255, 255, 255)
grey = (104, 109, 118)
blue = (39, 139, 255)

ft_font = pygame.freetype.SysFont('Barlow', 50)
ft_font2 = pygame.freetype.SysFont('Barlow', 25)
ft_font3 = pygame.freetype.SysFont('Barlow', 25)


words = random_words(12)
text_str = 'Type As Fast As You Can'
enter_text = " "+" "*(len(words)+1)
i = 0
wpm = ""
timer = 0
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
stop_timer = False
while running:
    try:
        canvas.blit(background, (0, 0))
        clock.tick(60)
        print(timer)
        if i == len(words):
            stop_timer = True
            wpm = "wpm: "+str(int(12/(timer/60)))

        text_rect = ft_font.get_rect(text_str)
        text_rect.center = (screen_width//2, 234)
        ft_font.render_to(canvas, text_rect.topleft, text_str, blue)

        text2_rect = ft_font2.get_rect(words)
        text2_rect.center = (screen_width // 2, screen_height//2)
        ft_font2.render_to(canvas, text2_rect.topleft, words, white)

        text4_rect = ft_font3.get_rect(enter_text)
        text4_rect.center = (screen_width//2, screen_height//2)
        ft_font3.render_to(canvas, text2_rect.topleft, enter_text, grey)

        text3_rect = ft_font2.get_rect(wpm)
        text3_rect.center = (screen_width//2, screen_height//2 + 60)
        ft_font2.render_to(canvas, text3_rect.topleft, wpm, blue)

        for event in pygame.event.get():
            if event.type == timer_event and not stop_timer and i > 0:
                timer += 1
            if event.type == pygame.KEYDOWN:

                if event.key == ord(words[i]):
                    enter_text = replacer(enter_text, words[i], i)
                    i += 1
                if event.key == pygame.K_BACKSPACE:
                    enter_text = replacer(enter_text, " ", i-1)
                    i -= 1
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    except IndexError:
        continue
    except ValueError:
        continue


