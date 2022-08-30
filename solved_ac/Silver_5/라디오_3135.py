'''
백준 - 실버5 - 라디오 - 3135
그리디 문제

절댓값을 이용해서 n_list를 입력받고,
최종적으로 a - b보다 + 1한 후 더 작은 값이 n_list에 있다면 해당 값을 출력하면 된다..
'''

a, b = map(int, input().split())
n = int(input())
n_list = [ abs(int(input()) - b) for _ in range(n) ]

# 테스트
# a, b = 100, 15
# n = 1
# n_list = [ abs(15 - 15) ] # 1
# a, b = 88, 17
# n = 3
# n_list = [ abs(18 - b), abs(1 - b), abs(42 - b) ] # 2
# a, b = 64, 120
# n = 1
# n_list = [ abs(567- b) ] # 56
 
print(min(abs(a - b), min(n_list) + 1))
