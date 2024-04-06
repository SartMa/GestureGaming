from os import walk
import pygame
def import_folder(path):
    surface_list=[]
    for _,__,img_files in walk(path):
        img_files.sort()
        for img in img_files:
            full_path = path+'/'+img
            img_surf=pygame.image.load(full_path).convert_alpha()
            img_surf=pygame.transform.scale(img_surf, (48*1.5, 48*1.5))
            surface_list.append(img_surf)
    return surface_list
    

#import_folder('/home/siddharth-kini/PythonCode/Practice/graphics/idle')

