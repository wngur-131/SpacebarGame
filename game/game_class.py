import pygame

class Button:
    def __init__(self):
        self.image = pygame.image.load("./game/image/button.png")
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def setButtonPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def ifClickButton(self, mouseXpos, mouseYpos):
        if mouseXpos >= self.xPos and mouseXpos <= self.xPos + self.width:
            if mouseYpos >= self.yPos and mouseYpos <= self.yPos + self.height:
                return True

class Background:
    def __init__(self):
        self.image = pygame.image.load("./game/image/background.png")
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]