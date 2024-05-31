import sys
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien
from you_died import Died   

def check_event(ship , bullets , screen, settings , aliens ,bottom):
    for event in pygame.event.get():

        check_quit(event)

        keydown(event,ship ,bullets , screen, settings)
        
        keyup (event,ship)

        create_alien(aliens , screen , settings)

        # alien碰到左右两边屏幕就转向
        alien_turn(aliens,settings)
        
        # ship与aliens相撞
        if pygame.sprite.spritecollideany(ship, aliens): 
            settings.game_status = False
            change_Gamestatus(settings , screen ,ship)
            push_bottom ( bottom , settings ,aliens , screen)


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

            # 是否按下空格 产生新的bullet 并且加入到 弹夹 中,并发出音效biu
            elif event.key == pygame.K_SPACE and len(bullets)<=1:
                new_bullet=Bullet(ship, screen, settings)
                bullets.add(new_bullet)
                pygame.display.flip()
                sound = pygame.mixer.Sound ('sound\\biu.mp3')
                sound.play()



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

def create_alien ( aliens , screen ,settings):
     if len(aliens) ==0 :
        for _ in range (3)  :
            new_alien = Alien( screen ,settings )
            aliens.add(new_alien)

def alien_turn(aliens,settings):
    for alien in aliens:
            if alien.rect.left < 20:
                alien.Xspeed = abs(alien.Xspeed)

            if alien.rect.right > settings.screen_width - 50 :
                alien.Xspeed = -abs(alien.Xspeed)

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


def update (screen , ship , bullets , aliens, bottom ,settings):
    ship.update ()

    ##当子弹与alien碰撞后，删除他俩
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) 

    for bullet in bullets:
        bullet.update()
    
    ##移除碰到屏幕的子弹
    for old_bullet in bullets:
        if old_bullet.rect.bottom < 0 :
            bullets.remove(old_bullet)

    for alien in aliens :
         alien.update()

    ##移除碰到屏幕的alien
    for alien in aliens :
         if alien.rect.bottom > 790 :
            aliens.remove(alien)
            change_Gamestatus(settings , screen ,ship)
            push_bottom ( bottom , settings ,aliens,screen)

            
            

def draw_screen( screen , ship , bullets , aliens):
## 每次循环都重新绘制以下图形

    screen.fill((0,0,0))

    ship.blitme()

    
    for bullet in bullets:
         bullet.draw_myself()

    for alien in aliens:
         alien.blitme()


def push_bottom ( bottom , settings ,aliens,screen):
     
     while not settings.game_status:
            bottom.blitme()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        settings.game_status = True
                        for alien in aliens :
                             aliens.remove(alien)
                    elif event.key == pygame.K_q :
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if bottom.rect.collidepoint(mouse_x, mouse_y):
                        settings.game_status = True
                        for alien in aliens :
                             aliens.remove(alien)

# def ship_collide_alien( aliens , ship ,settings ):
#     if pygame.sprite.spritecollideany(ship, aliens): 
#         settings.game_status = False

# 当 游戏失败时，会发出boom的一声，并且飞船重置
def change_Gamestatus(settings,screen,ship):
    screen.fill( (230, 230, 230) )
    settings.game_status = False
    sound = pygame.mixer.Sound ('sound\\boom.mp3')
    sound.play()
    died=Died(screen)
    died.blitme()
    pygame.display.flip()    

    ship.moving_left =False
    ship.moving_up = False
    ship.moving_right = False
    ship.moving_down = False