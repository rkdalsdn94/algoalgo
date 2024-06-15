# 백준 - 실버2 - 영역 색칠 - 28015 - 그리디 문제
'''
그리디 문제

그리디 방식으로 푸는데, 어느 정도는 완전 탐색 느낌도 있다.
이 문제를 푸는데 핵심은 덧칠이 가능한지 확인하는 것이다.
    덧칠을 파악하는 부분을 색1, 색2 두 개의 flag를 사용해서 풀었다.
문제를 다 풀고 다른 사람의 풀이를 보니, 문자열로 접근하는게 훨씬 더 깔끔하게 풀 수 있다.
    해당 방식은 코드를 직접 적기보다 간단히 설명하면 다음과 같다.
    '1'과 '2'로 split 한 뒤, 원래 문자열의 길이에서 split 한 값을 빼고 그 중 min을 출력하는 방식이다.

풀이 과정
    1. 입력을 받고, n_list를 만든다.
    2. n_list를 돌면서 덧칠이 가능한지 확인하고, 덧칠이 가능하면 덧칠을 한다.
    3. 덧칠을 한 후, res를 출력한다.
'''

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 2, 2
# n_list = [[2, 1], [0, 0]] # 2
# n, m = 4, 4
# n_list = [[1, 0, 0, 1], [1, 1, 2, 2], [0, 0, 1, 2], [1, 1, 1, 1]] # 7
# n, m = 2, 6
# n_list = [[2, 1, 2, 1, 1, 2], [0, 0, 0, 0, 0, 0]] # 3

res = 0

for i in n_list:
    while 1:
        color_one_flag, color_two_flag = False, False

        for j in range(m):
            if i[j] == 0:
                color_one_flag = False
                color_two_flag = False

            if i[j] == 1 and not color_one_flag and not color_two_flag:
                i[j] -= 1
                res += 1
                color_one_flag = True
            elif i[j] == 2 and not color_one_flag and not color_two_flag:
                i[j] -= 2
                res += 1
                color_two_flag = True
            elif i[j] == 1 and color_one_flag:
                i[j] -= 1
            elif i[j] == 2 and color_two_flag:
                i[j] -= 2

        if sum(i) == 0:
            break

print(res)
