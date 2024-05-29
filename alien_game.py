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
    pygame.display.set_caption('Alien Game')

    ##定义一个Ship类型的对象
    ship=Ship(screen)
    bullets = Group()
    

    ##主循环
    while True:
        ##事件检测
        game_function.check_event( ship , bullets ,screen , settings)

        game_function.update(screen , ship , bullets)
        
        game_function.draw_screen( screen , ship , bullets )

        pygame.display.flip()

run_game()