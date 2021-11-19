# 매일 반복된 출석부 인쇄로 종이가 부족해 다른 대안의 필요성을 느끼게 되었다.
# 그래서 아래 요구사항에 맞는 프로그램을 개발하려고한다.

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

        studentGrade = 0
        studentName = ""
        studentNumber = 0
        studentMajor = ""

        for i in range(0,4) : 
            if i == 0 : 
                studentName = input("이름을 입력하세요 : ")
            elif i == 1 : 
                studentGrade = input("학년을 입력하세요.(1~3) : ")
            elif i == 2 : 
                studentNumber = input("학번을 입력하세요 : ")
            elif i == 3 : 
                studentMajor = input("전공을 입력하세요 : ")
        
        if int(studentGrade) <= -1 or int(studentGrade) >= 4 or len(studentName) == 0 or len(studentMajor) == 0 or int(studentNumber) < 0: 
            print("입력값이 올바르지 않습니다.\n")
        else : 
            grade.append(studentGrade)
            name.append(studentName)
            number.append(studentNumber)
            major.append(studentMajor)
            check.append("없음")
            line()
            print(studentName, "학생 등록이 완료되었습니다.\n")

    # 전체 학생 목록 출력 기능
    elif mode == 2 :
        printAllStudents("전체")

    # 출석 체크 기능
    elif mode == 3 :
        cnt = len(name)

        line()
        print('출석을 진행합니다. 숫자를 입력하여 출결 상태를 입력해주세요')
        print("1 : 출석 | 2 : 지각 | 3 : 결석")
        line()

        for i in range(0, cnt) : 
            data = int(input(name[i] + " : "))

            if data == 1 : check[i] = "출석"
            elif data == 2 : check[i] = "지각"
            elif data == 3 : check[i] = "결석"
            else :
                print("올바른 값을 입력해주세요.")
                break

    # 출석 변경 기능
    elif mode == 4 :
        printAllStudents("전체")
        studentName = input("출석을 변경할 학생이름을 입력해주세요 : ")
        print()

        for i in range(0,len(name)) : 
            if name[i] == studentName : 
                line()
                print('출석을 변경합니다. 숫자를 입력하여 출결 상태를 입력해주세요')
                print("1 : 출석 | 2 : 지각 | 3 : 결석")
                line()

                data = int(input(name[i] + " : "))

                if data == 1 : 
                    check[i] = "출석" 
                    print("변경 완료")
                    break
                elif data == 2 :
                    check[i] = "지각"
                    print("변경 완료")
                    break
                elif data == 3 : 
                    check[i] = "결석"
                    print("변경 완료")
                    break
                else :
                    print("올바른 값을 입력해주세요.")
                    break

            elif i== len(name)-1 : 
                print("등록된 학생이 아닙니다")

    # 출석 학생 목록 출력 기능
    elif mode == 5 :
        printAllStudents("출석")

    # 지각 학생 목록 출력 기능
    elif mode == 6 :
        printAllStudents("지각")

    # 결석 학생 목록 출력 기능
    elif mode == 7 :
        printAllStudents("결석")

    # 프로그램 종료
    elif mode == 8 :
        print("프로그램을 종료합니다.")
        state = False
    
    # 입력 오류
    else : 
        print("번호를 다시 입력해주세요")