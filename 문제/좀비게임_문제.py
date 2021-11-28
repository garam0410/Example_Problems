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
            # 구현
            
            
            
            if :
                
            elif :
                
            elif :
                
            elif :
                
            else : 
                dialog("이동하려는 위치가 벽이거나 잘못 입력하였습니다. 다시 입력하세요.")
                continue
            while True : 
                if :
                    
                    
                elif :
                    
                    
                elif :
                    
                    
                elif :
                    
                    
                else : 
                    
                    

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