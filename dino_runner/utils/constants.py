import pygame
import os

# Global Constants
TITLE = "Metal Slug Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


SMALL_CACTUS_Y_POS = 300

LARGE_CACTUS_Y_POS = 300

BIRD_Y_POS = 250

CAR_Y_POS = 300

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

# Assets Constants
ICON =  pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive1.png"))

DRIVE = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive8.png"))
]

JUMP = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugJump6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDrive1.png"))
    
]

DUCK = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugDuck7.png"))


]

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame1.png")), 
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame2.png")), 
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlame8.png"))
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDrive8.png"))
]    

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameJump6.png"))
]                  
JUMPING_HAMMER = [ 
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerJump6.png"))
    
                  
]
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugFlameDuck7.png"))

]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Slug/SlugHammerDuck7.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png"))
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

MISSILE = [
    pygame.image.load(os.path.join(IMG_DIR, "Missile/Missile1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Missile/Missile2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Missile/Missile3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Missile/Missile4.png"))
]

ENEMYTANK = [
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "EnemyTank/EnemyTankDrive6.png"))
]

CAR = [
    pygame.image.load(os.path.join(IMG_DIR, "Car/Car1Destroyed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Car/Car2Destroyed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Car/Car3Destroyed.png"))
]
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'PowerUps/FlameShot.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'PowerUps/HeavyMG.png'))

BG = [ 
    pygame.image.load(os.path.join(IMG_DIR, 'Scenario/bg1.png'))
]
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
