# 백준 - 브론즈2 - 좋은 자동차 번호판 - 1871 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
 - 'LLL-DDDD' 형식으로 입력이 들어올 때 LLL과 DDDD를 '-'를 기준으로 split 한다.
 - 'DDDD' 형식의 부분을 int 형으로 바꾸고, temp라는 변수로 LLL을 계산한다.
    - 계산하는 방식으론 a의 글자를 반복하면서 각 글자에 26의 자리수 만큼 제곱하면 된다. 식은 다음과 같다.
    - ord([j] - 65) * 26 ** (len(a) - j - 1) for j in range(len(a)) -> 이 식을 sum 함수로 더해주면 된다.
 - temp와 DDDD를 비교해서 차이가 100 이하면 nice, 아니면 not nice를 출력한다.
'''

n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# n = 2
# n_list = ['ABC-0123', 'AAA-9999'] # nice  \  not nice

for i in n_list:
    a, b = i.split('-')
    b = int(b)
    temp = sum([(ord(a[j]) - 65) * 26 ** (len(a) - j - 1) for j in range(len(a))])

    if abs(temp - b) <= 100:
        print('nice')
    else:
        print('not nice')
