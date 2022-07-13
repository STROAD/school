from os import system, name
from time import sleep
import numpy as np
from sympy import symbols, Derivative, Integral
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt


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


x = symbols("x")


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
                    \n\n\n도움말에서 나가려면 아무키나 누르세요.\n"
                )

            elif n1 == 1:
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
                        st = float(input("\n첫번째 숫자를 입력해 주세요.\n"))
                        nd = float(input("\n두번째 숫자를 입력해 주세요.\n"))
                        print(f"\n\n{st} + {nd} = {st + nd}\n")
                        sleep(2)

                    elif ns == 2:
                        clearConsole()
                        st = float(input("\n첫번째 숫자를 입력해 주세요.\n"))
                        nd = float(input("\n두번째 숫자를 입력해 주세요.\n"))
                        print(f"\n\n{st} - {nd} = {st - nd}\n")
                        sleep(2)

                    elif ns == 3:
                        clearConsole()
                        st = float(input("\n첫번째 숫자를 입력해 주세요.\n"))
                        nd = float(input("\n두번째 숫자를 입력해 주세요.\n"))
                        print(f"\n\n{st} x {nd} = {st * nd}\n")
                        sleep(2)

                    elif ns == 4:
                        clearConsole()
                        st = float(input("\n첫번째 숫자를 입력해 주세요.\n"))
                        nd = float(input("\n두번째 숫자를 입력해 주세요.\n"))
                        print(f"\n\n{st} / {nd} = {st / nd}\n")
                        sleep(2)

                    elif ns > 4 or ns < 1:
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

            elif n1 == 2:
                clearConsole()
                fx = input("함수 f(x) 입력 : ")
                fprime = Derivative(fx, x).doit()
                print(f"f′(x) = {fprime} 입니다")

                sleep(2)

            elif n1 == 3:
                try:
                    clearConsole()
                    nd = int(
                        input(
                            "원하는 계산의 숫자를 눌러주세요.\
                        \n\n\n1 : 부정적분\n2 : 정적분\n\n"
                        )
                    )

                    if nd == 1:
                        clearConsole()
                        fx = input("함수 f(x) 입력 : ")
                        Fx = Integral(fx, x).doit()
                        print(f"Fx = {Fx} + C 입니다")
                        sleep(2)

                    elif nd == 2:
                        clearConsole()
                        fx = input("함수 f(x) 입력 : ")
                        a = input("아래끝 a 입력 : ")
                        b = input("위끝 b 입력 : ")
                        Fx = Integral(fx, (x, a, b)).doit()
                        print(f"Fx = {Fx} 입니다")
                        sleep(2)

                    elif nd > 2 or nd < 1:
                        raise NumberError(f"입력값 : {nd}")

                except NumberError as err:
                    print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
                    print(err)
                    sleep(1)
                    continue

                except:
                    print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
                    sleep(1)
                    continue

            elif n1 == 4:
                clearConsole()
                x = np.array(range(-100, 101))
                y = eval(input("함수 입력 : y = "))

                plt.figure("그래프 그리기")
                plt.xlabel("x")
                plt.ylabel("y", rotation=0)
                plt.grid(True)

                model = make_interp_spline(x, y)
                xs = np.linspace(-10, 10, 500)
                ys = model(xs)

                plt.axis([-10, 10, -10, 10])
                plt.plot(xs, ys)
                plt.show()
                sleep(2)

            elif n1 == 5:
                clearConsole()
                print("이용해주셔서 감사합니다.")
                sleep(1)
                break

        elif n1 > 5 or ns < 0:
            raise NumberError(f"입력값 : {n1}")

    except NumberError as err:
        print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
        print(err)
        sleep(1)
        continue

    except:
        print("\n\n에러가 발생했습니다.\n유효한 숫자를 입력해주세요.\n")
        sleep(1)
        continue
