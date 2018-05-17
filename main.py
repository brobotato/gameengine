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


block_dict = {filename[:-4]: create_image(filename[:-4]) for filename in os.listdir('resources')}


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

    def __init__(self, width, height, caption):
        self.states = []
        self.run = True

        self.display_width = width
        self.display_height = height

        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("resources/vgaoem.fon", 15)
        self.black = (255, 255, 255)

    def change_state(self, state):
        if not self.states:
            self.states.append(state)
        else:
            self.states[-1] = state

    def pause_state(self, state):
        if not self.states:
            pass
        else:
            self.states.append(state)

    def resume_state(self):
        if not self.states:
            pass
        else:
            self.states = self.states[:-1]

    def handle_events(self):
        self.states[-1].handle_events()

    def update(self):
        self.states[-1].update()

    def draw(self):
        self.states[-1].draw()

    def running(self):
        return self.run

    @staticmethod
    def quit():
        pygame.quit()
        quit()


game = GameEngine(800, 600, 'Asteroids')

while game.running():
    game.handle_events()
    game.update()
    game.draw()

pygame.quit()
