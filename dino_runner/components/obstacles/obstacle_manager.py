import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus_large import LargeCactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.option = list(range(1,10))
    
    def update(self,game_speed , game ):
        if len(self.obstacles) == 0:

            if game_speed <= 50:
                game_speed += 1
                
            random.shuffle(self.option)
            if self.option[0] <3:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.option[0] > 3:
                self.obstacles.append(Bird(BIRD))
            elif self.option[0]:
             self.obstacles.append(LargeCactus(LARGE_CACTUS))
            
    
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles) 
            if game.player.dino_rect.colliderect(obstacle.rect):
                
                
                if not game.player.shield:
                    self.obstacles = []
                    game.player_heart_manager.reduce_heart()

                    if game.player_heart_manager.heart_count > 0:
                        game.player.shield = True
                        game.player.show_text = False
                                     
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.obstacles.pop()
                

    def draw(self, screen):
       
       for obstsacle in self.obstacles:
        obstsacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
