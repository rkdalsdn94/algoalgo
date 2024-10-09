# 백준 - 실버3 - 교수님의 기말고사 - 20126 - 정렬, 구현 문제
'''
정렬, 구현 문제

정렬과 구현을 사용하면 된다.
출력할 때 시작 가능한 시간이 여러 개 있으면 가장 앞선 시각을 출력해야 된다.
즉, 처음부터 시작할 수 있는 시간을 계산하고, 시작할 수 있는 시간이 없으면 -1을 출력한다.

풀이 과정
    1. n, m, s를 입력받는다.
    2. n_list에 n개의 리스트를 입력받는다.
    3. n_list를 정렬한다.
    4. n_list[0][0]이 m보다 크거나 같으면 0을 출력하고 종료한다.
    5. temp를 0으로 초기화한다.
    6. n_list의 길이만큼 반복문을 돌린다.
        6.1. 만약 n_list[i][0] - temp이 m보다 크거나 같으면 temp를 출력하고 종료한다.
        6.2. temp에 n_list[i][0] + n_list[i][1]을 더한다.
    7. s - temp이 m보다 크거나 같으면 temp를 출력하고 종료한다.
    8. 그렇지 않으면 -1을 출력한다.
'''

n, m, s = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m, s = 2, 3, 5
# n_list = [[0, 1], [4, 1]] # 1
# n, m, s = 2, 3, 5
# n_list = [[0, 2], [4, 1]] # -1

n_list.sort()

if n_list[0][0] >= m:
    print(0)
    exit(0)

temp = 0
for i in range(n):
    if n_list[i][0] - temp >= m:
        print(temp)
        exit(0)
    temp = n_list[i][0] + n_list[i][1]

if s - temp >= m:
    print(temp)
else:
    print(-1)
