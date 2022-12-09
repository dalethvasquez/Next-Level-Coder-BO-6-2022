from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS
import random


class LargeCactus(Obstacle):
    def __init__(self, image):
      self.type = random.randint(0, 2)
      self.image = LARGE_CACTUS[0]
      super().__init__(image, self.type)
      self.rect.y = 300
      

    