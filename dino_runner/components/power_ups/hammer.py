import pygame
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE) 
    pygame.init()
    hammer_sound = pygame.mixer.Sound('HeavyMG.wav')