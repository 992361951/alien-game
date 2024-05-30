import pygame
import sys
from settings import Settings
from ship import Ship
import game_function
from pygame.sprite import Group 

def run_game():
    pygame.init()
    
    ##背景的设置
    settings=Settings()
    screen=pygame.display.set_mode(
    (settings.screen_width , settings.screen_height)
    )

    background = pygame.image.load('image\\background.png')
    background = pygame.transform.scale(background, (settings.screen_width, settings.screen_height))

    ##定义一个Ship类型的对象
    ship=Ship(screen)
    
    bullets = Group()
    aliens = Group()
    

    ##主循环
    while True:
        ##事件检测
        game_function.check_event( ship , bullets ,screen , settings , aliens)

        game_function.update(screen , ship , bullets , aliens)
        
        # screen.blit(background, (0, 0))

        game_function.draw_screen( screen , ship , bullets ,aliens,background)

        pygame.display.flip()

run_game()