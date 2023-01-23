# 백준 - 실버4 - 3231 - 카드놀이 - 구현 문제
'''
구현 문제

풀이 과정.
1. input값들을 잘 입력받고 res는 0으로, 방문했는지 체크하기 위해 ck를 n + 1 크기의 0으로 된 리스트를 만들어준다.
2. n의 크기만큼 반복하면서 card_list의 i번째 인덱스의 값이 ck의 0이면 res를 추가하고 아니면 방문했다는 흔적만 남겨준다.
3. res를 1뺀 상태로 출력한다.
'''

n = int(input())
card_list = [ int(input()) for _ in range(n) ]

# 테스트
# n = 5
# card_list = [3,5,1,4,2] # 2
# n = 3
# card_list = [2,1,3] # 1
# n = 7
# card_list = [3,6,7,1,5,4,2] # 3

ck = [ 0 for _ in range(n + 1) ]
res = 0

for i in range(n):
    if ck[card_list[i] - 1] == 0:
        res += 1
        ck[card_list[i]] = 1
    else:
        ck[card_list[i]] = 1 

print(res - 1)
