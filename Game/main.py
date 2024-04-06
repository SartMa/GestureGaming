import pygame, sys
from settings import *
from level import Level
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
level = Level(screen)
mixer.init()
mixer.music.load('music.ogg')
mixer.music.set_volume(0.7)
mixer.music.play(-1)
highscore=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    screen.fill('black')
    

    if(level.gameover):
        if(level.score>highscore):
            highscore=level.score
        level=Level(screen)
        
    level.run()
    score_surf = pygame.Surface((300,50), flags=pygame.SRCALPHA)
    text = f'Hi-score : {int(highscore)}'
    font = pygame.font.Font('Pixeltype.ttf', 32)
    text = font.render(text, True, 'black')
    score_surf.blit(text, (0, 10))
    pygame.Surface.blit(screen, score_surf, (50,10))

    

    pygame.display.update()

   
    clock.tick(60)
