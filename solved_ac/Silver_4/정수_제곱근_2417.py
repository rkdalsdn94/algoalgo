# 백준 - 실버4 - 정수 제곱근 - 2417 - 수학, 이진 탐색 문제
'''
수학, 이진 탐색 문진

제일 아래 단순하게 풀려다 실패한 코드와, 그 바로 위 decimal 모듈을 활용해서 푼 코드가 있다.
근데, 뭔가 아쉬워서 이진 탐색으로도 풀 수 있다고 해서 도전 해봤다.

풀이 과정.
1. n을 입력 받은 후, start와 end를 각각 0과 n + 1로 초기화한다.
2. 이진 탐색 진행을 위해 start가 end보다 커질때까지 while 문을 실행한다.
    2.1. start와 end를 더하고 2로 나눈 몫을 mid 값으로 대입한다.
    2.2. mid를 제곱 했을 때 n보다 작으면 start를 mid + 1한 값으로 바꿔주고, 크면 end를 mid - 1 한 값을 바꿔준다.
    2.3. 위 과정을 start가 end보다 커질때까지 반복한다.
3. start를 출력한다.
'''

n = int(input())

# 테스트
# n = 122333444455555 # 11060446

start, end = 0, n + 1

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)

'''
# 단순히 python 0.5를 제곱해서 쉽게? 구하려고 했는데, 정답이 안됐다. -> 제일 아래 코드
# 전에 해당 문제와 비슷한 프로그래머스 문제(Lv1 정수 제곱근 판별)에서도 헤맸던 기억이 나서, 해당 코드를 참고하고 제출했는데도 안됐다..
# 파이썬 부동 소수점 관련해서 찾다가 아래 링크를 참고해 decimal 이라는 파이썬의 소수점 연산을 더 정확하게 해주는 모듈을 사용해서 해결했다.
# decimal 이라는 모듈을 한 번도 안써봤는데, 이 기회에 사용해 볼 수 있어서 좋았다.

# 참고 링크
# https://docs.python.org/ko/3/tutorial/floatingpoint.html - 파이썬에서 부동 소수점 산술 문제점 및 한계에 관해
# https://docs.python.org/ko/3/library/decimal.html#module-decimal - decimal 모듈 설명


import decimal

n = int(input())
res = decimal.Decimal(str(n))

if res.sqrt() == int(res.sqrt()):
    print(int(res.sqrt()))
else:
    print(int(res.sqrt()) + 1)
'''




'''
완전 단순하게 풀려다가 실패한 코드..

# n = int(input())
n = 122333444455555 # 1106446

print(int(n ** 0.5) + 1)
'''