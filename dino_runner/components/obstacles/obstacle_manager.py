import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus_large import LargeCactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.option = list(range(0,8))
    
    def update(self,game_speed , game ):
        if len(self.obstacles) == 0:
            #self.obstacles.append(Cactus(LARGE_CACTUS))
            #if game_speed <= 60:
                #game_speed += 1
            random.shuffle(self.option)
            if self.option[0] <= 6:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
            if self.option[0] <=2:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            
    
        for obstacle in self.obstacles:
                obstacle.update(game_speed, self.obstacles) 
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if not game.player.shield:

                        pygame.time.delay[300]
                        game.playing = False
                        break
                    else:
                        self.obstacles.pop()


    def draw(self, screen):
        
       for obstsacle in self.obstacles:
        obstsacle.draw(screen)