from dino_runner.components.game import Game
import pygame


pygame.init()
pygame.mixer.music.load('METAL-SLUG-1-STAGE-1.mp3')
pygame.mixer.music.play(-1)

if __name__ == "__main__":
    game = Game()

    game.execute()


    