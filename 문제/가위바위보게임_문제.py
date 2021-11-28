import random

state = True

mode = 0

block = 10 # 블록 수
steps = 1  # 가위바위보 승리 시, 전진하는 칸 수

comResult = []  # 컴퓨터 승패
userResult = [] # 사용자 승패

# 메인 화면
def mainPage() :
    print("\n","-"*54)
    
    for i in range(2) : 
        print("│"," "*52,"│")
        
    print("│"," "*15,"블록 가위바위보 게임"," "*15,"│")
    
    
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

def showResult(comIdx, userIdx) : 
    comLocation = ""
    userLocation = ""
    
    for i in range(0,block) : 
        if comIdx == i : 
            comLocation += "▼ "
        else : 
            comLocation += "  "
        
        if userIdx == i : 
            userLocation += "▼ "
        else : 
            userLocation += "  "
    
    print("       "+comLocation)
    print(" Com : " + "* "*block)
    
    print("       "+userLocation)
    print("User : " + "* "*block)

while state : 
    
    mainPage()
    
    print()
    print("     1. 게임 시작")
    print("     2. 환경 설정")
    print("     3. 게임 기록")
    print("     4. 종료")
    print()
    line()
    
    mode = int(input("항목을 숫자로 입력해주세요 : "))
    print()
    
    if mode == 1 : 
        dialog("게임을 시작합니다")
        
        comIdx = 0      # 컴퓨터 층
        userIdx = 0     # 사용자 층
        
        while comIdx < block-1 and userIdx < block-1 : 
            showResult(comIdx, userIdx)
            
            line()
            print()
            
            user = int(input("가위 : 1 | 바위 : 2 | 보 : 3  => "))
            
            if user != 1 and user != 2 and user != 3 : 
                dialog("다시 입력해 주세요")
                continue
            
            #구현
            
            if :
            
            
            
            elif :
            
            
            
            elif :
            
            
            
            elif :
            
            
            
            elif :
            
        
        if :
        
        
        
        
        
        elif :
        
        
        
        
        
        
    elif mode == 2 : 
        dialog("환경설정을 진행합니다")
        
        inputBlock = int(input("게임을 진행할 최대 블록 수(5층 이상, 현재 "+ str(block) + "개로 설정 됨) : "))
        inputSteps = int(input("가위바위보를 승리하였을 때, 전진할 블록 수를 설정해주세요(현재 " + str(steps) + " 블록으로 설정 됨) : "))
        
        #구현
        
        
        
        
        
        
        
        
        
        dialog("환경설정이 저장되었습니다")         
        
    elif mode == 3 : 
        dialog("게임 기록")
        
        print("  Com  vs  User")
        print("  -------------")
        
        for i in range(0, len(userResult)) : 
            print(i+1,comResult[i] + "     " + userResult[i])
        
    elif mode == 4 : 
        state = False
        dialog("게임을 종료합니다")
    
    else : 
        dialog("번호를 다시 입력해 주세요.")