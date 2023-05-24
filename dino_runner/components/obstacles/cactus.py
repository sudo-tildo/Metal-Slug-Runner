import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ENEMYTANK, LARGE_CACTUS_Y_POS


class Cactus(Obstacle):
    
    def __init__(self, images):
        self.type = random.randint(0,2)
        self.image = ENEMYTANK[0]
        self.step_index = 0
        super().__init__(images,self.type)

        self.rect.y = LARGE_CACTUS_Y_POS

    def drive(self):
         self.image = ENEMYTANK[self.step_index + 0] 
         self.image = pygame.transform.scale(self.image, (71*2, 56*2))
         self.tank_rect = self.image.get_rect()
         self.rect.y = LARGE_CACTUS_Y_POS 
         self.step_index += 1
         
         if self.step_index == 6:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.drive()
        super().update(game_speed, obstacles)
        

