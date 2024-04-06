import pygame
from tiles import Tile
from player import Player
from settings import screen_width, screen_height
from enemy import Obelisk, Mushman
from enemysup import import_folder
from bullet import Bullet, BulletPack
import random


class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_level()
        self.time=0
        self.phase=0
        self.obeliskfreq = {0:100, 1: 90, 2:80, 3:70, 4:60, 5:50}
        self.phasetime=0
        self.gameover=False
        self.score=0

    def setup_level(self):
        self.bldg1_tiles = pygame.sprite.Group()
        self.bldg2_tiles = pygame.sprite.Group()
        self.bldg3_tiles = pygame.sprite.Group()
        self.cloud1_tiles = pygame.sprite.Group()
        self.cloud2_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.obelisks = pygame.sprite.Group()
        self.ground = pygame.sprite.GroupSingle()
        self.moon = pygame.sprite.GroupSingle()
        self.roads = pygame.sprite.Group()
        self.paving = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.bullets = pygame.sprite.Group()
        self.obelisks = pygame.sprite.Group()
        self.obelisks1 = pygame.sprite.Group()
        self.obelisks2 = pygame.sprite.Group()
        self.obelisks3 = pygame.sprite.Group()
        self.mushes = pygame.sprite.Group()
        self.bulletpacks = pygame.sprite.Group()


        self.time1=0
        self.time2=0
        self.time3=0



        player = Player((50, 435))
        self.player.add(player)

        bldg1_tiles=import_folder('./graphics/bg/bldg1')
        for i in range(len(bldg1_tiles)):
            bldg = Tile((723*i, float(screen_height/5 -70)), bldg1_tiles[i])
            self.bldg1_tiles.add(bldg)
        
        bldg2_tiles=import_folder('./graphics/bg/bldg2')
        for i in range(len(bldg2_tiles)):
            bldg = Tile((723*i, screen_height/5-50), bldg2_tiles[i])
            self.bldg2_tiles.add(bldg)

        bldg3_tiles=import_folder('./graphics/bg/bldg3')
        for i in range(len(bldg3_tiles)):
            bldg = Tile((723*i, screen_height/5), bldg3_tiles[i])
            self.bldg3_tiles.add(bldg)

        cloud1_tiles=import_folder('./graphics/bg/clouds1')
        for i in range(len(cloud1_tiles)):
            cloud = Tile(((screen_width/6)*(i), screen_height/11 ), cloud1_tiles[i])
            self.cloud1_tiles.add(cloud)

        cloud2_tiles=import_folder('./graphics/bg/clouds2')
        for i in range(len(cloud2_tiles)):
            cloud = Tile(((screen_width/6)*(i)+110, screen_height/19 ), cloud2_tiles[i])
            self.cloud2_tiles.add(cloud)

        ground_tile=import_folder('./graphics/bg/ground')
        for i in range(len(ground_tile)):
            bldg = Tile((0, -150), ground_tile[i])
            self.ground.add(bldg)

        moon_tile=import_folder('./graphics/bg/moon')
        for i in range(len(moon_tile)):
            bldg = Tile((400, 0), moon_tile[i])
            self.moon.add(bldg)

        road_tiles=import_folder('./graphics/bg/road')
        for i in range(len(road_tiles)):
            cloud = Tile((660*i, screen_height-371), road_tiles[i])
            self.roads.add(cloud)

    def handle_bullets(self):
        player=self.player.sprite
        keys = pygame.key.get_pressed()

        if player.can_attack and (not player.dead) and keys[pygame.K_SPACE] and player.bulletcount>0:
            self.bullets.add(Bullet((player.rect.x + 48, player.rect.y + 29), player.lane))
            player.bulletcount-=1
            self.startattack = pygame.time.get_ticks()
            player.can_attack = False

        if not player.can_attack:
            self.endattack = pygame.time.get_ticks()
            if(self.endattack - self.startattack>250):
                player.can_attack = True

        for bullet in self.bullets:
            if(bullet.rect.x>screen_width+20):
                bullet.kill()

        # print(len(self.bullets))

        # print(player.can_attack)
                
    def handle_obelisks(self):
        self.time+=1
        if(self.time%(self.obeliskfreq[self.phase])==0):
            lane = random.randint(1, 3)
            ob =Obelisk(lane)
            if(lane==1):
                self.obelisks1.add(ob)
                

            if(lane==2):
                self.obelisks2.add(ob)


            if(lane==3):
                self.obelisks3.add(ob)
                pass
            self.time=0
            self.obelisks.add(ob)
        # print(len(self.obelisks3))

        for obelisk in self.obelisks:
            if obelisk.rect.x<-135:
                pygame.sprite.Sprite.kill(obelisk)

    def handle_mushmen(self):
        player=self.player.sprite
        self.endattack = pygame.time.get_ticks()
        num = random.randint(0,8)
        flag=0
        if(len(self.obelisks1)==0 and self.endattack-self.time1>1000):
            if num==3 and player.bulletcount<20:
                self.bulletpacks.add(BulletPack(1))
                flag=1
            else:
                self.mushes.add(Mushman(1))
            self.time1 = pygame.time.get_ticks()  
        if(len(self.obelisks2)==0 and self.endattack-self.time2>1000):
            if num==3 and flag==0 and player.bulletcount<20:
                self.bulletpacks.add(BulletPack(2))
                flag=1
            else:
                self.mushes.add(Mushman(2))
            self.time2 = pygame.time.get_ticks()  
        if(len(self.obelisks3)==0 and self.endattack-self.time3>1000):
            if num==3 and flag==0 and player.bulletcount<20:
                self.bulletpacks.add(BulletPack(3))
            else:
                self.mushes.add(Mushman(3))
            self.time3 = pygame.time.get_ticks()      

        for mush in self.mushes:
            if mush.rect.x<-151:
                mush.kill() 

        for bp in self.bulletpacks:
            if bp.rect.x<-151:
                bp.kill() 

    def collisions(self):
        player=self.player.sprite
        for ob in self.obelisks:
            if(ob.rect.x+51<player.rect.x+60 and ob.rect.x+131> player.rect.x+25 and player.lane==ob.lane and not player.dead):
                player.status='death' 
                player.frame_index=0
                player.dead=True

        for mush in self.mushes:
            if(mush.rect.x+51<player.rect.x+60 and mush.rect.x+130> player.rect.x+25 and player.lane==mush.lane and not player.dead):
                player.status='death' 
                player.frame_index=0
                player.dead=True

            for bullet in self.bullets:
                if(mush.rect.x+51<bullet.rect.x+6 and mush.rect.x+130> bullet.rect.x and bullet.lane==mush.lane):
                    self.score+=5
                    mush.kill()
                    bullet.kill()
            
        for bp in self.bulletpacks:
            if(bp.rect.x-5<player.rect.x+60 and bp.rect.x+26>player.rect.x+25 and player.lane==bp.lane and not player.dead):
                player.bulletcount+=10
                bp.kill()
                


    def run(self):
        player=self.player.sprite

        self.phasetime+=1
        if not player.dead:
            self.score+=0.1
        # print(player.bulletcount)
        if(self.phasetime>500 and self.phase<5):
            self.phase+=1
            self.phasetime=0
        # print(self.phase, self.phasetime)
            

        
        
        self.ground.draw(self.display_surface)
        self.moon.draw(self.display_surface)

        if not player.dead:
            self.cloud2_tiles.update(1, 120, screen_width)
            self.cloud1_tiles.update(1, 120, screen_width)
            self.bldg3_tiles.update(1+self.phase, 723, 723*2)
            self.bldg2_tiles.update(2+self.phase, 723, 723*2)
            self.bldg1_tiles.update(3+self.phase, 723, 723*2)
            self.roads.update(4+1*(self.phase), 660, 660*2)


        self.cloud2_tiles.draw(self.display_surface)
        self.cloud1_tiles.draw(self.display_surface)
        self.bldg3_tiles.draw(self.display_surface)
        self.bldg2_tiles.draw(self.display_surface)
        self.bldg1_tiles.draw(self.display_surface)
        self.roads.draw(self.display_surface)

        bullet_surf = pygame.Surface((300,50), flags=pygame.SRCALPHA)
        key = pygame.image.load('./graphics/bullet/tile004.png')
        pygame.Surface.blit(bullet_surf, key, (0,0))
        text = f' : {player.bulletcount}'
        font = pygame.font.Font('Pixeltype.ttf', 32)
        text = font.render(text, True, 'black')
        bullet_surf.blit(text, (30, 10))
        pygame.Surface.blit(self.display_surface, bullet_surf, (450,10))

        score_surf = pygame.Surface((300,50), flags=pygame.SRCALPHA)
        text = f'Score : {int(self.score)}'
        font = pygame.font.Font('Pixeltype.ttf', 32)
        text = font.render(text, True, 'black')
        score_surf.blit(text, (0, 10))
        pygame.Surface.blit(self.display_surface, score_surf, (250,10))
        
        

        self.collisions()

        self.handle_bullets()
        self.bullets.update()
        self.bullets.draw(self.display_surface)

        self.bulletpacks.draw(self.display_surface)
        if not player.dead:
            self.bulletpacks.update(12+1*(self.phase))

        self.player.update()
        self.player.draw(self.display_surface)

        self.handle_mushmen()
        if not player.dead:
            self.mushes.update(12+1*(self.phase))
        self.mushes.draw(self.display_surface)

        self.handle_obelisks()
        if not player.dead:
            self.obelisks.update(4+1*(self.phase))
        self.obelisks.draw(self.display_surface)

        if player.dead and player.frame_index==7:
            self.gameover=True


        



        

        

