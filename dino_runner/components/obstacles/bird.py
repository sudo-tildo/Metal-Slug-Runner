import random
import pygame
from dino_runner.utils.constants import BIRD, BIRD_Y_POS, MISSILE
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,1)
        self.image = MISSILE[0]
        self.step_index = 0
        super().__init__(images,self.type)

        self.rect.y = BIRD_Y_POS

    def fly(self):
         self.image = MISSILE[self.step_index + 0] 
         self.image = pygame.transform.scale(self.image, (323/2, 67/2))
         self.missile_rect = self.image.get_rect()
         self.rect.y = BIRD_Y_POS
         self.step_index += 1
         
         if self.step_index == 4:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.fly()
        super().update(game_speed, obstacles)