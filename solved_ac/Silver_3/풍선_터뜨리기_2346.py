# 백준 - 실버3 - 풍선 터뜨리기 - 2346 - 자료 구조(덱) 문제
'''
자료 구조(덱) 문제

전에 풀었던 '요세푸스 문제 0 - 11866'와 비슷하게 while 문으로 popleft 후 append 하는 방식으로 풀었었는데,
다른 사람의 풀이를 보고 이 방식이 훨씬 좋아보여 해당 방식으로 바꿨다. (deque.rorate 함수 활용하는 방식)

python deque 를 사용하면서 rotate 함수를 사용해본 적이 없는데, 이번 기회에 공부할 수 있었다.
    rotate 함수는 인자의 값으로 양수면 리스트의 값을 오른쪽으로 한 칸씩 미는 것이고, 음수면 왼쪽으로 한 칸씩 밀게 된다.
        예를 들어 다음과 같은 리스트가 있을 때 rotate 함수를 사용해보자.
        deque([1,2,3,4,5]) -> rotate(1) -> [5,1,2,3,4]
        deque([1,2,3,4,5]) -> rotate(-1) -> [2,3,4,5,1]
최종적으로 rotate를 활용해서 문제를 풀었다.

입력으로 들어오는 풍선 리스트를 rotate를 사용하기 위해 deque로 만들어 준다.
    - q로 만들 때 enumerate 함수를 이용해서 인덱스랑 같이 만들어준다.

인덱스와 값을 q에서 꺼내면서 값이
양수이면 왼쪽으로 1을 뺀 값을 rotate 시킨다.
    1을 빼는 이유는 처음 입력된 값이 빠지기 때문 즉, [3, 2, 1, -3, -1] 이렇게 있을 때 3이 빠지면 [2, 1, -3, -1] 이렇게 되니까 1을 빼야된다.
음수이면 오른쪽으로 rotate 시킨다. (오른쪽으로 rotate 시키기 위해 -을 붙여 양수로 만든다.)
'''

from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))

# n = 5
# q = deque(enumerate([3, 2, 1, -3, -1])) # 1 4 5 3 2

res = []

while q:
    idx, value = q.popleft()
    res.append(idx + 1)

    if value > 0:
        q.rotate(-(value - 1))
    else:
        q.rotate(-value)

print(*res)
