'''
문제에서 주어진 요구사항을 차례대로 잘 실행하면 된다.
함수로 만들지 않아도 되는데, 뭔가 함수가 편할거 같아서 그렇게 했다.
처음에 숫자로 비교해서 10보다 작을때 비교하고 문자로 바꾸고 하려고 했는데,
매번 문자열로 캐스팅 하는거 보다 문자열로 비교하면서 다루다
int로 더하는게 더 편해서 문자열로 기준으로 코드를 작성했다.
'''

n = input()

# 테스트
# n = '26' # 4
# n = '0' # 1
# n = '1' # 60
# n = '71' # 12

def add_cycle(n):
    res = 0
    temp = n

    while 1:
        if n == '0':
            res += 1
            break

        if len(n) == 1:
            n = '0' + n
        
        add_temp = str(int(n[0]) + int(n[1]))
        n = n[-1] + add_temp[-1]
        res += 1
        if int(n) == int(temp):
            break

    return res

print(add_cycle(n))
