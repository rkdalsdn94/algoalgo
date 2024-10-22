# 백준 - 브론즈1 - 이제는 더 이상 물러날 곳이 없다 - 30455 - 애드 훅, 게임 이론 문제
'''
애드 훅, 게임 이론 문제

브론즈1 보다도 더 쉬운 문제이다.

풀이 과정
    1. n을 입력받는다.
    2. n이 짝수면 Duck을 출력하고, 홀수면 Goose를 출력한다.
'''

n = int(input())

# 테스트
# n = 3 # Goose
# n = 4 # Duck
# n = 7 # Goose

if n % 2 == 0:
    print("Duck")
else:
    print("Goose")
