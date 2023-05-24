import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, HAMMER_TYPE, SHIELD_TYPE, SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS


class ObstacleManager():
    

    def __init__(self):
        self.obstacles = []
        self.obst = 0
    def update(self, game):
       
        if len(self.obstacles) == 0:
            obst = random.randint(1,3)
            self.obst = obst
            if obst == 1:
                obstacle = Cactus(LARGE_CACTUS)
            elif obst == 2:
                obstacle = Cactus(SMALL_CACTUS)
            else:
                obstacle = Bird(BIRD) 
            
            

            self.obstacles.append(obstacle)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            """ if (game.player.type == SHIELD_TYPE and not self.obst == 3) or (game.player.type == HAMMER_TYPE and self.obst == 3) or not game.player.has_power_up:
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
            else:
                    self.obstacles.remove(obstacle) """
        
            
        
        
   
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()
                