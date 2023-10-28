# 백준 - 실버5 - 호텔 방 번호 - 5671 - 완전 탐색, 자료 구조(set) 문제
'''
완전 탐색, 자료 구조(set) 문제

풀이 과정
input의 종료 조건이 없으므로 try except 문을 통해 입력이 들어오지 않았을 때 break 하는 방식으로 입력을 받아야 된다.

한 숫자가 두 번 이상 들어있는지 검사는 len()을 통해 하면 된다.
n부터 m까지 한 숫자 씩 반복하면서 문자형으로 캐스팅 후, 해당 길이와 set을 통해 중복을 제거한 길이가 같다면
    같은 숫자가 들어온 경우가 없는 상황이므로 res에 1씩 더하고 이 과정을 m + 1 까지 반복한 뒤 res를 출력하면 된다.
'''

while 1:
    try:
        n, m = map(int, input().split())
        res = 0

        for i in range(n, m + 1):
            if len(str(i)) == len(set(str(i))):
                res += 1

        print(res)
    except:
        break
