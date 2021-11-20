# 집안의 가전들이 모두 인터넷에 연결되어 있는 IOT의 세상이 다가왔다
# 이러한 기기틀을 통합적으로 관리하기 위한 프로그램을 개발해야한다.
# 프로토타입으로 장치의 전원을 ON,OFF할 수 있도록 프로그램을 만들어야한다.
# 현재 등록된 장소는 침실, 거실, 부엌, 서재 밖에 없다고 가정한다.

state = True
mode = 0

# 침실, 거실, 부엌, 서재
#[장소,장치이름, 전원상태]

place = ["침실","거실","부엌","서재"]
device = [
            ["침실","TV","ON"],["침실","형광등","ON"],["침실","에어컨","OFF"],
          ["거실","TV","OFF"],["거실","형광등","OFF"],["거실","블루투스스피커","OFF"],["거실","플레이스테이션","OFF"],
          ["부엌","전자레인지","OFF"],["부엌","식탁불","ON"],["부엌","식기세척기","ON"],
          ["서재","컴퓨터","OFF"],["서재","프린터","OFF"],["서재","led스탠드","ON"]
          ]

# 메인 화면
def mainPage() :
    print("\n","-"*54)
    
    for i in range(2) : 
        print("│"," "*52,"│")
        
    print("│"," "*18,"IOT Management"," "*18,"│")
    
    
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

# 장치 목록
def showDevice() : 
    for i in range(0,len(place)) : 

        print(place[i])
        line()
        
        for j in range(0,len(device)) : 
            if(device[j][0] == place[i]) : 
               print(device[j][2].rjust(3) + "   " + device[j][1])
                
        print()
                    

while state : 
    
    mainPage()
    
    print()
    print("     1. 장치 제어")
    print("     2. 장치 추가")
    print("     3. 장치 제거")
    print("     4. 위치별 장치 목록")
    print("     5. 종료")
    print()
    line()
    
    mode = int(input("항목을 숫자로 입력해주세요 : "))
    print()
    
    if mode == 1 : 
        dialog("장치 제어를 시작합니다\n명령어를 입력해주세요\n\n ex) 침실 TV ON\n ex) 부엌 전자레인지 ON")
        run = input("명령어를 입력하세요. : ")
        
        data = run.split(" ")
        
        location = data[0]
        deviceName = data[1]
        power = data[2]
        
        for i in range(0,len(device)) : 
            if device[i][0] == location and device[i][1] == deviceName : 
                if power == device[i][2] : 
                    if power == "ON" : 
                        dialog("장치가 이미 켜져 있습니다.")
                        break
                    elif power == "OFF" : 
                        dialog("장치가 이미 꺼져 있습니다.")
                        break
                elif power != device[i][2] and power == "ON" : 
                    device[i][2] = power
                    dialog("장치의 전원을 ON 하였습니다.")
                    break
                elif power != device[i][2] and power == "OFF" : 
                    device[i][2] = power
                    dialog("장치의 전원을 OFF 하였습니다.")
                    break
            elif i == len(device) - 1 : 
                dialog("장치가 존재하지 않거나, 명령어를 인식할 수 없습니다.")
    
    elif mode == 2 : 
        dialog("장치 추가를 시작합니다.\n추가할 장소와 장치명을 입력해주세요\n\n ex) 거실 에어컨")
        
        run = input("명령어를 입력하세요. : ")
        
        data = run.split(" ")
        
        location = data[0]
        deviceName = data[1]
        
        for i in range(0,len(device)) : 
            if location == device[i][0] and deviceName == device[i][1] : 
                dialog("이미 존재하는 장치 입니다")
                break
            elif i == len(device) -1 : 
                tmp = []
                tmp.append(location)
                tmp.append(deviceName)
                tmp.append("OFF")
                
                device.append(tmp)
                dialog("장치가 성공적으로 추가되었습니다.")                    
        
    elif mode== 3 : 
        dialog("장치 제거를 시작합니다.\n제거할 장소와 장치명을 입력해주세요\n\n ex) 거실 에어컨")
        
        run = input("명령어를 입력하세요. : ")
        
        data = run.split(" ")
        
        location = data[0]
        deviceName = data[1]
        
        for i in range(0,len(device)) : 
            if location == device[i][0] and deviceName == device[i][1] : 
                device.remove(device[i])
                dialog("장치를 성공적으로 제거하였습니다.")
                break
            elif i == len(device) -1 : 
                dialog("장치가 존재하지 않거나 명령어를 잘못입력하였습니다.")
        
    elif mode == 4 :
        dialog("장치 목록과 상태를 출력합니다.")
        showDevice()
        
    elif mode == 5 : 
        state = False
        dialog("프로그램을 종료합니다.")
        
    else : 
        dialog("올바른 번호를 입력해 주세요.")