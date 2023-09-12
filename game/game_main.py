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
    
    # 데이터베이스 설정
    db = Database()

    # FPS 설정
    FPS = 60
    clock = pygame.time.Clock()

    # 배경화면 설정
    background = Background()
    
    # 버튼 설정
    exitButton = Button()
    EXITBUTTON_X_POS = SCREEN_WIDTH - exitButton.width - 48
    EXITBUTTON_Y_POS = 48
    exitButton.setButtonPosition(EXITBUTTON_X_POS, EXITBUTTON_Y_POS)
    
    startButton = Button()
    STARTBUTTON_X_POS = 360
    STARTBUTTON_Y_POS = SCREEN_HEIGHT - 300
    startButton.setButtonPosition(STARTBUTTON_X_POS, STARTBUTTON_Y_POS)

    rankButton = Button()
    RANKBUTTON_X_POS = SCREEN_WIDTH - rankButton.width - 360
    RANKBUTTON_Y_POS = SCREEN_HEIGHT - 300
    rankButton.setButtonPosition(RANKBUTTON_X_POS, RANKBUTTON_Y_POS)

    undoButton = Button()
    UNDOBUTTON_X_POS = SCREEN_WIDTH / 2 - undoButton.width / 2
    UNDOBUTTON_Y_POS = SCREEN_HEIGHT - 300
    undoButton.setButtonPosition(UNDOBUTTON_X_POS, UNDOBUTTON_Y_POS)

    

    scene = 1 # 1: 시작, 2: 게임, 3: 게임종료, 4: 순위

    # 시작 시간 설정
    startTicks = pygame.time.get_ticks()
    
    # 게임 변수 초기화
    totalTime = 20
    score = 0

    running = True
    initScene = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass

            # 클릭 이벤트 처리
            if event.type == pygame.MOUSEBUTTONUP:
                MOUSEPOS = pygame.mouse.get_pos()

                # 종료 버튼 클릭 이벤트 처리
                if exitButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                    running = False
                    
                # 시작 화면 클릭 이벤트 처리
                if scene == 1:
                    if startButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 2
                        initScene = True
                    elif rankButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 4
                        initScene = True

                # 게임 화면 클릭 이벤트 처리
                elif scene == 2:
                    if undoButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 1
                        initScene = True

                # 종료 화면 클릭 이벤트 처리
                elif scene == 3:
                    if undoButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 2
                        initScene = True
                    elif rankButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 4
                        initScene = True

                # 순위 화면 클릭 이벤트 처리
                elif scene == 4:
                    if undoButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
                        scene = 1
                        initScene = True
                        
        # 그리기
        screen.blit(background.image, (0, 0))

        # 시작 화면 구성
        if scene == 1:
            # 첫 화면 초기화
            if initScene:
                initScene = False

            screen.blit(startButton.image, (startButton.xPos, startButton.yPos))
            screen.blit(rankButton.image, (rankButton.xPos, rankButton.yPos))

        # 게임 화면 구성
        elif scene == 2:
            if initScene:
                score = 0
                startTicks = pygame.time.get_ticks() # 시작 시간 설정
                initScene = False
                
            # 경과 시간 설정
            elapsedTime = (pygame.time.get_ticks() - startTicks) / 1000
            
            if elapsedTime >= 20:
                scene++
                initScene = True
                
                
            else:
                pass
                
            
                
        elif scene == 3:
            if initScene:
                pass

        else:
            pass

        pygame.display.update()

    # pygame 종료
    pygame.quit()

if __name__ == "__main__":
    main()