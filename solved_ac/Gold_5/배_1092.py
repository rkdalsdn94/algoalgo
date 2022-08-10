'''
그리디, 정렬 문제

Pypy3로 제출해야 된다.
역순으로 정렬한 후에 무게 제한이 가장 높은 크레인이 가장 무거운 박스의 무게를 못 실으면 어차피 안되는거라 -1을 출력한다.
모든 크레인은 동시에 움직일 수 있으므로 크레인 무게제한 리스트를 하나씩 꺼내면서 박스의 무게와 비교한다.
박스의 무게가 더 작을시 해당 박스를 지워가면서 반복문이 끝나면 res를 1 증가시킨다.
'''
import sys; input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())), reverse=True) # 크레인
m = int(input())
m_list = sorted(list(map(int, input().split())), reverse=True) # 박스

# 테스트
# n = 3
# n_list = sorted([6, 8, 9], reverse=True)
# m = 5
# m_list = sorted([2,5,2,4,7], reverse=True) # 2
# n = 2
# n_list = sorted([19, 20], reverse=True)
# m = 7
# m_list = sorted([14, 12, 16, 19, 16, 1, 5], reverse=True) # 4
# n = 4
# n_list = sorted([23, 32, 25, 28], reverse=True)
# m = 10
# m_list = sorted([5, 27, 10, 16, 24, 20, 2, 32, 18, 7], reverse=True) # 3
# n = 10
# n_list = sorted([11, 17, 5, 2, 20, 7, 5, 5, 20, 7], reverse=True)
# m = 5
# m_list = sorted([18, 18, 15, 15, 17], reverse=True) # 2

res = 0
flag = True

if m_list[0] > n_list[0]: # 크레인 무게 제한 체크
    print(-1)
    exit(0)

while m_list:
    if not m_list: break # 모든 박스가 비워졌으면 while문 그만해도 된다.

    for i in n_list:
        for j in m_list:
            if i >= j:
                m_list.remove(j)
                break

    res += 1

print(res)
