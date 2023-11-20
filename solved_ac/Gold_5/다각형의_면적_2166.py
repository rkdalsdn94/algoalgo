# 백준 - 골드5 - 다각형의 면적 - 2166 - 수학, 다각형의 넓이 문제
'''
수학, 다각형의 넓이 문제

다른 사람들의 풀이와 비슷하듯이 아래 링크를 통해 답을 쉽게 구할 수 있었다. (파트3 부터 보면 됨)
  - "https://ko.wikihow.com/다각형-넓이-구하기#:~:text=정다각형의 넓이를 구,의 중심으로 모이는 선분"

'위 링크 파트3'에서 나온 공식대로 풀면 된다.
단, 두 가지 주의할 점이 있다.
 1. 문제에서 '소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력' 이라는 부분이 있으므로 둘째 자리에서 반올림 처리를 해야 하낟.
      - round 함수 2 번째 인자로 1을 줘서 둘째 자리에서 반올림 처리
 2. 정답이 음수로 나올 수 있으므로 절댓값 처리
      - 반올림을 처리하기 전 abs() 함수를 통해 절댓값 처리

in
    4
    0 0
    0 10
    10 10
    10 0
out
    100.0
'''

n = int(input())
x_list, y_list = [], []
x_res, y_res = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    x_list.append(a)
    y_list.append(b)
x_list.append(x_list[0])
y_list.append(y_list[0])

for i in range(n):
    x_res += x_list[i] * y_list[i + 1]
    y_res += y_list[i] * x_list[i + 1]

print(round(abs((x_res - y_res)) / 2, 1))
