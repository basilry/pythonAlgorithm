def testinfo():
    print("https://school.programmers.co.kr/learn/courses/30/lessons/181910")

testinfo()


def solution(my_string, n):
    answer = my_string[-n:]

    return answer

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))

