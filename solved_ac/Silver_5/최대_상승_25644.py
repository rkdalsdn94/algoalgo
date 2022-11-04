###################################################
# 백준 - 실버5 - 최대 상승 - 25644 - 구현, 그리디 문제
'''
구현, dp, 그리디 문제

풀이 과정
1. 입력받은 n_list의 첫 번째 인자를 temp에 담는다.
2. 전체 코드를 실행하고 결과로 출력하기 위한 res 리스트를 n의 크기만큼, 0으로 초기화 된 상태로 만든다.
3. 1부터 n까지 만큼 반복문을 실행한다.
4. 반복문을 실행할 동안 temp의 값으로 n_list[i]를 비교한다.
    4.1 temp가 n_list[i] 보다 작으면 res의 현재 인덱스를 n_list[i] - temp의 값으로 바꾼다.
    4.2 temp가 더 클 경우 temp의 값을 갱신해준다.
5. res의 가장 큰 값을 반환한다. -> 이 상태가 가장 비싸게 팔 수 있는 상태이다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [4,2,3,1,5] # 4
# n = 3
# n_list = [3,2,1] # 0
# n = 4
# n_list = [7,1,2,6] # 5

temp = n_list[0]
res = [0] * n

for i in range(1, n):
    if temp < n_list[i]:
        res[i] = n_list[i] - temp
    else:
        temp = n_list[i]

print(max(res))
