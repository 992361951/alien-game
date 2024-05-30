class Settings:
    def __init__(self) -> None:
        self.screen_width=1200
        self.screen_height=800
        self.scree_color=(0,0,0)
        
        self.speed=1
        # bullet的设定
        self.bullet_color=(100,0,0)
        self.bullet_speed = 2.0
        self.bullet_width = 10
        self.bullet_height =20

        self.game_status = False