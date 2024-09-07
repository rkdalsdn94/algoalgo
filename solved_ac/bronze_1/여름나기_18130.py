# 백준 - 브론즈1 - 여름나기 - 18130 - 수학, 구현, 사칙연산 문제
'''
수학, 구현, 사칙연산 문제

n : 선풍기 개수
q : 집까지 걸리는 시간
n_list : [선풍기 가격, 추가비용을 내야 하는 시간 간격, 추가 비용의 초기값] 형식의 리스트

k 시간이 흘렀을 때 c만큼 비용
2 * k 시간이 흘렀을 때 2 * c만큼 비용
t가 자연수 일 때 t * k초가 흘렀을 때 t * c만큼 비용
    ex)
    선풍기 가격 : 500
    3시간 마다 : 100원 추가
    12시간이 걸린다면
    3시간 100원, 6시간 200원, 9시간 300원, 12시간은 집 도착이라 계산 x
    600 + 500 = 1100원
주의할 점으론 total_amount의 초기값을 (2 ** 63 - 1) 보다 크게 설정해야 된다.

풀이 과정
    1. n, q를 입력받는다.
    2. n_list를 입력받는다.
    3. id, total_amount를 -1, 2 ** 65로 초기화한다.
    4. n_list를 돌면서 다음을 확인한다.
        4.1. p, k, c를 각각 할당한다.
        4.2. cnt를 구한다. (q - 1) // k
        4.3. temp를 구한다. p + cnt * (cnt + 1) // 2 * c
        4.4. temp가 total_amount보다 작다면 id, total_amount를 갱신한다.
    5. id, total_amount를 출력한다.
'''

n, q = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, q = 5, 12
# n_list = [
#     [100, 2, 100],
#     [200, 3, 100],
#     [0, 10, 500],
#     [0, 10, 600],
#     [1000, 13, 100]
# ] # 3 500

id, total_amount = -1, 2 ** 65

for i in range(n):
    p, k, c = n_list[i]
    cnt = (q - 1) // k

    temp = p + cnt * (cnt + 1) // 2 * c
    if temp < total_amount:
        id, total_amount = i + 1, temp

print(id, total_amount)
