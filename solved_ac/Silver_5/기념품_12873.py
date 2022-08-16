'''
수학, 구현, 시뮬레이션 문제

문제 중에 
' (t단계인 경우에 t ** 3을 외칠 때 앞에 있던 사람) 사람이 제거된 후에는
백준이는 시계 방향으로 다음 사람에게 이동한다. '  라는 부분이 있다.

(idx + i ** 3 - 1) % len(user_list) -> 이 부분의 식만 구하면 푼제는 쉽게 풀 수 있다.

' 그 다음, 시계 방향으로 다음 사람에게 이동하며 "둘"을 외친다. '
위 부분을 구하기 위해 i를 1씩 증가되는 for문을 사용했다.
'''

n = int(input())

# 테스트
# n = 3 # 2
# n = 6 # 6
# n = 10 # 8

user_list = [ i for i in range(1, n + 1) ]
idx = 0

for i in range(1, n):
    idx = (idx + i ** 3 - 1) % len(user_list)
    user_list.pop(idx)
print(user_list[0])
