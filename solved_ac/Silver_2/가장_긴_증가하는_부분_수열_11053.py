'''
dp식만 세우면 간단하게 풀 수 있다.
a_list의 범위 만큼 반복문을 돌고 해당 인덱스 값을 가지고
그 전 인덱스를 비교한 뒤에 dp식에 값 추가
dp식에서 가장 큰 값을 출력 (가장 긴 수열을 찾아야 된다.)
'''

a = int(input())
a_list = list(map(int, input().split()))

# 테스트
# a = 6
# a_list = [10, 20, 10, 30, 20, 50]

res = [1] * a

for i in range(a):
    for j in range(i):
        if a_list[i] > a_list[j]:
            # print(a_list[i], a_list[j], i)
            res[i] = max(res[i], res[j] + 1)

print(max(res))