# 백준 - 브론즈3 - ABC - 3047 - 단순 구현 문제
'''
단순 구현 문제

숫자 list 형으로 입력 받은 후, word의 글자와 비교해서 A위치가 가장 작은 값, B 위치의 중간 값, C 위치의 제일 큰 값을 넣고 출력하면 된다.
'''

numbers = sorted(map(int, input().split()))
word = input()

# 테스트
# numbers = sorted([1, 5, 3])
# word = 'ABC' # 1 3 5
# numbers = sorted([6, 4, 2])
# word = 'CAB' # 6 2 4

res = []

for i in word:
    if i == 'A':
        res.append(numbers[0])
    elif i == 'B':
        res.append(numbers[1])
    else:
        res.append(numbers[-1])

print(*res)
