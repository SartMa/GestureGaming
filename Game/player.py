import pygame
from support import import_folder
from bullet import Bullet
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index=0
        self.animation_speed=0.15
        self.image = self.animations['run'][self.frame_index]
        self.rect=self.image.get_rect(topleft = pos)
        self.bulletcount=100

        self.y_positions={1:305, 2:435, 3:565}
        self.dead = False
        self.can_move = True
        self.can_attack = True
        self.status= 'run'
        self.lane = 2
        self.score = 0
        self.startdelay=0
        self.enddelay=0

    def import_character_assets(self):
        character_path='./graphics/player/'
        self.animations={'run':[], 'death':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation]=import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index+=self.animation_speed
        if self.frame_index >= len(animation):
            if self.status=='taking_hit':
                self.status='idle'
                self.taking_damage=False
            elif self.status=='death':
                self.frame_index=len(animation)-1
            if not self.dead:
                self.frame_index=0

        image=animation[int(self.frame_index)]
        self.image=image
        

    def get_input(self):
        keys = pygame.key.get_pressed()

        if not self.dead and self.can_move:
            if keys[pygame.K_UP] and self.lane>1:
                self.can_move = False
                self.startdelay = pygame.time.get_ticks()
                self.lane-=1
            
            elif keys[pygame.K_DOWN] and self.lane<3:
                self.can_move = False
                self.startdelay = pygame.time.get_ticks()
                self.lane+= 1

    

    def get_status(self):
        keys = pygame.key.get_pressed()
        if not self.can_move:
            self.enddelay=pygame.time.get_ticks()
            if(self.enddelay-self.startdelay>200):
                self.can_move=True
        

    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y+= self.direction.y

    def jump(self):
        if(self.on_ground or self.onrope or self.falling):
            self.direction.y=self.jump_speed
            print(self.direction.y, self.on_ground, self.onrope, self.falling)

    def update(self):
      
        self.get_status()
        self.get_input()
        self.rect.y = self.y_positions[self.lane]
        self.animate()
