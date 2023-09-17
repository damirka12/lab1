import math




a = int(input())
b = int(input())
c = int(input())

def sumOfThree(a, b, c):
    sum = a + b + c
    print("Сумма трех: ", sum)

def areaOfTriangle(a, b):
    area = (a*b)/2
    print("Площадь треугольника с катетами ", a, " & ", b, "это: ", area)


def appleDividing(a, b):
    apps = b // a
    apRem = b % a
    print("Яблок на каждого школьника: ", apps, "\nОстаток в корзине: ", apRem)


def elClock(a):
    hours = a // 60
    min = a - (hours * 60)
    while hours >= 24: hours = hours - 24
    print("Time: ", hours, ":", min)


d = str(input())
def hello(d):
    print("Hello,", d + "!")


def nextPrev(a):
    next = a + 1
    prev = a - 1
    print("The next number for the number", a, "is", str(next) + "." "\nThe previous number for the number", a, "is", str(prev) + ".")


def tables(a, b, c):
    aTab = math.ceil(a / 2)
    bTab = math.ceil(b / 2)
    cTab = math.ceil(c / 2)
    tables = aTab + bTab + cTab
    print(tables)


l = int(input())
N = int(input())

def Shnur(a, b, l, N):
res = (2*l) + (b*(N-1) * 2) + (a*(N*2 - 1))
print(res)