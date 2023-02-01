# 백준 - 실버4 - 치킨 TOP N - 11582 - 정렬, 분할 정복 문제
'''
정렬, 분할 정복 문제

기본적인 방법으론 병합(Merge) 정렬을 구현하면 된다. 근데, 문제 조건중에 'N은 항상 2의 거듭제곱 꼴이다.' 라는 조건이 있다.
해당 조건으로 반복문을 통해 n // k 의 값을 가지는 temp를 갖고 해당 범위만큼 정렬을 한 후 res에 추가한 다음 최종 res를 출력해도 정답이 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))
k = int(input())

# 테스트
# n = 8
# n_list = [1,5,2,4,2,9,7,3]
# k = 2 # 1 2 4 5 2 3 7 9

temp = n // k
res = []

for i in range(0, n, temp):
    res += sorted(n_list[i:i + temp])

print(*res)
