import pygame
from settings import Settings

## 无法自动补齐其他类传入的参数
class Ship:
    def __init__(self, screen:pygame.Surface):
        ##将背景放进来
        self.screen=screen
        ##载入图片，并获得其矩形属性
        self.image=pygame.image.load("image\\ship.png")
        self.image=pygame.transform.scale(self.image,(100,100))

        self.image_rect=self.image.get_rect()

        ##背景矩阵属性
        self.screen_rect=screen.get_rect()
        ##将飞船初始位置定为背景中下
        # self.image_rect.centerx= self.screen_rect.centerx##这个其实就是rect的x属性
        # self.image_rect.bottom= self.screen_rect.bottom
        ##为了小数点而补上去的
        self.centerx= float(self.screen_rect.centerx)
        self.bottom = float(self.screen_rect.bottom )

        ##飞船速度
        self.settings=Settings()
        self.speed=self.settings.speed

        ##是否按下有方向键(默认为否)
        self.moving_right = False
        self.moving_left =False
        self.moving_up = False
        self.moving_down = False



    def blitme(self):
        self.screen.blit(self.image,self.image_rect)

    def update(self):
        # 水平方向
        if self.moving_right == True and self.image_rect.right < self.screen_rect.right:
            self.centerx += self.speed
        
        if self.moving_left == True and self.image_rect.left > 0 :
            self.centerx -= self.speed
        
        self.image_rect.centerx = self.centerx

        # 竖直方向
        if self.moving_up == True and self.image_rect.top > 0:
            self.bottom -= self.speed

        if self.moving_down == True and self.image_rect.bottom < self.screen_rect.bottom :
            self.bottom += self.speed

        self.image_rect.bottom = self.bottom

    