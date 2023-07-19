import math

def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/120830")

testinfo()


def solution(n, k):
    answer = 0

    sheep = n * 12000
    drink = (k - math.floor(n / 10)) * 2000

    answer = sheep + drink

    return answer