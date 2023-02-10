# 백준 - 브론즈3 - 열 개씩 끊어 출력하기 - 11721 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

입력으로 주어진 문자열을 10글자 씩 출력하는 간단한 문제이다.
'''

n = input()

# n = 'BaekjoonOnlineJudge' # BaekjoonOn  \  lineJudge
# n = 'OneTwoThreeFourFiveSixSevenEightNineTen' # OneTwoThre  \  eFourFiveS  \  ixSevenEig  \  htNineTen

for i in range(0, len(n), 10):
    print(n[i:i + 10])
