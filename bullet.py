import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ship:Ship ,screen:pygame.Surface , settings: Settings):
        super().__init__()

        self.screen=screen
        self.screen_rect=screen.get_rect()
        ##子弹的基本属性
        self.color=settings.bullet_color
        self.speed = settings.bullet_speed
        ##画一个子弹
        self.rect=pygame.Rect(0 , 0 , settings.bullet_width , settings.bullet_height)
        self.rect.top = ship.image_rect.top
        self.rect.centerx = ship.image_rect.centerx


    def draw_myself(self):
        pygame.draw.rect(self.screen , self.color , self.rect )

    def fire (self):
        
        self.rect.top -= self.speed##这里可能会出错
        self.draw_myself(self)


