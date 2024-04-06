import pygame
from settings import screen_width

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, lane):
        super().__init__()
        self.image = pygame.image.load('./graphics/bullet/SpongeBullet.png')
        self.image = pygame.transform.scale(self.image, (3*2, 1*2))
        self.rect=self.image.get_rect(bottomleft= pos)
        self.lane=lane

    def update(self):
        self.rect.x+=5

class BulletPack(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.image = pygame.image.load('./graphics/bullet/tile004.png')
        # self.image = pygame.transform.scale(self.image, (3*2, 1*2))
        self.lane=lane
        self.y_positions={1:320, 2:450, 3: 580}
        self.rect=self.image.get_rect(topleft= (screen_width, self.y_positions[self.lane]))

    def update(self, shift):
        self.rect.x-=shift
