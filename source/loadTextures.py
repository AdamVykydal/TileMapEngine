import os
import pygame

class LoadTextures:

    def run():
        image_directory = "recources\\img"
        pygame.init()
        images = {}

        for filename in os.listdir(image_directory):
            
            if filename.endswith('.png'):
                # Načtení obrázku a přidání do seznamu
                image_path = os.path.join(image_directory, filename)
                image = pygame.image.load(image_path)
                images[filename.replace(".png","")] = image
                print(images)

LoadTextures.run()
        

