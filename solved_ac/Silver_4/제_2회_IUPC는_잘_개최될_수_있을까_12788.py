# 백준 - 실버4 - 제 2회 IUPC는 잘 개최될 수 있을까? - 12788 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

CTP 회원들이 갖고 있는 펜(n_list)의 수를 내림차순으로 정렬한 후, 총 필요한 펜의 수(total)를 구한다.
임시로 사용할 temp와 res 변수를 각각 0으로 초기화 한 뒤,
내림차순으로 정렬한 n_list의 값들을 하나 씩 꺼내서 temp에 더한다. 더할 때 temp가 total을 넘기면 break 한다.
만약, n_list를 다 반복해도 total을 넘기지 못할 수 있으므로 출력할 때에 if 문으로 분기 처리한 뒤에 출력하면 된다.
'''

n = int(input())
m, k = map(int, input().split())
n_list = sorted(list(map(int, input().split())), reverse=True)

# 테스트
# n = 7
# m, k = 36, 3
# n_list = sorted([9, 70, 15, 13, 19, 20, 11], reverse=True)

total = m * k
res = 0
temp = 0

for i in n_list:
    if total > temp:
        temp += i
        res += 1
    else:
        break

if total > temp:
    print('STRESS')
else:
    print(res)