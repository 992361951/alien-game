import pygame
import random
import time
from pygame.sprite import Group
from settings import Settings

class Alien(pygame.sprite.Sprite):
    def __init__(self, screen:pygame.Surface , settings) :
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect

        self.image = pygame.image.load( 'image\\alien1.png' )
        self.image=pygame.transform.scale(self.image,(100 , 50) )
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(50, settings.screen_width-50 )
        self.rect.top = random.randint(0 , 250 )

        self.x= float(self.rect.centerx)
        self.y= float(self.rect.top)

        ##记录时间
        self.last_update_time= time.time()

        ##飞船移动速度
        self.Xspeed = round(random.uniform(0.5, 0.5), 1)

    def update (self ):
        current_time = time.time()

        if current_time - self.last_update_time > 0.5:
            # 更新时间
            
            self.last_update_time = current_time
            # 更新水平速度
            self.Xspeed=round(random.uniform(-0.3, 0.3), 1)
        
        self.y += random.uniform(0,0.5)
        self.rect.top= self.y

        self.x += self.Xspeed
        self.rect.centerx = self.x 
            
            
        

    def blitme(self):
        self.screen.blit(self.image,self.rect)

