import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager 
from dino_runner.components.menu_score.menu import*
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.cloud.cloud import Cloud

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_c = 200
        self.y_pos_c = 80
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.running = True
        self.player_heart_manager = PlayerHeartManager()
        self.cloud = Cloud()

    def run(self):
        # Game loop: events - update - draw
        self.points = 0 
        #self.obstacle_manager.reset_obstacles()
        self.player_heart_manager.reset_hearts()
        self.power_up_manager.reset_power_ups(self.points )
        self.playing = True
        pygame.mixer.music.load("la-atmosfera_4.mp3")
        pygame.mixer.music.play(30)
       

        while self.playing:
            self.events()
            self.update()
            self.draw()
           

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.cloud.update(self.game_speed)
        self.score()
        
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 0, 255))
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
            print(self.points)
        score, score_rect = get_score(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.running = True 
        white_color = (255,255,255)
        self.screen.fill(white_color)

        self.print_menu(self.death_count)

        pygame.display.update()

        self.handle_key_events_on_menu()
    

    def print_menu(self,death_count = 0):
        half_screen_height = SCREEN_HEIGHT //2
        

        if death_count == 0:
         text, text_rect = get_centered_message("Press any key to start")
         self.screen.blit(text, text_rect)
            
        elif death_count > 0 :
                text, text_rect = get_centered_message("Press any key to start")
                score, score_rect = get_centered_message("Your score: " + str(self.points), height = half_screen_height + 50)
                self.screen.blit(score, score_rect)
                self.screen.blit(text,text_rect)
                
           
        
    def handle_key_events_on_menu(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                    pygame.display.quit()
                    pygame.quit
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.run()



    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    
     
     
