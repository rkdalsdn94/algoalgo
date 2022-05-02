'''
완전 탐색 (브루트 포스) 문제

처음 계산식으로 풀려고 시도 했는데, 도저히 생각이 안나서 일일히 다 탐색하는 방식으로 만들었다.
(문제 제일 하단에 알고리즘 분류에서 브루트포스 알고리즘이라고 적혀 있기도 했다....)

0 ≤ N ≤ 500,000 n의 조건이 이렇게 되어 있다.
힌트에서 보면 '예제 1의 경우 5455++ 또는 5459--' 이렇게 되어 있어서
더하기, 빼기 두 경우 모두 생각해야 되므로 50만의 2배 만큼 반복문을 돌리고
고장난 버튼이 있을 경우 무시, 번호를 누를수 있는 경우엔 min값 비교 후 계산 하는 방식으로 풀었다.
'''

n = int(input())
button_num = int(input())
if button_num: button_list = list(map(int, input().split()))
else: button_list = []

# 테스트
# n = 5457
# button_num = 3
# button_list = [6, 7, 8] # 6
# n = 100
# button_num = 5
# button_list = [0,1,2,3,4] # 0
# n = 500000
# button_num = 8
# button_list = [0,2,3,4,6,7,8,9]
# n = 100
# button_num = 3
# button_list = [1,0,5] # 0
# n = 14124
# button_num = 0
# button_list = [] # 5
# n = 1
# button_num = 9
# button_list = [1,2,3,4,5,6,7,8,9]
# n = 80000
# button_num= 2
# button_list = [8,9] # 2228

res = abs(100 - n)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in button_list:
            break
        elif j == len(i) - 1:
            res = min(res, abs(int(i) - n) + len(i))

print(res)
