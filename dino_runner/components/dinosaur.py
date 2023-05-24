import pygame
import os
from dino_runner.utils.hitbox import fix_rect
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, RUNNING_HAMMER, JUMPING_HAMMER
from dino_runner.utils.constants import DRIVE, JUMP, DUCK



X_POS = 80
Y_POS = 320
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCK, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMP, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: DRIVE, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

Y_POS_DUCK = 340

class Dinosaur: 
    def __init__(self):
        self.image = DRIVE[0]
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.size = fix_rect(self.dino_rect, 0.70)
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.dino_run = False
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.duck_index = 0
        self.jump_index = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False
        
        pygame.init()
       
        slug_drive = pygame.mixer.Sound('SlugDriving.wav')
        slug_drive.play(-1)
        slug_drive.set_volume(0.06)


    def run(self):
        
        self.dino_run = True
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.image = DRIVE[self.step_index + 0]
        self.image = pygame.transform.scale(self.image, (62*2, 59*2))
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS - 25
        self.step_index += 1
        
        
        
        if self.step_index == 8:
            self.step_index = 0

         
        
        

    def jump(self):
        self.image = JUMP[self.jump_index, 0]
        self.image = JUMP_IMG[self.type]
        self.image = pygame.transform.scale(self.image, (55*2, 73*2))
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.7
            self.jump_index += 1

        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
        
        if self.jump_index == 7:
            self.jump_index = 0

    def duck(self):
        self.image = DUCK[self.duck_index + 0]
        self.image = DUCK_IMG[self.type][self.step_index//5]
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


    

