import pygame
from settings import screen_width

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        super().__init__()
        self.image = img
        self.rect=self.image.get_rect(topleft = pos)

    def update(self, shift, leftbound, rightbound):
        self.rect.x = self.rect.x - shift
        if(self.rect.x < - leftbound):
            # print(self.rect.x)
            self.rect.x = (rightbound)
        

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size, typ):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('brown')
        self.rect=self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity=0.4
        self.prevx=pos[0]
        self.prevy=pos[1]
        self.type=typ
        if self.type=='fall':
            self.enable=0
        else:
            self.enable=1
        self.beingpushed=False

    def apply_gravity(self):
        self.direction.y+=self.gravity
        self.rect.y+= self.direction.y

    def update(self, x_shift, y_shift):
        self.prevx=self.rect.x
        self.prevy=self.rect.y
        self.rect.x += (x_shift)
        self.rect.x += y_shift

class Rope(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('dark green')
        self.rect=self.image.get_rect(topleft=pos)
    def update(self, x_shift, y_shift):
        self.rect.x += (x_shift)
        self.rect.y += (y_shift)
