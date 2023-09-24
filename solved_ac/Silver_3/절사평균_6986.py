# 백준 - 실버3 - 절사평균 - 6986 - 구현, 정렬 문제
'''
구현, 정렬 문제

문제를 풀 때 두 가지 부분을 조심해야 한다.
    1. 예제도 맞고, 코드가 맞는거 같은데 '틀렸습니다.'가 나올 경우 (부동 소수점 처리)
    2. 인덱스 에러 (k가 0 일 떄)

# 1. 부동 소수점 처리
    부동 소수점 관련해서는 찾아보면 되고, 해결하는 방식은 0.00000001 을 더해서 소수점을 구하면 된다.

# 2. 인덱스 에러
    k가 0일 경우를 확인해 봐야 한다.
    k가 0일 땐 '절사평균', '보정평균' 모두 인덱스의 모든 합을 더해 n으로 나눈 뒤 출력하고, 프로그램을 종료하면 된다.

문제를 푸는 방식은 정렬 후 리스트 슬라이싱을 활용해서 풀면 된다.
이 부분은 크게 어렵지 않으므로 https://pythontutor.com/render.html#mode=display 해당 사이트에서 슬라이싱을 잘 활용하면 된다.
'''

import sys; input = sys.stdin.readline

n, k = map(int, input().split())
score_list = sorted([float(input()) for _ in range(n)])
# print('score_list = ', score_list)

# 테스트
# n, k = 7, 2
# score_list = sorted([9.3, 9.5, 9.6, 9.8, 9.1, 5.0, 9.3])

if k == 0:
    print('{:.2f}'.format(sum(score_list) / n))
    print('{:.2f}'.format(sum(score_list) / n))
    exit(0)

trimmed_mean = sum(score_list[k:-k]) / (n - k * 2) + 0.00000001
adjusted_mean = (score_list[k:-k][0] * k + sum(score_list[k:-k]) + score_list[k:-k][-1] * k) / n + 0.00000001

print(f'{trimmed_mean:.2f}')
print(f'{adjusted_mean:.2f}')
