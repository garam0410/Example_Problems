# 좀비가 되어 사람을 잡으면 승리하는 게임입니다.
# 중심에는 좀비, 오른쪽 아래에는 사람이 있다고 가정할 때, 사람을 잡으로 한칸 이동할때마다 1점이 추가됩니다.
# 좀비와 사람 모두 한칸씩 움직이지만, 사람이 다음에 움직일 칸은 예측할 수 없습니다.
# 점수가 낮을 수록 높은 순위를 가집니다.
# 크기는 5X10

import random

state = True
gameState = False

userId = []
userScore = []

# 메인 화면
def mainPage() :
    print("\n","-"*54)
    
    for i in range(2) : 
        print("│"," "*52,"│")
        
    print("│"," "*20,"좀비  게임"," "*20,"│")
    
    
    for i in range(2) : 
        print("│"," "*52,"│")
    
    print("","-"*54,"")

# 점선
def line() : 
    print("-" * 55)

# 알림 메시지
def dialog(msg) : 
    print()
    line()
    print(msg)
    line()
    print()

# 경기장
def showBoard(userX, userY, zombieX, zombieY) : 
    
    print("#"*12)
    for i in range(0,5) : 
        tmp = "#"
        for j in range(0,10) : 
            
            if userX == i and userY == j : 
                tmp += "●"
            elif zombieX == i and zombieY == j : 
                tmp += "Z"
            else : 
                tmp += " "
        print(tmp + "#")
    
    print("#"*12)

while state : 
    mainPage()
    
    print()
    print("     1. 게임 시작")
    print("     2. 역대 순위")
    print("     3. 종료")
    print()
    line()
    
    mode = int(input("항목을 숫자로 입력해주세요 : "))
    print()
    
    if mode == 1 : 
        dialog("사용자명을 입력해 주세요")
        inputId = input("사용자명 : ")
        
        dialog("게임을 시작합니다.\n\n사람 : ● | 좀비 : Z")
        
        zombieX = 1
        zombieY = 3
        userX = 3
        userY = 7
        
        score = -1
        
        while userX != zombieX or userY != zombieY : 
            score += 1
            showBoard(userX, userY, zombieX, zombieY)
            
            zombieDirection = input("Up : U | Down : D | Left : L | Right : R  => ")
            userDirection = random.randrange(0,4)
            
            if zombieDirection == "U" and zombieX - 1 >= 0: 
                zombieX -= 1
            elif zombieDirection == "D" and zombieX + 1 <=4: 
                zombieX += 1
            elif zombieDirection == "L" and zombieY -1 >= 0 : 
                zombieY -= 1
            elif zombieDirection == "R" and zombieY + 1 <= 8: 
                zombieY += 1
            else : 
                dialog("이동하려는 위치가 벽이거나 잘못 입력하였습니다. 다시 입력하세요.")
                continue
            while True : 
                if userDirection == 0 and userX -1 >= 0 : 
                    userX -= 1
                    break
                elif userDirection == 1 and userX +1 <= 4 : 
                    userX += 1
                    break
                elif userDirection == 2 and userY -1 >= 0 : 
                    userY -= 1
                    break
                elif userDirection == 3 and userY +1 <= 8 : 
                    userY += 1
                    break
                else : 
                    userDirection = random.randrange(0,4)
                    continue

        dialog("사람을 잡았습니다.... 점수는 " + str(score) + "점 입니다.")
        userId.append(inputId)
        userScore.append(score)
        
    elif mode == 2 : 
        dialog("기록")
        
        print("score    userId")
        print("---------------")
        for i in range(0,len(userId)) : 
            print(str(userScore[i]).center(5) + "  " + userId[i])
    
    elif mode == 3 : 
        dialog("게임을 종료합니다")
        state = False