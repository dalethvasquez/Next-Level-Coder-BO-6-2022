from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS
import random


class LargeCactus(Obstacle):
    def __init__(self, image):
      self.index = random.randint(0, 2)
      
      super().__init__(image, self.index)
      self.rect.y = 300
      

    