import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 250
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.death_count = 0
        self.score = 0



    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def execute(self):
        self.executing = True
        pygame.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load('METAL-SLUG-1-STAGE-1.mp3')
        pygame.mixer.music.play(-1)
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
       
        
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score+=1

        if self.score%100 == 0:
            self.game_speed+=1
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)

        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG[0].get_width()
        image_height = BG[0].get_height()
        scale_factor = max(SCREEN_WIDTH / image_width, SCREEN_HEIGHT / image_height)
        scaled_width = int(image_width * scale_factor)
        scaled_height = int(image_height * scale_factor)
        
        scaled_bg = pygame.transform.scale(BG[0], (scaled_width, scaled_height))
        self.x_pos_bg -= self.game_speed

        if self.x_pos_bg <= -scaled_width:
            self.x_pos_bg = 0
        
        self.screen.blit(scaled_bg, (self.x_pos_bg, SCREEN_HEIGHT - scaled_height))
        self.screen.blit(scaled_bg, (self.x_pos_bg + scaled_width, SCREEN_HEIGHT - scaled_height))

    def write_screen(self, text, y, font_size = 22, color = (0,0,0)):
        half_screen_width = SCREEN_WIDTH //2

        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, y)
        self.screen.blit(text,text_rect)

    def show_menu(self):
        
        self.screen.fill((255,255,255))

        half_screen_height = SCREEN_HEIGHT //2
        
        
        if self.death_count == 0:
            self.write_screen("Press (S) to start playing", half_screen_height, 25, (0,0,0))
            
        else:
            self.write_screen("Press (S) to start playing", half_screen_height, 25, (255, 0, 0))
            self.write_screen(f"Score: {self.score}", half_screen_height + 25,20,(255,0,0))
            self.write_screen(f"Deaths: {self.death_count}", half_screen_height + 50, 12, (0,0,0))

        
        
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s]:
                    self.run()

                
                    

                    
                    