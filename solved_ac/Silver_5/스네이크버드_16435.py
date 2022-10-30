# 백준 - 실버5 - 스네이크버드 - 16435 - 정렬, 그리디 문제
'''
정렬, 그리디 문제

풀이 과정
1. 입력받은 과일의 높이(h_list)가 현재 키(l) 보다 작거나 같은 위치에 있을 때마다 l을 1씩 증가한다.
2. l을 출력한다.

단순하게 그리디로 접근하면 금방 풀 수 있다.
'''

n, l = map(int, input().split())
h_list = sorted(list(map(int, input().split())))

# 테스트
# n, l = 3, 10
# h_list = sorted([10,11,13]) # 12
# n, l = 9, 1
# h_list = sorted([9,5,8,1,3,2,7,6,4]) # 10

for i in h_list:
    if i <= l:
        l += 1

print(l)
