import pygame
import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = "code.wngur131",
            db = "info",
            charset = "utf8mb4"
        )
        self.cursor = self.db.cursor()

    def createTable(self):
        try:
            self.cursor.execute(
                """CREATE TABLE spacebargame_info (
                    id int(10) AUTO_INCREMENT PRIMARY KEY,
                    class varchar(5),
                    name varchar(10),
                    score int(10) DEFAULT 0
                    )"""
            )
            self.db.commit()

        except:
            pass
        
    def insertData(self, data):
        try:
            SQL = "INSERT INTO spacebargame_info (class, name, score) VALUES (%s, %s, %s)"
            self.cursor.execute(SQL, data)
            self.db.commit()
        except:
             return False
        else:
            return True


    def getData(self):
        try:
            self.cursor.execute("SELECT * FROM spacebargame_info")
            self.data = self.cursor.fetchall()
        except:
            return False
        else:
            return True     
        
    def deleteTable(self):
        try:
            self.cursor.execute("DELETE TABLE spacebargame_info")
        except:
            pass
            
    def rankScore(self, score):
        rank = 1
        for data in self.data:
            if score < int(data[3]):
                rank += 1
                
        return rank


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
            
class Text:
    def __init__(self, size, color):
        self.size = size
        self.font = pygame.font.Font("./game/font/NotoSansKR-Black.otf", size)
        self.color = color
        self.width = 0
        self.height = 0

    def setTextPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos


class Background:
    def __init__(self, ifText):
        if ifText:
            self.image = pygame.image.load("./game/image/backgroundText.png")
        else:
            self.image = pygame.image.load("./game/image/background.png")
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]