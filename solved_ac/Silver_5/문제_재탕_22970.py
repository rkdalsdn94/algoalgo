# 백준 - 실버5 - 문제 재탕 - 22970 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

증가하는 부분과 감소하는 부분의 수열을 각각 구한 뒤, 두 수열의 같은 인덱스의 합 중 max 값을 출력하면 되는 문제이다.
주의 해야 될 부분으론 다음이 있다.
    증가하는 부분이든, 감소하는 부분이든 둘 중 하나를 초기화 할 때 1로 초기화 해야 된다.
    본인을 포함시켜야 하기 때문에
    다른 당법으론 증가 감소 수열 모두 0으로 초기화 한 뒤 출력할 때 1을 더해도 된다.
        inc = [0] * n
        dec = [0] * n
        print(res + 1) 이런 식으로

증가하는 부분과 감소하는 부분을 구하는 방법은 쉽게 구할 수 있어 따로 설명을 적진 않는다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [1,2,3,2,1] # 5
# n = 6
# n_list = [1,2,1,3,4,1] # 4
# n = 5
# n_list = [1,1,1,1,1] # 1
# n = 5
# n_list = [3,2,1,2,3] # 3

increase_list = [1] * n
decrease_list = [0] * n
res = 0

for i in range(1, n):
    if n_list[i] > n_list[i - 1]:
        increase_list[i] = increase_list[i - 1] + 1

for i in range(n - 2, -1, -1):
    if n_list[i] > n_list[i + 1]:
        decrease_list[i] = decrease_list[i + 1] + 1

for i in range(n):
    res = max(res, increase_list[i] + decrease_list[i])

print(res)
