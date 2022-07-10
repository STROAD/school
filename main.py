from os import system, name
from time import sleep
import matplotlib.pyplot as plt
from sympy import symbols, Derivative, Integral


class NumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


clearConsole = lambda: system("cls" if name in ("nt", "dos") else "clear")


def progressBar(
    iterable, prefix="", suffix="", decimals=1, length=100, fill="█", printEnd="\r"
):

    total = len(iterable)

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / int(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + "-" * (length - filledLength)
        print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)

    printProgressBar(0)

    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()


items = list(range(0, 37))


print("\n\n school\n")
for item in progressBar(items, prefix=" 시작중 :", suffix="완료", length=50):
    sleep(0.001)


while True:
    try:
        clearConsole()
        n1 = int(
            input(
                "원하는 작업의 번호를 입력해주세요.\n\n\n0 : 도움말\n1 : 사칙연산\n2 : 미분\n3 : 적분\n4 : 그래프 그리기\n5 : 나가기\n\n"
            )
        )

        if 0 <= n1 <= 5:

            if n1 == 0:
                clearConsole()
                input(
                    "\n\n\n도움말\n\
                    \n\n※ 버전※\
                    \n\nv1.0\
                    \n\n\n※ 안내※\
                    \n\
                    \n프로그램을 종료하고 싶으시면 초기화면에서 '5'를 눌러주세요.\
                    \n\n\n※ 주의※\n잘못된 값을 입력하면 초기화면으로 돌아갑니다.\
                    \n\n\n도움말에서 나가려면 아무키나 누르세요."
                )

    except:
        print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")

    try:

        if n1 == 1:

            try:
                clearConsole()
                ns = int(
                    input(
                        "원하는 계산의 숫자를 눌러주세요.\
                    \n\n\n1 : 덧셈\n2 : 뺄셈\n3 : 곱셈\n4 : 나눗셈\n\n"
                    )
                )

                if ns == 1:
                    clearConsole()
                    st = int(input("\n첫번째 숫자를 입력해 주세요.\n"))
                    nd = int(input("\n두번째 숫자를 입력해 주세요.\n"))
                    print(f"\n\n{st} + {nd} = {st + nd}\n")
                    sleep(2)

                if ns == 2:
                    clearConsole()
                    st = int(input("\n첫번째 숫자를 입력해 주세요.\n"))
                    nd = int(input("\n두번째 숫자를 입력해 주세요.\n"))
                    print(f"\n\n{st} - {nd} = {st - nd}\n")
                    sleep(2)

                if ns == 3:
                    clearConsole()
                    st = int(input("\n첫번째 숫자를 입력해 주세요.\n"))
                    nd = int(input("\n두번째 숫자를 입력해 주세요.\n"))
                    print(f"\n\n{st} x {nd} = {st * nd}\n")
                    sleep(2)

                if ns == 4:
                    clearConsole()
                    st = int(input("\n첫번째 숫자를 입력해 주세요.\n"))
                    nd = int(input("\n두번째 숫자를 입력해 주세요.\n"))
                    print(f"\n\n{st} / {nd} = {st / nd}\n")
                    sleep(2)

                if ns > 4 or ns < 1:
                    raise NumberError(f"입력값 : {ns}")

            except NumberError as err:
                print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
                print(err)
                sleep(1)
                continue

            except:
                print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
                sleep(1)
                continue

        if n1 == 2:

            sleep(2)

        if n1 == 3:

            sleep(2)

        if n1 == 4:

            sleep(2)

        if n1 == 5:
            clearConsole()
            print("이용해주셔서 감사합니다.")
            sleep(1)
            break

    except NumberError as err:
        print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
        print(err)

    except:
        print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
