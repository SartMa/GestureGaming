import pygame
from enemysup import import_folder
import time
from math import sqrt
from settings import screen_width


class Obelisk(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.import_character_assets()
        self.frame_index=0
        self.animation_speed=0.20
        self.image = self.animations['idle'][self.frame_index]
        self.lane = lane
        self.y_positions={1:170, 2:300, 3:430}
        self.rect=self.image.get_rect(topleft= (screen_width, self.y_positions[self.lane]))
        self.status='idle'
        # self.hitbox=pygame.Rect(self.rect.x+56, self.rect.y, 80, 93)
        # self.punchLeft=pygame.Rect(self.rect.x, self.rect.y+34, 108, 22)
        # self.punchRight=pygame.Rect(self.rect.x+82, self.rect.y+34, 108, 22)

        # self.speed=1
        # self.health=30
        # self.damage=7.5

        # self.status='run'
        # self.attacking=False
        # self.attack_radius=92
        # self.facing_right=True
        # self.can_attack = True
        # self.hasattacked=False
        # self.taking_damage=False
        # self.dead=False

        

    def import_character_assets(self):
        character_path='./graphics/obelisk/'
        self.animations={'idle':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation]=import_folder(full_path)
            # print(len(self.animations['idle']))

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index+=self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index=0

        image=animation[int(self.frame_index)]
        self.image=image
        
        
       

    def get_status(self, player):
        distx = player.rect.centerx- self.rect.centerx
        disty = player.rect.centery - self.rect.centery

        distance = sqrt(distx**2 + disty**2)
        if self.status=='idle':
            current_time=pygame.time.get_ticks()
            if current_time - self.startidle > 500:
                self.can_attack = True
                self.hasattacked=False
            if self.taking_damage:
                self.status='take_hit'
                self.speed=0
                self.taking_damage=False
        if not self.attacking and self.can_attack:
            if abs(distance)< self.attack_radius:
                self.attacking = True
                self.status='attack'
                self.can_attack = False
                self.frame_index=0
                if distx*self.speed<0:
                    self.facing_right=not self.facing_right
                else:
                    if self.speed == 0:
                        if distx>0 and not self.facing_right:
                            self.facing_right=not self.facing_right
                        elif distx <0 and self.facing_right:
                            self.facing_right=not self.facing_right
                self.speed=0
            else:
                self.status='run'
                if self.facing_right:
                    self.speed=1
                else:
                    self.speed=-1
        else:
            if self.can_attack:
                self.status='run'
                if self.facing_right:
                    self.speed=1
                else:
                    self.speed=-1

        if self.health==0:
            self.dead=True
            if self.status!='death':
                self.frame_index=0
            self.status='death'





    def update(self, shift):
        # self.get_status(player)
        self.animate()
        self.rect.x-=shift
        # self.healthbar.sprite.update((self.rect.x+75 ,self.rect.y-30))
        # self.hitbox=pygame.Rect(self.rect.x+41 ,self.rect.y, 104, 93)
        # self.punchLeft=pygame.Rect(self.rect.x, self.rect.y+34, 108, 22)
        # self.punchRight=pygame.Rect(self.rect.x+82, self.rect.y+34, 108, 22)

class Mushman(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.import_character_assets()
        self.frame_index=0
        self.animation_speed=0.20
        self.image = self.animations['run'][self.frame_index]
        self.lane = lane
        self.y_positions={1:218, 2:350, 3:485}
        self.rect=self.image.get_rect(topleft= (screen_width, self.y_positions[self.lane]))
        self.status='run'
        self.dead= False

    def import_character_assets(self):
        character_path='./graphics/mushroom/'
        self.animations={'run':[], 'death':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation]=import_folder(full_path)
            # print(len(self.animations['run']))

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index+=self.animation_speed
        if self.frame_index >= len(animation):
            if not self.dead:
                self.frame_index=0
            else:
                self.frame_index=len(animation)-1

        image=animation[int(self.frame_index)]
        self.image=image

    def update(self, shift):
        # self.get_status(player)
        self.animate()
        self.rect.x-=shift
        # self.healthbar.sprite.update((self.rect.x+75 ,self.rect.y-30))
        # self.hitbox=pygame.Rect(self.rect.x+41 ,self.rect.y, 104, 93)
        # self.punchLeft=pygame.Rect(self.rect.x, self.rect.y+34, 108, 22)
        # self.punchRight=pygame.Rect(self.rect.x+82, self.rect.y+34, 108, 22)
        

