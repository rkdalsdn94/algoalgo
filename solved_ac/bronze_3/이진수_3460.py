# 백준 - 브론즈3 - 이진수 - 3460 - 단순 구현 문제
'''
단순 구현 문제

테스트 케이스만큼 반복하면서 숫자를 입력받고 2진수로 바꾼다.(파이썬 내장함수 bin() 이용)
bin 함수의 반환 타입은 문자열이고, 앞의 두 글자는 0b가 와서 두 글자를 자르기 위해 리스트 슬라이싱을 이용했다.
역순으로 조회하면서 '1'이 나오면 해당 인덱스를 res에 추가한 후, res를 출력하면 된다.

in
    1
    13
out
    0 2 3
'''

t = int(input())

for _ in range(t):
    binary_num = bin(int(input()))[2:]
    res = []
    idx = 0

    for i in binary_num[::-1]:
        if i == '1':
            res.append(idx)
        idx += 1

    print(*res)
