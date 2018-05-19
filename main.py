import os

import pygame

pygame.init()


# rotate an image while keeping its center and size
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


# create pygame image from sprite name in resource directory
def create_image(sprite_name):
    return pygame.image.load('resources/{0}.png'.format(sprite_name))


sprite_dict = {filename[:-4]: create_image(filename[:-4]) for filename in os.listdir('resources') if
               filename[-4:] == '.png'}


class GameState:

    def __init__(self):
        pass

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class GameEngine:
    states = []
    run = False
    display_width = 0
    display_height = 0
    game_display = None
    clock = None
    font = None

    @staticmethod
    def __init__(width, height, caption):
        GameEngine.states = []
        GameEngine.run = True

        GameEngine.display_width = width
        GameEngine.display_height = height

        GameEngine.game_display = pygame.display.set_mode((GameEngine.display_width, GameEngine.display_height))
        pygame.display.set_caption(caption)

        GameEngine.clock = pygame.time.Clock()

        GameEngine.font = pygame.font.Font("resources/vgaoem.fon", 15)

    @staticmethod
    def change_state(state):
        if not GameEngine.states:
            GameEngine.states.append(state)
        else:
            GameEngine.states[-1] = state

    @staticmethod
    def pause_state(state):
        if not GameEngine.states:
            pass
        else:
            GameEngine.states.append(state)

    @staticmethod
    def resume_state():
        if not GameEngine.states:
            pass
        else:
            GameEngine.states = GameEngine.states[:-1]

    @staticmethod
    def handle_events():
        GameEngine.states[-1].handle_events()

    @staticmethod
    def update():
        GameEngine.states[-1].update()

    @staticmethod
    def draw():
        GameEngine.states[-1].draw()

    @staticmethod
    def running():
        return GameEngine.run

    @staticmethod
    def quit():
        pygame.quit()
        quit()


game = GameEngine(800, 600, 'Game Engine')

while game.running():
    game.handle_events()
    game.update()
    game.draw()

pygame.quit()
