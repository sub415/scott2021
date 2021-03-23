print("갤러그 게임 시작")
print("적 비행기 발생")
print("1.발사 2.오른쪽 이동 3.왼쪽 이동")
number = input("숫자를 입력하세요: ")
print("당신의 입력값", number)

# 만약에 1번을 누르면 총알 발사
if number == "1":
    print("총알 발사")
# 만약에 2번을 누르면 오른쪽 
if number == "2":
    print("오른쪽 으로 이동")
# 만약에 3번을 누르면 왼쪽 
if number == "3":
    print("왼쪽 으로 이동")