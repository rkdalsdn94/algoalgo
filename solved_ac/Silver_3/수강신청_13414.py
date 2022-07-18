'''
구현, 자료구조 문제

처음에 리스트로 풀려고하다가 계속 시간 초과가 나왔다.
딕셔너리를 활용해서 문제를 푸니까 통과할 수 있었다.

.rstrip()이 없으면 '출력 형식이 잘못되었습니다'라고 실패한다.
구현 + 자료 구조를 잘 활용해서 풀어야 되는 문제인거 같았다.
'''
import sys; input = sys.stdin.readline

# k, l = map(int, input().split())
# k_list = sorted({ input().rstrip(): i for i in range(l) }.items(), key=lambda x: x[1])[:k]
# print(k, l, k_list)

# 테스트
k, l = 3, 8
k_list = sorted({'20103324': 0, '20133221': 2, '20093778': 6,
          '20140101': 4, '01234567': 5, '20103325': 7}.items(), key=lambda x: x[1])[:k] # 20103324 \n 20133221 \n 20140101

for i in k_list:
    print(i[0])
