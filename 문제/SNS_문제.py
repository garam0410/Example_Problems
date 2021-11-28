snsState = True # SNS 프로그램 상태
loginState = False # 로그인 상태

mode = 0

userId = ["test"]     # 아이디 저장
userPw = ["1234"]     # 비밀번호 저장
loginId = ""          # 로그인된 아이디

title = ["안녕하세요."]      # 글 제목
writer = ["test"]           # 글쓴 사람
text = ["반갑습니다."]       # 글 내용

# 메인 화면
def mainPage() :
    print("\n","-"*54)
    
    for i in range(2) : 
        print("│"," "*52,"│")
        
    print("│"," "*16,"WKU Social Service"," "*16,"│")
    
    
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

# 게시글 모듈
def script(scriptIdx, inputTitle, inputWriter, inputText) : 
    print("NO."+str(scriptIdx))
    line()
    print("제목 : " + inputTitle)
    print("작성자 : " + inputWriter + "\n")
    print("내용 : ")
    print(inputText)
    line()
    print()

# 프로그램 시작
while snsState : 
    
    mainPage()
    
    print()
    print("     1. 로그인")
    print("     2. 회원가입")
    print("     3. 종료")
    print()
    line()

    mode = int(input("항목을 숫자로 입력해주세요 : "))
    print()
    
    # 로그인 기능
    if mode == 1 : 
        dialog("로그인을 진행합니다\n 아이디와 비밀번호를 입력해 주세요.")
        
        inputId = input("아이디 : ")
        inputPw = input("비밀번호 : ")










    
    # 회원가입 기능
    elif mode == 2 : 
        dialog("회원가입을 진행합니다\n아이디와 비밀 번호를 입력해 주세요.")
        
        inputId = input("아이디 : ")
        inputPw = input("비밀번호 : ")










    
         
    # 프로그램 종료       
    elif mode == 3 : 
        print("프로그램을 종료합니다.")
        snsState = False
    
    # 입력 오류
    else : 
        print("번호를 다시 입력해주세요")
    
    # 로그인 성공 후,
    while loginState : 
        
        dialog(loginId+"님 환영합니다.")
        print("     1. 전체 게시글")
        print("     2. 글쓰기")
        print("     3. 로그아웃")
        print()
        line()
        
        mode = int(input("항목을 숫자로 입력해주세요 : "))
        print()
        
        if mode == 1 : 
            
            
            
        
        elif mode == 2 : 
            dialog("게시글 등록을 시작합니다")
            
            inputTitle = input("제목 : ")
            inputText = input("내용 : ")
            
            
            
            
            
            
            
        
        elif mode == 3 : 
            dialog("정상적으로 로그아웃 되었습니다")
            loginState = False