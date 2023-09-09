import pygame
from pygame.locals import *

# pygame 실행
def main():

    # pygame 초기화
    pygame.init()

    # 화면 크기 설정
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 화면 타이틀 설정
    pygame.display.set_caption("SpacebarGame")

    # FPS 설정
    FPS = 60
    clock = pygame.time.Clock()

    # 사용자 게임 초기화
    background = pygame.image.load("C:\\Users\\samsung_\\Desktop\\GameProject\\SpacebarGame\\game\\image\\background.png")
    # startButton = pygame.image.load("C:\\Users\\samsung_\\Desktop\\GameProject\\SpacebarGame\\game\\image\\startButton.png")
    
    dt = clock.tick(FPS)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 그리기
        screen.blit(background, (0, 0))

        pygame.display.update()

    # pygame 종료
    pygame.quit()

if __name__ == "__main__":
    main()