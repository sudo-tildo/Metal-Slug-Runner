import pygame
import os

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING
from dino_runner.utils.constants import DRIVE, JUMP, DUCK



X_POS = 80
Y_POS = 320
JUMP_VEL = 8.5

class Dinosaur: 
    def __init__(self):
        self.image = DRIVE[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.duck_index = 0
        self.jump_index = 0
        self.jump_vel = JUMP_VEL


    def run(self):
        self.image = DRIVE[self.step_index + 0]
        self.image = pygame.transform.scale(self.image, (62*2, 59*2))
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS - 25
        self.step_index += 1

        if self.step_index == 8:
            self.step_index = 0

        

    def jump(self):
        self.image = JUMP[self.jump_index + 0]
        self.image = pygame.transform.scale(self.image, (55*2, 73*2))
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.9
            self.jump_index += 1

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

        if self.jump_index == 7:
            self.jump_index = 0

    def duck(self):
        self.image = DUCK[self.duck_index + 0]
        self.image = pygame.transform.scale(self.image, (71*2, 42*2))
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 10
        self.duck_index += 1

        if self.duck_index == 7:
            self.duck_index = 0 
        


    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False    
        elif not self.dino_jump:
            self.dino_run = True
    
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_DOWN] and not self.dino_duck and not self.dino_jump:
            self.duck()
        
        

    

        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


    

