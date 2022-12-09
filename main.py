from dino_runner.components.game import Game
import pygame

if __name__ == "__main__":
    game = Game()
    while game.running:
        
        if not game.playing:
            game.show_menu() 
