import pygame
from Coords import Coords

class HandleEvents():
    def __init__(self, screenWidt, screenHeight, mapWidt, mapHeight):
        self.mapWidt = mapWidt
        self.mapHeight = mapHeight
        self.screenWidth = screenWidt
        self.screenHeight = screenHeight
        self.margin = 20
        self.moveY = 0
        self.moveX = 0
        self.cameraMoveSpeed = 10
        self.scale =  160
        self.startPoint = Coords(0, 0)
        self.mousePressed = False
    
    def check(self):
        
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEWHEEL:
                
                self.scale += event.y *2
                if self.scale <= 101:
                    self.scale = 100
                elif self.scale >= 301:
                    self.scale = 300
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mousePressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mousePressed = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.moveY = self.cameraMoveSpeed
                if event.key == pygame.K_DOWN:
                    self.moveY = -self.cameraMoveSpeed
                if event.key == pygame.K_LEFT:
                    self.moveX = self.cameraMoveSpeed
                if event.key == pygame.K_RIGHT:
                    self. moveX = -self.cameraMoveSpeed
            
            if event.type == pygame.KEYUP:
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
        print(self.startPoint.x, self.startPoint.y)
        
        
        if self.startPoint.x > 0:
            self.startPoint.x = 0
        
        if self.startPoint.y > 0:
            self.startPoint.y = 0
        
        if self.startPoint.x < -(self.scale/5 * self.mapWidt) - 1920:
            self.startPoint.x = -(self.scale/5 * self.mapWidt) - 1920
        
        if self.startPoint.y < -(self.scale/5 * self.mapHeight) - 1080:
            self.startPoint.y = -(self.scale/5 * self.mapHeight) - 1080 
       
        print(-(self.scale) - 1920, -(self.scale) - 1080)
        print("-----------------------")
        
        return self.scale, self.startPoint, self.mousePressed
    
    def cameraMouseMove(self, mousePosX, mousePosY):
        if mousePosX < self.margin:
            self.startPoint.x += self.cameraMoveSpeed
        if mousePosX > self.screenWidth - self.margin:
            self.startPoint.x += -self.cameraMoveSpeed     
        if mousePosY < self.margin:
            self.startPoint.y += self.cameraMoveSpeed
        if mousePosY > self.screenHeight - self.margin:
            self.startPoint.y += -self.cameraMoveSpeed
        
        return self.startPoint
        