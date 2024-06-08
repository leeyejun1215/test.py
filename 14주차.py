
menu = ["냉면", "볶음밥", "피자", "짜장면"]

def kiosk():
    while True:
        try:
            print("메뉴를 선택하세요:")
            for i, item in enumerate(menu, start=1):
                print(f"{i}. {item}")
            choice = input("원하는 메뉴의 번호를 입력하세요: ")
            choice_num = int(choice)
            if 1 <= choice_num <= len(menu):
                print(f"선택한 메뉴는 {menu[choice_num - 1]}입니다.")
                break
            else:
                print("잘못된 번호입니다. 1에서 4 사이의 번호를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")
        except IndexError:
            print("유효하지 않은 번호입니다. 다시 입력하세요.")
kiosk()
