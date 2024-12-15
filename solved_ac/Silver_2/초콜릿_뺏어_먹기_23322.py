# 백준 - 실버2 - 초콜릿 뺏어 먹기 - 23322 - 그리디, 에드 훅 문제
'''
그리디, 에드 훅 문제

풀이 과정
    1. 초콜릿을 입력받는다.
    2. 초콜릿을 정렬한다.
    3. 초콜릿의 개수를 줄여가면서 가장 작은 초콜릿 개수를 찾는다.
    4. 가장 작은 초콜릿 개수보다 큰 초콜릿 개수를 줄여간다.
    5. 초콜릿 개수를 줄이는 동안 카운트를 증가시킨다.
    6. 카운트와 날짜를 출력한다.
'''

def solve(n_list):
    day, cnt, temp = 0, 0, min(n_list)

    for i in range(1, len(n_list)):
        # 현재 초콜릿 개수가 이전 초콜릿 개수와 같거나 크고, 가장 작은 초콜릿 개수(temp)보다 크다면
        if n_list[i - 1] <= n_list[i] and temp < n_list[i]:

            # 현재 초콜릿 개수가 이전 초콜릿 개수와 같아질 때 까지 줄인다.
            while n_list[i] > n_list[i - 1]:
                n_list[i] -= 1
                cnt += 1

            day += 1

    print(cnt, day)

n, k = map(int, input().split())
n_list = list(map(int, input().rstrip().split()))

# 테스트
# n, k = 4, 2
# n_list = [1, 2, 2, 3] # 4 3
# n, k = 2, 1
# n_list = [5, 5] # 0 0

solve(sorted(n_list))
