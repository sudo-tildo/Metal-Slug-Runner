import random
import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        
        
    def generate_power_up(self, score):
        
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            random_power = random.randint(0,1)
            if random_power == 0:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())
              

    def update(self, game):
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                hammer_sound = pygame.mixer.Sound("HeavyMG.wav")
                hammer_sound.set_volume(0.07)
                shield_sound = pygame.mixer.Sound("FlameShot.wav")
                shield_sound.set_volume(0.07)
                power_up.start_time = pygame.time.get_ticks()
                player.has_power_up = True
                player.type = power_up.type
                if player.type == Hammer: Hammer.hammer_sound.play()
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

                if player.dino_rect.colliderect(power_up.rect):
                    if power_up.type == "hammer":
                        
                        hammer_sound.play()
                    elif power_up.type == "shield":
                        
                        shield_sound.play()
            


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(200, 300)