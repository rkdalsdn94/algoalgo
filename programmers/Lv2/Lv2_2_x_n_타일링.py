'''
이 전에 백준에서 푼 문제랑 똑같이 풀었다.

백준 11726 문제를 보면 풀이도 적어놨다.
근데 백준에서 풀 때에는 범위가 여기 보다 작아서 그러닞
반복문을 돌면서 % 1000000007를 안했었는데,
여기서는 반목문 돌면서 하지 않으면 시간 초과가 나온다.

참고로 파이썬은 나머지 연산자의 처리 속도가 되게 느리다고 한다!
'''

def solution(n):
    answer = [0] * (n + 2)
    answer[1] = 1
    answer[2] = 2
    
    for i in range(3, n + 1):
        answer[i] = answer[i-1] + answer[i-2] % 1000000007

    return answer[n] % 1000000007

print(solution(4)) # 5
