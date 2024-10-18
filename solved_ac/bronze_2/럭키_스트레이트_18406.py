# 백준 - 브론즈2 - 럭키 스트레이트 - 18406 - 구현, 문자열 문제
'''
구현, 문자열 문제

문자열을 입력받아, 왼쪽 부분의 합과 오른쪽 부분의 합이 같으면 "LUCKY"를 출력하고, 그렇지 않으면 "READY"를 출력하는 문제이다.

풀이 과정
    1. n을 입력받는다.
    2. n의 길이를 구한다.
    3. n의 길이를 2로 나눈 몫을 구한다.
    4. n[:mid]의 합과 n[mid:]의 합이 같으면 "LUCKY"를 출력하고, 그렇지 않으면 "READY"를 출력한다.
'''

n = input()

# 테스트
# n = '123402' # LUCKY
# n = '7755' # READY

mid = len(n) // 2

if sum(map(int, n[:mid])) == sum(map(int, n[mid:])):
    print('LUCKY')
else:
    print('READY')
