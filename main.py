import pygame
from assets import Assets
from utils import *
import random
from constants import *

from game_state import GameState
from screens.menu import MenuScreen
from screens.psw import PSWScreen

pygame.init()
# randomised window caption
pygame.display.set_caption(f"Steel and Salvos{random.choice(captions)}")
programIcon = pygame.image.load(resource_path('resources/images/Icon.png'))
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()

pygame.mixer.init()

assets = Assets()
state = GameState()

screens = {
    "main": MenuScreen(assets, state),
    "PSW": PSWScreen(assets, state)
}

FPS = 30
running = True

while running:
    dt     = clock.tick(FPS) / 1000
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    current = screens.get(state.screen)
    if current:
        current.update(dt, events)
        current.draw(screen)
    
    if state.screen == "exit":
        running = False

    pygame.display.update()

pygame.quit()