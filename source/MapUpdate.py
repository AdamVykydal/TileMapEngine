import copy 
import pygame
from Renderer import Renderer

class MapUpdate:
    def __init__(self, textures):
        self.renderer = Renderer() 
        self.textures = textures
   
    def manageChuncks(self, screen, mapChunks, scale, startPointCoords, mousePressed, mousePos):
        self.startPointCoords = copy.deepcopy(startPointCoords)
    
        for y, row in enumerate(mapChunks):
            self.startPointCoords.x = copy.deepcopy(startPointCoords.x)
            
            for x,chunk in enumerate(row):
                if self.startPointCoords.y >= -scale and self.startPointCoords.y <= 1080 and self.startPointCoords.x >= -scale and self.startPointCoords.x <= 1920:
                    
                    rect = self.renderer.renderChunks(screen, scale, chunk.surface, self.startPointCoords) 
                    
                    if mousePressed:
                        if rect.collidepoint(mousePos):
                            a = scale / 5
                            for tileY, tileRow in enumerate(chunk.tiles):
                                for tileX, tile in enumerate(tileRow):
                                    
                                    if pygame.Rect((self.startPointCoords.x + tileX * a,self.startPointCoords.y + tileY * a), (a,a)).collidepoint(mousePos):
                                        chunk.tiles[tileY][tileX] = 1
                                        chunk.update(self.textures)
                                        break

                
                
                self.startPointCoords.x += scale 
            
            self.startPointCoords.y += scale