import pygame.font 
 
class Died(): 
 
    def __init__(self,  screen ) : 
        """初始化按钮的属性""" 
        self.screen = screen 
        self.screen_rect = screen.get_rect() 
         
        # 设置 案件 及其 尺寸
        self.image = pygame.image.load("image\\you_died.png")
        self.image = pygame.transform.scale(self.image,(400,100))
        # 创建按钮的rect对象，并使其居中上
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.centery - 100
         
    def blitme (self):
        self.screen.blit(self.image,self.rect)
        