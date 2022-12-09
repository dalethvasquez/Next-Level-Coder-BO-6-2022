from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import  CLOUD


class Cloud(Sprite):
    def __init__(self, ):
        self.image = CLOUD
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        

    def update(self,  game_speed):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
         
            