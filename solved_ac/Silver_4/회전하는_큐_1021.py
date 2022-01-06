from collections import deque

def solution(n, m, m_list):
    res = 0
    q = deque([i for i in range(1, n+1)])

    for i in m_list:
        while 1:
            if q.index(i) == 0:
                q.popleft()
                break
            
            if q.index(i) - 0 <= len(q) - q.index(i):
                res += 1
                q.append(q.popleft())
            else:
                res += 1
                q.appendleft(q.pop())

    return res

n, m = map(int, input().split())
m_list = map(int, input().split())

print(solution(n, m, m_list))


# 테스트
# print(solution(10, 3, [1,2,3])) # 0
# print(solution(10, 3, [2,9,5])) # 8
# print(solution(32, 6, [27, 16, 30, 11, 6, 23])) # 59
# print(solution(10, 10, [1, 6, 3, 2, 7, 9, 8, 4, 10, 5])) # 14
