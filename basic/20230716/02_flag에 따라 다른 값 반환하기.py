def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/181933")

testinfo()


def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b


print(solution(-4, 7, True))
print(solution(-4, 7, False))