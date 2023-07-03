# 백준 - 브론즈2 - 지우개 - 21756 - 수학, 구현, 시뮬레이션 문제
'''
수학, 단순 구현, 시뮬레이션 문제

단순 구현문제이다. n의 범위가 크지 않아 완전 탐색 방식으로 풀었다.
1 ~ n 까지의 범위로 n_list를 만든다.
해당 리스트의 홀수 칸들을 temp 에 담은 후, temp의 값을 꺼내면서 n_list에서 제거해준다.
    - 홀수 칸들을 담을 때 list는 0번지 부터 시작이므로 2로 나눠지는 값을 담아야 된다.

문제의 난이도와 n의 범위가 크지 않아 단순하게 구현할 수 있었다.
다른 사람의 풀이를 봤을 때,
binary로 만든 후 shift 연산를 사용했는데.. 이해가 잘 안간다. 이진수로 다루는 연산이 아직 익숙하지 않은거 같다.
'''

n = int(input())

# 테스트
# n = 1 # 1
# n = 2 # 2
# n = 5 # 4

n_list = [ i for i in range(1, n + 1) ]

while len(n_list) != 1:
    temp = []
    for i in range(len(n_list)):
        if i % 2 == 0:
            temp.append(n_list[i])
    for i in temp:
        n_list.remove(i)

print(*n_list)
