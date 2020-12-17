import sys
import pygame
from pygame.locals import *


pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True

class Blauwdruk:

    Lives = 5
    Coins = 10
    def __init__(self, Lives):
        self.Lives = Lives

print("Blauwdruk.Lives", Blauwdruk.Lives)

Player1 = Blauwdruk
Player1.Lives = 10

print("Player1.Lives", Player1.Lives)


playerSprite = pygame.image.load("../Art/spr_Player.png")
playerRect = playerSprite.get_rect()
playerSpeed = 5


while IS_RUNNING:


    KEYS_DOWN = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    if (KEYS_DOWN[K_UP]):
        playerRect.y -= playerSpeed
    elif (KEYS_DOWN[K_DOWN]):
        playerRect.y += playerSpeed

    if (KEYS_DOWN[K_LEFT]):
        playerRect.x -= playerSpeed
    elif (KEYS_DOWN[K_RIGHT]):
        playerRect.x += playerSpeed
    


    SCREEN.fill(BG_COLOUR)

   
    SCREEN.blit(playerSprite, playerRect)
    

    pygame.display.flip()

    CLOCK.tick(FPS)
