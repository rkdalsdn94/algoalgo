# 백준 - 브론즈1 - 유니대전 퀴즈쇼 - 20362 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순한 구현 문제이다.

풀이 과정
1. 입력값을 입력 받는다.
2. n_list를 반복하면서 s와 같은 값이 나오면 그 전까지의 값 중 s와 같은 값이 있는지 확인하고 있다면 res에 1을 더한다.
3. 반복이 끝나면 res를 출력한다.
'''

n, s = input().split()
n = int(n)
n_list = [list(input().split()) for _ in range(n)]

# 테스트
# n, s = 3, 'duck'
# n_list = [
#     ['oridya', 'hello'], ['orihehe', 'hi'], ['duck', 'hi']
# ] # 1
# n, s = 8, 'orihehe'
# n_list = [
#     ['orihehe', 'duck'], ['skynet', 'duck'],
#     ['rdd', 'duck'], ['vega', 'duck'],
#     ['reversing', 'duck'], ['dongbin', 'duck'],
#     ['kimyh', 'duck'], ['hunni', 'duck']
# ] # 0
# n, s = 8, 'orihehe'
# n_list = [
#     ['hunni', 'duck'], ['skynet', 'duck'],
#     ['rdd', 'duck'], ['vega', 'duck'],
#     ['reversing', 'duck'], ['dongbin', 'duck'],
#     ['kimyh', 'duck'], ['orihehe', 'duck'],
# ] # 7
# n, s = 8, 'orihehe'
# n_list = [
#     ['skynet', 'dduck'], ['rdd', 'dduck'],
#     ['vega', 'dduck'], ['reversing', 'dduck'],
#     ['dongbin', 'dduck'], ['kimyh', 'dduck'],
#     ['hunni', 'dduck'], ['orihehe', 'duck']
# ] # 0

res = 0

for i in range(n):
    if n_list[i][0] == s:
        for j in range(i):
            if n_list[j][1] == n_list[i][1]:
                res += 1
        break

print(res)
