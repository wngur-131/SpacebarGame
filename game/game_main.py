import pygame
from game_class import *

# pygame 실행
def main(info):

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
    db.createTable()
    
    dbError = True
    
    dbTotal = 0
    dbRank = 0

    # FPS 설정
    FPS = 60
    clock = pygame.time.Clock()

    # 배경화면 설정
    background = Background(False)
    backgroundText = Background(True)
    
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

    # 컬러 설정
    WHITE = (255, 255, 255)
    BLACK = (25, 25, 25)
    RED = (255, 49, 32)

    # 텍스트 설정
    timerText = Text(36, WHITE)
    scoreText = Text(96, WHITE)

    resultText = Text(96, WHITE)
    rankText = Text(36, WHITE)
    
    
    # 씬 설정
    scene = 1 # 1: 시작, 2: 게임, 3: 게임종료, 4: 순위

    # 시작 시간 설정
    startTicks = pygame.time.get_ticks()
    
    # 게임 변수 초기화
    TOTAL_TIME = 20
    score = 0

    running = True
    initScene = True
    while running:
        dt = clock.tick(FPS)

        # 이벤트 처리
        for event in pygame.event.get():
            # pygame 종료
            if event.type == pygame.QUIT:
                running = False

            # 키보드 이벤트 처리
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if scene == 2:
                        score += 1

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
                    if startButton.ifClickButton(MOUSEPOS[0], MOUSEPOS[1]):
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

        # 시작 화면 구성
        if scene == 1:
            # 첫 화면 초기화
            if initScene:
                initScene = False

            # 그리기
            screen.blit(backgroundText.image, (0, 0))
            screen.blit(startButton.image, (startButton.xPos, startButton.yPos))
            screen.blit(rankButton.image, (rankButton.xPos, rankButton.yPos))

        # 게임 화면 구성
        elif scene == 2:
            if initScene:
                score = 0
                startTicks = pygame.time.get_ticks() # 시작 시간 설정
                initScene = False
                
            # 남은 시간 설정
            leftTime = TOTAL_TIME - (pygame.time.get_ticks() - startTicks) / 1000
            
            if leftTime <= 0:
                scene += 1
                initScene = True
                
                
            else:
                screen.blit(background.image, (0, 0))
                screen.blit(undoButton.image, (undoButton.xPos, undoButton.yPos))

                # 텍스트 랜더링
                timerRender = timerText.font.render(f"남은 시간 : {str(int(leftTime) + 1)}초", None, timerText.color)
                timerText.width = timerRender.get_rect().size[0]
                timerText.height = timerRender.get_rect().size[1]
                timerText.setTextPosition(SCREEN_WIDTH / 2 - timerText.width / 2, undoButton.yPos - 64 - timerText.height)
                screen.blit(timerRender, (timerText.xPos, timerText.yPos))

                scoreRender = scoreText.font.render(f"점수 : {str(score)}점", None, scoreText.color)
                scoreText.width = scoreRender.get_rect().size[0]
                scoreText.height = scoreRender.get_rect().size[1]
                scoreText.setTextPosition(SCREEN_WIDTH / 2 - scoreText.width / 2, timerText.yPos - 24 - scoreText.height)
                screen.blit(scoreRender, (scoreText.xPos, scoreText.yPos))
                
        elif scene == 3:
            # 그리기
            screen.blit(background.image, (0, 0))
            screen.blit(startButton.image, (startButton.xPos, startButton.yPos))
            screen.blit(rankButton.image, (rankButton.xPos, rankButton.yPos))

            if initScene:
                # 데이터 삽입, 불러오기
                if db.insertData((info[0], info[1], score)) and db.getData():
                    dbError = False

                    dbTotal = len(db.data)
                    dbRank = db.rankScore(score)

                # 데이터베이스 오류
                else:
                    dbError = True
                
                initScene = False

            # 텍스트 랜더링
            if dbError:
                rankRender = rankText.font.render("데이터베이스 오류로 인해 데이터 수신에 실패했어요", None, rankText.color)
                rankText.width = rankRender.get_rect().size[0]
                rankText.height = rankRender.get_rect().size[1]
                rankText.setTextPosition(SCREEN_WIDTH / 2 - rankText.width / 2, rankButton.yPos - 64 - rankText.height)
                screen.blit(rankRender, (rankText.xPos, rankText.yPos))
                
            else:
                rankRender = rankText.font.render(f"전체 {dbTotal}명 중 {dbRank}위를 기록했어요", None, rankText.color)
                rankText.width = rankRender.get_rect().size[0]
                rankText.height = rankRender.get_rect().size[1]
                rankText.setTextPosition(SCREEN_WIDTH / 2 - rankText.width / 2, rankButton.yPos - 64 - rankText.height)
                screen.blit(rankRender, (rankText.xPos, rankText.yPos))

            resultRender = resultText.font.render(f"최종 점수 : {score}점", None, resultText.color)
            resultText.width = resultRender.get_rect().size[0]
            resultText.height = resultRender.get_rect().size[1]
            resultText.setTextPosition(SCREEN_WIDTH / 2 - resultText.width / 2, rankText.yPos - 24 - resultText.height)
            screen.blit(resultRender, (resultText.xPos, resultText.yPos))
        
        else:
            # 그리기
            screen.blit(background.image , (0, 0))
            screen.blit(undoButton.image, (undoButton.xPos, undoButton.yPos))

            if initScene:
                if db.getData():
                    rankTotal = len(db.data)
                    
                    rankData = []
                    for data in db.data:
                        pass


        
        pygame.display.update()

    # pygame 종료
    pygame.quit()

    # 데이터베이스 종료
    db.db.close()

if __name__ == "__main__":
    main(("10309", "문주혁"))