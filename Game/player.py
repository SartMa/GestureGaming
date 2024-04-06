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
        # self.bullets= pygame.sprite.Group()

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

        
            # if keys[pygame.K_UP]:
            #     self.frame_index=0
            #     if self.falling:
            #         self.falling=False
            #     self.jump()

            # if keys[pygame.K_SPACE] and not self.attacking:
            #     self.attacking=True
            #     self.startattack=pygame.time.get_ticks()
            #     self.frame_index=0
            
            # if keys[pygame.key.key_code("S")] and self.onrope:
            #     self.rect.y+=1
            
            # if keys[pygame.key.key_code("W")] and self.onrope:
            #     self.rect.y-=1

            # if self.climbing and keys[pygame.key.key_code("D")]:
            #     self.onrope=True
            #     self.gravity=0
            #     self.direction.y=0
            # else:
            #     self.gravity=0.4
            #     self.onrope=False

    

    def get_status(self):
        keys = pygame.key.get_pressed()
        # print(self.can_move)
        if not self.can_move:
            self.enddelay=pygame.time.get_ticks()
            if(self.enddelay-self.startdelay>150):
                self.can_move=True
        # if self.direction.y<0:
        #     self.status='jump'
        # elif self.direction.y>1:
        #     self.status='fall'
        # else:
        #     if self.direction.x!=0:
        #         self.status='run'
        #     else:
        #         self.status='idle'
        # if self.attacking:
        #     self.status='attack'
        #     endattack=pygame.time.get_ticks()
        #     if(endattack-self.startattack>670):
        #         self.attacking=False
        #         self.hasattacked=False
        #     #pygame.time.set_timer(self.attacking=False, 700)
        # if self.onrope:
        #     self.status='climb'
        #     if keys[pygame.key.key_code("W")] or keys[pygame.key.key_code("S")]:
        #         self.animation_speed=0.15
        #     else:
        #         self.animation_speed=0
        # else:
        #     self.animation_speed=0.15

        # if self.taking_damage:
        #     self.status='take_hit'
        #     self.direction.x=0
        #     self.taking_damage=False

        # if self.health==0:
        #     self.status='dead'
        #     self.dead=True
                
    

        # self.bullets.update()
        

    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y+= self.direction.y

    def jump(self):
        if(self.on_ground or self.onrope or self.falling):
            self.direction.y=self.jump_speed
            print(self.direction.y, self.on_ground, self.onrope, self.falling)

    def update(self):
        #self.prevx=self.rect.left
        #self.prevy=self.rect.top
        # self.get_input()
        self.get_status()
        self.get_input()
        self.rect.y = self.y_positions[self.lane]
        # print(self.lane)
        self.animate()
        # self.healthbar.sprite.update((self.rect.x+5 ,self.rect.y-20))