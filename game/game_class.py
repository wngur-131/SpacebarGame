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
                    score int(10) DEFAULT 0,
                    date varchar(14)
                    )"""
            )
            self.db.commit()

        except:
            return False
        
        else:
            return True
        
    def insertData(self, data):
        self.cursor.execute(
            f"""INSERT INTO spacebargame_info (
                (class, name, score, date) VALUES {data}
                )

        """)
        self.db.commit()

    def getData(self):
        try:
            self.cursor.execute("SELECT * FROM spacebargame_info")
            self.data = self.cursor.fetchall()
        except:
            return False
        else:
            return True     

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