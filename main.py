import os

import pygame

import gameengine

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

game = gameengine.GameEngine(800, 600, 'Game Engine')

while game.running():
    game.handle_events()
    game.update()
    game.draw()
