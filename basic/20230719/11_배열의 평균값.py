def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/120817")

testinfo()


def solution(numbers):
    answer = 0

    for i in numbers:
        answer += i

    return answer / len(numbers)