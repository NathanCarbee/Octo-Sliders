import pygame, sys, random
from Ball import Ball
from Player import Player
from HUD import Text
from HUD import Score
from Button import Button
from BackGround import BackGround
from Level import Level
from Block import Block




pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 10

pygame.display.set_caption("Octo-Sliders")

screen = pygame.display.set_mode(size)

balls = pygame.sprite.Group()
players = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ball.containers = (all, balls)
Player.containers = (all, players)
BackGround.containers = (all, backgrounds)


run = False

all.update(width, height)

dirty = all.draw(screen)
pygame.display.update(dirty)
pygame.display.flip()
clock.tick(60)
