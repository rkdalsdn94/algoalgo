# 백준 - 브론즈2 - Class Field Trip - 27386 - 단순 구현, 문자열, 정렬 문제
'''
단순 구현, 문자열, 정렬 문제

핵심 아이디어
    - ann과 ben의 이름을 합친 후 정렬하여 출력

풀이 과정
    1. ann과 ben의 이름을 입력받음
    2. ann과 ben의 이름을 합친 후 정렬하여 출력
    3. join 함수를 통해 리스트를 문자열로 변환하여 출력
'''

ann, ben = input(), input()

# 테스트
# ann, ben = 'ahjmnoy', 'acijjkll' # aachijjjkllmnoy

print(''.join(sorted(ann + ben)))
