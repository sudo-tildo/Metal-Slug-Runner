""""import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CAR, CAR_Y_POS

class Car(Obstacle):
    
    def __init__(self, images):
        self.type = random.randint(0,1)
        self.image = CAR
        self.image = pygame.transform.scale(self.image, (89*2, 39*2))
        self.car_rect = self.image.get_rect()
        super().__init__(images,self.type)

        self.rect.y = CAR_Y_POS"""

    
    
            