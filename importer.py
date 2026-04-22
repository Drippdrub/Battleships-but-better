import pygame
from os.path import join
from os import walk, scandir
from utils import resource_path
from constants import RESOURCE_DIR

# code taken from Atlas's video "Efficient imports in pygame", edited for new functionality
# https://www.youtube.com/watch?v=fFTV6FLPbZo
def import_image(*path, alpha=True, format='png'):
    rel_path = join(*path) + f'.{format}'
    full_path = resource_path(rel_path)
    surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
    print(f"Imported image '{full_path}'")
    return surf

def import_image_folder(*path):
    frames = []
    for folder_path, sub_folders, images in walk(join(*path)):
        for image in sorted(images, key = lambda name: int(name.split('.')[0])):
            full_path = resource_path(join(folder_path, image))
            surf = pygame.image.load(full_path).convert_alpha()
            frames.append(surf)
    return frames

def import_image_folder_dict(*path):
    frames = {}
    for folder_path, sub_folders, images in walk(join(*path)):
        for image in images:
            full_path = resource_path(join(folder_path, image))
            surf = pygame.image.load(full_path).convert_alpha()
            frames[image.split('.')[0]] = surf
    return frames

def import_image_sub_folders(*path):
    frames = {}
    base_path = join(*path)

    def recurse(current_path, current_key):
        entries = sorted(scandir(current_path), key=lambda e: e.name)
        image_files = [e for e in entries if e.is_file() and e.name.endswith('.png')]
        sub_dirs = [e for e in entries if e.is_dir()]

        if image_files:
            frames[current_key] = [
                pygame.image.load(resource_path(e.path)).convert_alpha()
                for e in sorted(image_files, key=lambda e: int(e.name.split('.')[0]))
            ]

        for sub_dir in sub_dirs:
            next_key = f"{current_key}/{sub_dir.name}" if current_key else sub_dir.name
            recurse(sub_dir.path, next_key)

    for _, sub_folders, __ in walk(base_path):
        for sub_folder in sub_folders:
            recurse(join(base_path, sub_folder), sub_folder)
        break  # only iterate top-level here; recursion handles the rest

    return frames