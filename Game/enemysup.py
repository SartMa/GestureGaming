from os import walk
import pygame
def import_folder(path):
    surface_list=[]
    for _,__,img_files in walk(path):
        img_files.sort()
        img_files.sort()
        for img in img_files:
            full_path = path+'/'+img
            img_surf=pygame.image.load(full_path).convert_alpha()
            if(path=='./graphics/mushroom/run' or path=='./graphics/mushroom/death'):
                img_surf=pygame.transform.flip(img_surf, True, False)
                img_surf=pygame.transform.scale(img_surf, (150*1.4, 150*1.4))
            surface_list.append(img_surf)
    return surface_list

