import pygame
from game_class import *

# pygame 실행
def main():

    # pygame 초기화
    pygame.init()

    # 화면 크기 설정
    SCREEN_WIDTH = 1536
    SCREEN_HEIGHT = 864
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 화면 타이틀 설정
    pygame.display.set_caption("SpacebarGame")

    # FPS 설정
    FPS = 60
    clock = pygame.time.Clock()

    # 배경화면 설정
    background = Background()
    
    # 버튼 설정
    startButton = Button()
    STARTBUTTON_X_POS = 360
    STARTBUTTON_Y_POS = background.height - 300
    startButton.setButtonPosition(STARTBUTTON_X_POS, STARTBUTTON_Y_POS)

    rankButton = Button()
    RANKBUTTON_X_POS = SCREEN_WIDTH - rankButton.width - 360
    RANKBUTTON_Y_POS = background.height - 300
    rankButton.setButtonPosition(RANKBUTTON_X_POS, RANKBUTTON_Y_POS)

    scene = 1 # 1: 시작, 2: 게임, 3: 게임종료, 4: 순위

    # 시작 시간 설정
    startTicks = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass

            if event.type == pygame.MOUSEBUTTONUP:
                MOUSEPOS = pygame.mouse.get_pos()
                if startButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                    running = False
                if scene == 1:
                    pass
        # 그리기
        screen.blit(background.image, (0, 0))
        screen.blit(startButton.image, (startButton.xPos, startButton.yPos))
        screen.blit(rankButton.image, (rankButton.xPos, rankButton.yPos))

        pygame.display.update()

    # pygame 종료
    pygame.quit()

if __name__ == "__main__":
    main()