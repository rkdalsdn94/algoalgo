# 백준 - 실버4 - 행운의 티켓 - 1639 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

풀이 과정
1. 입력받은 문자를 숫자 리스트로 변경한다.
2. 리스트의 길이가 홀수면 -1을 하기 위해 len(s) % 2 를 빼준다.
3. 두 개의 while 문으로 완전 탐색을 시작한다.
    3.1 - 첫 번째 while 문은 리스트의 길이가 0보다 크면 계속 시작할 수 있게 만들고, 해당 while 문 안에선 idx, res를 각각 0으로 초기화한다.
    3.2 - 두 번째 while 문을 실행하고, 종료 조건으로는 위에서 정의한 idx와 length의 합이 s의 길이보다 작거나 같을때까지 반복한다.
        3.2.1 - 행운의 숫자인지 체크하기 위해 lucky_number_check 함수를 실행 시키고, 인자로는 idx 부터 idx와 length 를 더한 값을 준다.
            3.2.1.1 - 함수가 통과하면 최대 길이를 구하는 문제라 바로 해당 길이를 출력하고 종료시키면 된다.
            3.2.1.2 - 함수가 통과하지 못하면 idx는 1을 더하고, length는 2를 뺀다.
4. 이 과정을 첫 번째 while 문과 두 번째 while 문을 다 완료해도 프로그램이 종료되지 않으면 행운의 티켓을 찾을 수 없으므로 0을 출력하면 된다.

https://pythontutor.com/render.html#mode=display 이 사이트에서 아래 코드를 실행시켜보면 이해하는데 도움이 된다.
'''

s = list(map(int, list(input())))

# 테스트
# s = list(map(int, list('74233285'))) # 4
# s = list(map(int, list('123231'))) # 6
# s = list(map(int, list('986561517416921217551395112859219257312'))) # 36
# s = list(map(int, list('1'))) # 0
# s = list(map(int, list('112'))) # 2

def lucky_number_check(n):
    mid = len(n) // 2
    a, b = sum(n[:mid]), sum(n[mid:])
    if a == b:
        return True
    return False

res = 0
length = len(s) - len(s) % 2

while length > 0:
    idx, res = 0, 0

    while idx + length <= len(s):
        if lucky_number_check(s[idx: idx + length]):
            res = length
            print(res)
            exit(0)
        idx += 1
    length -= 2
print(res)
