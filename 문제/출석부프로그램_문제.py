state = True    # 프로그램 상태 : True면 실행중, False면 종료

mode = 0

grade = []  # 학년
name = []   # 이름
number = [] # 학번
major = []  # 전공
check = []  # 출석

# 구분선 함수
def line() : 
    print("-" * 55)

# 전체 학생 목록 출력 함수
def printAllStudents(type) : 
    cnt = len(name)
    print(type + ' 학생 목록')
    line()
    print("출결".center(3),"이름".center(3),"학년".center(3),"학번".center(4),"전공".center(7))
    line()

    for i in range(0,cnt) : 
        if type=="전체" : 
            print(check[i].center(3),name[i].rjust(3),grade[i].rjust(2),number[i].center(10),major[i].ljust(14))
        elif type == check[i] : 
            print(check[i].center(3),name[i].rjust(3),grade[i].rjust(2),number[i].center(10),major[i].ljust(14))

    line()
    print()

while state :
    print("\n------------------출석부 관리 프로그램-----------------")
    print()
    print("     1. 학생 등록")
    print("     2. 전체 학생 목록 출력")
    print("     3. 출석 체크")
    print("     4. 출석 변경")
    print("     5. 출석 목록 출력")
    print("     6. 지각 목록 출력")
    print("     7. 결석 목록 출력")
    print("     8. 종료")
    print()
    line()

    mode = int(input("항목을 숫자로 입력해주세요 : "))
    print()

    # 학생 등록 기능
    if mode == 1 :
        line()
        print("학생 등록을 시작합니다.")
        line()

        # 작성

























    # 전체 학생 목록 출력 기능
    elif mode == 2 :
        

    # 출석 체크 기능
    elif mode == 3 :

        line()
        print('출석을 진행합니다. 숫자를 입력하여 출결 상태를 입력해주세요')
        print("1 : 출석 | 2 : 지각 | 3 : 결석")
        line()

        # 작성










    # 출석 변경 기능
    elif mode == 4 :

        # 작성































    # 출석 학생 목록 출력 기능
    elif mode == 5 :
        # 작성        

    # 지각 학생 목록 출력 기능
    elif mode == 6 :
        # 작성        

    # 결석 학생 목록 출력 기능
    elif mode == 7 :
        # 작성        

    # 프로그램 종료
    elif mode == 8 :
        print("프로그램을 종료합니다.")
        state = False
    
    # 입력 오류
    else : 
        print("번호를 다시 입력해주세요")