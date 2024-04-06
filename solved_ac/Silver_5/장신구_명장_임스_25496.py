# 백준 - 실버5 - 장신구 명장 임스 - 25496 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

단순히 정렬 후, 그리디하게 접근하면 되는 문제이다.

풀이 과정
 - 피로도(p)와 장신구의 개수(n)을 입력 받는다.
 - 장신구를 만들 때 드는 피로도(n_list)을 입력 받은 뒤 정렬한다.
 - 피로도가 200보다 작을 때 res를 1 더해주고, 피로도(p)에 장신구를 만들 때 드는 피로도를 더해준다.
 - 위 과정을 n_list의 크기만큼 반복한 뒤, res를 출력하면 된다.
'''

p, n = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# p, n = 190, 5
# n_list = sorted([20, 1, 8, 1, 10]) # 3
# p, n = 195, 4
# n_list = sorted([20, 1, 8, 1]) # 3

res = 0
for i in range(n):
    if p < 200:
        res += 1
        p += n_list[i]

print(res)
