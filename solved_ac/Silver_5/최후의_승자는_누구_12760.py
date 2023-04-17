# 백준 - 실버5 - 최후의 승자는 누구? - 12760 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

코드 옆에 주석으로 간단한 설명을 적어놨다.
사실 주석 없이 코드만 읽어도 크게 어렵지 않은 문제라 코드만 확인해도 괜찮을거 같다.
핵식은 n_list를 입력받을 때 내림차순 정렬을 하고, n_list의 값이 중복일 때의 상황만 고려하면 크게 어렵지 않다.
'''

n, m = map(int, input().split())
n_list = [ sorted(list(map(int, input().split())), reverse=True) for _ in range(n) ]

# 테스트
# n, m = 5, 3
# n_list = [
#     sorted([5,4,3], reverse=True),
#     sorted([2,5,1], reverse=True),
#     sorted([3,3,3], reverse=True),
#     sorted([2,2,2], reverse=True),
#     sorted([1,1,1], reverse=True)
# ] # 1
# n, m = 5, 3
# n_list = [
#     sorted([5,4,3], reverse=True),
#     sorted([3,4,5], reverse=True),
#     sorted([3,5,4], reverse=True),
#     sorted([4,5,3], reverse=True),
#     sorted([3,4,4], reverse=True)
# ] # 1 2 3 4

temp_list = [0] * n
res = []

for i in range(m):
    temp = n_list[0][i]

    for j in range(n): # max 값인지 확인
        temp = max(temp, n_list[j][i])

    for j in range(n): # max 값이 중복일 수도 있어서
        if n_list[j][i] == temp:
            temp_list[j] += 1

for i in range(n):
    if max(temp_list) == temp_list[i]: # max 값이 중복일 때를 대비
        res.append(i + 1)

print(*res)
