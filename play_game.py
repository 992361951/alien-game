import pygame
import sys
from settings import Settings
from ship import Ship
import game_function
from pygame.sprite import Group 
from bottom import Bottom

def run_game():
    pygame.init()
    
    ##背景的设置
    settings=Settings()

    screen=pygame.display.set_mode(
    (settings.screen_width , settings.screen_height)
    )

    ship=Ship(screen)
    bottom = Bottom ( screen )

    bullets = Group()
    aliens = Group()

    while True:
        ##事件检测
        
        game_function.check_event( ship , bullets ,screen , settings , aliens , bottom)

        game_function.update(screen , ship , bullets , aliens, bottom , settings)
         
        game_function.draw_screen( screen , ship , bullets ,aliens)

        #当游戏状态为false时，弹出botttom，并用鼠标点击才能重新玩

        game_function.push_bottom( bottom,settings,aliens ,screen)

        pygame.display.flip()

run_game()