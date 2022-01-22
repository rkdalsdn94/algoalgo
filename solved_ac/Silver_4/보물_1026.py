'''
a의 가장 낮은 숫자를 b의 가장 높은 숫자와 맞추면 될거 같다.
반환해야 되는 결과 값이 a의 리스트를 반환하는게 아니라서 b_list도 같이 조작하려 한다.
그래도 B를 재배열하지 말라고 하는데, 조작하는게 마음에 걸려 b_list를 수정하지 않는 방식으로 생각해 본다면
1. b_list를 복사한 배열을 하나 만들고,
2. b_list의 복사한 배열에서 가장 높은 값의 인덱스 정보를 a_list의 가장 낮은 값으로 맞춰가기
위와 같은 방식으로 풀 수 있을거 같다.
'''

n = int(input())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())), reverse=True)
# 테스트
# n = 5
# a_list = sorted([1,1,1,6,0])
# b_list = sorted([2,7,8,3,1], reverse=True) # 18
# n = 9
# a_list = sorted([5, 15, 100, 31, 39, 0, 0, 3, 26])
# b_list = sorted([11, 12, 13, 2, 3, 4, 5, 9, 1], reverse=True) # 528
res = 0

for i, j in zip(a_list, b_list):
    res += i * j

print(res)
