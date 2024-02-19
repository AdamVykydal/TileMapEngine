import pygame 
from Renderer import Renderer
from TileMap import TileMap
from Coords import Coords
from HandleEvents import HandleEvents
from loadTextures import LoadTextures
from MapUpdate import MapUpdate
from MapTerrein import MapTerrein
import copy



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.mapWidt = 100
        self.mapHeight = 100
        self.startPoint = Coords(0, 0)
        self.textures = LoadTextures.run()
        #self.tileMapTerrein = TileMap(self.textures, self.mapWidt, self.mapHeight)
        #self.tileMapObjects = TileMap(self.textures, self.mapWidt, self.mapHeight)
        self.mapTerrein = MapTerrein(self.textures, self.mapWidt, self.mapHeight)
        print(self.mapTerrein.surface)
        self.clock = pygame.time.Clock()
        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.handleEvents = HandleEvents(self.screenWidth, self.screenHeight, self.mapWidt, self.mapHeight)
        #self.mapUpdate = MapUpdate(self.textures)
        self.renderer = Renderer(copy.deepcopy(self.startPoint))
        
        print(self.textures)
        
    def run(self):

        while True:
            self.clock.tick()
            mousePosX, mousePosY = pygame.mouse.get_pos()
            self.startPoint = self.handleEvents.cameraMouseMove(mousePosX, mousePosY, self.startPoint)
            self.scale, self.startPoint, mousePressed = self.handleEvents.check(self.startPoint)
            self.screen.fill((0, 0, 0))
            self.renderer.renderScaleMap(self.screen, self.mapTerrein.surface, self.scale, self.startPoint)
            
            #self.mapUpdate.manageChuncks(self.screen, self.tileMapTerrein.chunks, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #print(sys.getsizeof(self.tileMapTerrein.chunks))
            #self.screen.blit(self.tileMapTerrein.chunks[0][0].surface, (50,50)) 
            #print(self.startPoint.x, self.startPoint.y)
            #self.renderer.renderChunks(self. screen, self.tileMapTerrein.chunks, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #self.renderer.renderTerrein(self. screen, self.tileMapTerrein.tiles, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            #self.renderer.renderObjects(self. screen, self.tileMapObjects.tiles, self.scale, copy.deepcopy(self.startPoint), mousePressed, (mousePosX,mousePosY))
            
            pygame.display.update()
            print(self.clock.get_fps())