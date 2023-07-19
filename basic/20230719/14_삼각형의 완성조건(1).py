from functools import reduce


def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/120889")

testinfo()


def solution(sides):
    answer = 0
    maxnum = max(sides)
    sides.remove(maxnum)
    total = reduce(lambda acc, cur: acc + cur, sides, 0)

    if maxnum < total:
        answer = 1
    else:
        answer = 2

    return answer
