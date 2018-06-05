class Settings():
    #save alien_invasion settings
    def __init__(self):
        #init game setting
        #screen setting
        self.screen_width=1024
        self.screen_height=768
        self.bg_color=(230,230,230)
        self.ship_speed_factor = 1.5

        #bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5