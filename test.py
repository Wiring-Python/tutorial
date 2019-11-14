import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30
# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((720, 480), 0, 32)
pygame.display.set_caption('animation')

# set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 180)
red = (255, 0, 0)

f_image = pygame.image.load('front.png')
b_image = pygame.image.load('back.png')


class Card:
    def __init__(self, name, x, y):
        self.card = pygame.image.load(name)
        self.x = x
        self.y = y
        self.toggle = False
        self.angle = 0
        self.dx = 0
        self.dy = 0
        self.FB = True


def GetW(angle):
    if angle <= 30:
        return 60 - (angle * 2)
    return (angle - 30) * 2


draw = Card("front.png", 50, 120)
flip = Card("front.png", 300, 300)

# text setting
font_obj = pygame.font.Font('freesansbold.ttf', 32)
text_surface_obj = font_obj.render('Hello World!', True, green, black)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 50)

while True:
    # the main game loop
    screen.fill(white)

    # draw the text onto the surface
    screen.blit(text_surface_obj, text_rect_obj)
    if draw.toggle:
        draw.dx += 10
        if draw.dx == 500:
            draw.dx = 0
            draw.toggle = False

    screen.blit(draw.card, (draw.x + draw.dx, draw.y + draw.dy))
    if flip.toggle:
        flip.angle = flip.angle + 6
        if flip.angle == 30:
            if flip.FB:
                flip.card = b_image
                flip.FB = False
            else:
                flip.card = f_image
                flip.FB = True
        elif flip.angle == 60:
            flip.angle = 0
            flip.toggle = False
    screen.blit(pygame.transform.scale(flip.card, (GetW(flip.angle), 80)),
                (flip.x + 30 - (GetW(flip.angle) / 2) + flip.dx, flip.y + flip.dy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 = flip.x + 30 - (GetW(flip.angle) / 2)
            y1 = flip.y
            x2 = flip.x + 30 + (GetW(flip.angle) / 2)
            y2 = flip.y + 80
            if x1 <= pygame.mouse.get_pos()[0] <= x2 and y1 <= pygame.mouse.get_pos()[1] <= y2 and flip.toggle is False:
                flip.toggle = True
            x1 = draw.x
            y1 = draw.y
            x2 = draw.x + 60
            y2 = draw.y + 80
            if x1 <= pygame.mouse.get_pos()[0] <= x2 and y1 <= pygame.mouse.get_pos()[1] <= y2 and draw.toggle is False:
                draw.toggle = True

    pygame.display.update()
    fpsClock.tick(FPS)



