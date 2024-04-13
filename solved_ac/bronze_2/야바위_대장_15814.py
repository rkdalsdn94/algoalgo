# 백준 - 브론즈2 - 야바위 대장 - 15814 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순히 문자열의 위치를 바꿔주면 되는 문제이다.

풀이 과정
1. 입력을 받고, 문자열을 리스트로 변환한다.
2. 입력으로 들어온 횟수만큼 반복문을 돌면서 문자열의 위치를 바꿔준다.
    2.1 - 이때 -1을 하지 않아도 된다. 문제 입력 부분에서 '문자열의 맨 처음 글자는 0번째 글자이다' 라는 조건이 있다.
3. res를 문자열로 합쳐서 출력한다.
'''

s = list(input())
t = int(input())
t_list = [list(map(int, input().split())) for _ in range(t)]

# 테스트
# s = list('Youngmaan-good')
# t = 2
# t_list = [[1, 3], [9, 2]] # Yn-ogmaanugood

for i, j in t_list:
    s[i], s[j] = s[j], s[i]

print(''.join(s))
