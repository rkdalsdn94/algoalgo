# 백준 - 실버5 - 여우 사인 - 14709 - 단순 구현 문제
'''
단수 구현 문제

여우 사인이 안 되는 두 가지 경우만 제외한 뒤 나머지는 여우 사인으로 출력하면 된다.

여우 사인이 아닌 두 경우
    - n의 범위가 2보다 작거나 같고, 4보다 크거나 같으면 틀리는 출력과
    - 입력으로 들어온 숫자들이 다음과 같은 경우가 아니여야 한다. (1, 3 = 3, 1), (1, 4 = 4, 1), (3, 4 = 4, 3)
위 두 가지에 걸리는 부분이 없다면 여우 사인은 완성된 것이다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# n_list = [[1, 3], [4, 3], [1, 4]] # Wa-pa-pa-pa-pa-pa-pow!
# n = 5
# n_list = [[1, 3], [3, 4], [4, 1], [1, 5], [5, 4]] # Woof-meow-tweet-squeek

if n <= 2 or n >= 4:
    print('Woof-meow-tweet-squeek')
    exit(0)

for i, j in n_list:
    if (i == 1 and j == 3) or (i == 3 and j == 1):
        continue
    elif (i == 1 and j == 4) or (i == 4 and j == 1):
        continue
    elif (i == 3 and j == 4) or (i == 4 and j == 3):
        continue
    else:
        print('Woof-meow-tweet-squeek')
        exit(0)

print('Wa-pa-pa-pa-pa-pa-pow!')
