'''
수학 문제

수학 문제라고 생각하는 이유가 해당 문제에선
a, b = (a + 1) // 2, (b + 1) // 2 -> 이 부분만 생각 나면 문제는 바로 해결된다.
'''

def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer

print(solution(8, 4, 7)) # 3
