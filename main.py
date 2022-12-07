from dino_runner.components.game import Game
import pygame

if __name__ == "__main__":
    game = Game()
    game.run()
    print("hello there...")
    pygame.mixer.music.load("la-atmosfera_4.mp3")
    pygame.mixer.play(5)
