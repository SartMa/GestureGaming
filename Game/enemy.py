import pygame
from enemysup import import_folder
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
        
    def import_character_assets(self):
        character_path='./graphics/obelisk/'
        self.animations={'idle':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation]=import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index+=self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index=0

        image=animation[int(self.frame_index)]
        self.image=image


    def update(self, shift):
        self.animate()
        self.rect.x-=shift
        

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
        self.animate()
        self.rect.x-=shift
        
        

