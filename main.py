import pygame

import gameengine
import states

pygame.init()

game = gameengine.GameEngine(800, 600, 'Game Engine')

game.change_state(states.Menu())

while game.running():
    game.handle_events()
    game.update()
    game.draw()