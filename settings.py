class Settings():
    #save alien_invasion settings
    def __init__(self):
        #init game setting
        #screen setting
        self.screen_width=1080
        self.screen_height=650
        self.bg_color=(230,230,230)

        #ship settins
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

