def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/120583")

testinfo()


def solution(array, n):
    answer = 0

    for i in array:
        if i == n:
            answer += 1

    return answer