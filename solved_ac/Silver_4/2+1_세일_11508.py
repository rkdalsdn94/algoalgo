# 백준 - 실버4 - 2+1 세일 - 11508 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

다른 그리디 문제들과 비슷하게 역순으로 정렬 후 생각한 그대로 풀면 된다.

풀이 과정.
1. input을 입력받고 n_list를 역순으로 정렬한다. -> 'N개의 유제품을 모두 살 때 필요한 최소비용을 출력' 이 부분 때문에 역순으로 해야 된다.
2. n의 크기만큼(유제품의 수 만큼) 반복하면서 반복 횟수가 3의 배수일 때만 res에 더하지 말고, 나머진 res에 더한다.
3. res를 출력한다.
'''

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ], reverse=True)

# 테스트
# n = 4
# n_list = sorted([3,2,3,2], reverse=True) # 8
# n = 6
# n_list = sorted([6,4,5,5,5,5], reverse=True) # 21
# n = 7
# n_list = sorted([10, 9, 4, 2, 6, 4, 3], reverse=True)

res = 0

for i in range(n):
    if i % 3 != 2:
        res += n_list[i]

print(res)
