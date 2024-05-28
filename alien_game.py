import pygame
import sys
from settings import Settings
from ship import Ship
import game_function

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


    ##主循环
    while True:
        game_function.upadate_screen( screen , ship )

        ##事件检测
        game_function.check_event( ship)
        ship.update()

        pygame.display.flip()

run_game()