import sys
import pygame
from settings import Settings
from bullet import Bullet
     
def check_event(ship , bullets , screen, settings):
    for event in pygame.event.get():

        check_quit(event)

        keydown(event,ship ,bullets , screen, settings)
        
        keyup (event,ship)

def keydown(event: pygame.event.Event ,ship  , bullets ,screen ,settings ):
    if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            elif event.key==pygame.K_UP:
                ship.moving_up=True
            elif event.key==pygame.K_DOWN:
                ship.moving_down=True

            # 是否按下空格 产生新的bullet 并且加入到 弹夹 中
            elif event.key == pygame.K_SPACE and len(bullets)<=1:
                new_bullet=Bullet(ship, screen, settings)
                bullets.add(new_bullet)
            
                 

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


def update (screen , ship , bullets):
    ship.update ()

    for bullet in bullets:
        bullet.update()

    for old_bullet in bullets:
        if old_bullet.rect.bottom < 0 :
            bullets.remove(old_bullet)

    

def draw_screen( screen , ship , bullets):
## 每次循环都重新绘制以下图形
## screen.fill( screen_settings.scree_color )
## 白色
    screen.fill((255,255,255))
    ship.blitme()
    
    for bullet in bullets:
         bullet.draw_myself()

