import sys
import pygame
from settings import Settings

def keydown(event: pygame.event.Event ,ship  ):
    if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            elif event.key==pygame.K_UP:
                ship.moving_up=True
            elif event.key==pygame.K_DOWN:
                ship.moving_down=True
            # 是否按下空格发射bullet
        
                 

def keyup(event :pygame.event.Event , ship):
    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_RIGHT: 
                ship.moving_right = False
        elif event.key == pygame.K_LEFT: 
                ship.moving_left = False 
        elif event.key==pygame.K_UP:
                ship.moving_up=False
        elif event.key==pygame.K_DOWN:
                ship.moving_down=False

def check_quit(event:pygame.event.Event):
     # 判断用户是否点了"X"关闭按钮,并执行if代码段
    if event.type == pygame.QUIT:
        #卸载所有模块
        pygame.quit()
        #终止程序，确保退出程序
        sys.exit()
    
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_q :
            pygame.quit()
            #终止程序，确保退出程序
            sys.exit()
     

def check_event(ship):
    for event in pygame.event.get():

        check_quit(event)

        keydown(event,ship)
        
        keyup (event,ship)
                

def upadate_screen( screen , ship ):
## 每次循环都重新绘制以下图形
## screen.fill( screen_settings.scree_color )
## 白色
    screen.fill((255,255,255))
    ship.blitme()

