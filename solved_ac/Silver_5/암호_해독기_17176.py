# 백준 - 실버5 - 암호해독기 - 17176 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
 - 입력을 형식에 맞게 잘 입력하고, 비밀 키(n_list)를 입력받을 때는 정렬한다.
 - temp 딕셔너리에 처음 시작을 빈 공간(' ')과 0으로 만들어주고,
    - 'A' ~ 'Z'와 'a' ~ 'z' 알파벳과 1씩 증가하는 숫자를 넣어준다.
 - 이후 입력받은 문자를 딕셔너리의 값으로 담겨 있는 숫자로 바꾸고 res 리스트에 담는다.
 - 이후 res를 정렬한 리스트와 비밀키 리스트가 같다면 y, 다르다면 n을 출력한다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))
word = input()

# 테스트
# n = 11
# n_list = sorted([44, 0, 38, 41, 38, 31, 23, 8, 41, 30, 38])
# word = 'Hello World' # y
# n = 5
# n_list = sorted([12, 3, 34, 52, 0])
# word = 'apple' # n

temp = {' ': 0}

for i in range(65, 91):
    temp[chr(i)] = i - 64

for i in range(97, 123):
    temp[chr(i)] = i - 70

res = sorted([temp[i] for i in word])
print('y' if res == n_list else 'n')
