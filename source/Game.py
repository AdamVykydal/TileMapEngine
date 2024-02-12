import pygame 
from Renderer import Renderer
from TileMap import TileMap
from Coords import Coords
import copy

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.renderer = Renderer()
        self.mapWidt = 300
        self.mapHeight = 300
        self.tileMap = TileMap(self.mapWidt, self.mapHeight)
        self.scale = 32
        self.startPoint = Coords(-500,-500)
        self.clock = pygame.time.Clock()
        #self.screenWidth, self.screenHeight = self.screen.get_size()
        self.moveY = 0
        self.moveX = 0
        self.margin = 20
        self.cameraMoveSpeed = 100
   
    def run(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.renderer.render(self. screen, self.tileMap.tiles, self.scale, copy.deepcopy(self.startPoint))
            print(self.startPoint.x, self.startPoint.y)
            pygame.display.update()
            events = pygame.event.get()
            
            mousePosX, mousePosY = pygame.mouse.get_pos()
            
            
            if mousePosX < self.margin:
               self.startPoint.x += self.cameraMoveSpeed
            if mousePosY < self.margin:
                self.startPoint.y += self.cameraMoveSpeed
            if mousePosX > 1920 - self.margin:
                self.startPoint.x += -self.cameraMoveSpeed
            if mousePosY > 1080 - self.margin:
                self.startPoint.y += -self.cameraMoveSpeed
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEWHEEL:
                    
                    self.scale += event.y
                    print(self.scale)
                    if self.scale <= 10:
                        self.scale = 11
                    elif self.scale >= 140:
                        self.scale = 139
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.moveY = self.cameraMoveSpeed
                    if event.key == pygame.K_DOWN:
                        self.moveY = -self.cameraMoveSpeed
                    if event.key == pygame.K_LEFT:
                        self.moveX = self.cameraMoveSpeed
                    if event.key == pygame.K_RIGHT:
                       self. moveX = -self.cameraMoveSpeed
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.moveY = 0
                    if event.key == pygame.K_DOWN:
                        self.moveY = 0
                    if event.key == pygame.K_LEFT:
                        self.moveX = 0
                    if event.key == pygame.K_RIGHT:
                        self.moveX = 0
                    
            self.startPoint.x += self.moveX
            self.startPoint.y += self.moveY
            
            if self.startPoint.x > 0:
                self.startPoint.x = 0
            
            if self.startPoint.y > 0:
                self.startPoint.y = 0
            
            if self.startPoint.x < -((self.scale*self.mapWidt) -1920):
                self.startPoint.x = -((self.scale*self.mapWidt) -1920)
            
            if self.startPoint.y < -((self.scale*self.mapHeight) -1080):
                self.startPoint.y = -((self.scale*self.mapHeight) -1080)
