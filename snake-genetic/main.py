import pygame, random
from genetic_alg import *
from replay import *

# random.seed(settings.seed)


pygame.init()
pygame.font.init()
pygame.display.set_caption('80629 - Snake / Press Escape to quit')

gen_alg()
# replay("individuals-list.pkl","food-list.pkl",15046)
# replay("individuals-list.pkl","food-list.pkl", 0)