# 백준 - 실버5 - 김인천씨의 식료품가게 (Large) - 12034 - 구현, 그리디 문제
'''
구현, 그리디 문제

문제에 있는 '각 품목의 판매 가격은 정상 가격의 정확히 75 %입니다.' 이 부분만 보고 문제를 풀어도 문제가 없다.
그리디 문제이므로 p_list로 입력받은 값을 하나 씩 꺼내서 0.75로 나눴을 때의 값이 p_list안에 있으면
해당 값을 p_list에서 제거하고, 앞서 꺼낸 p_num을 temp에 추가하면 된다.

출력할 때는 temp 리스트에 있는 값들을 띄어쓰기 기준으로 문자열로 만든 후, f스트링을 써서 출력했다.

in
    2
    3
    15 20 60 75 80 100
    4
    9 9 12 12 12 15 16 20
out
    Case #1: 15 60 75
    Case #2: 9 9 12 15
'''

t = int(input())

for cnt in range(1, t + 1):
    p = int(input())
    p_list = list(map(int, input().split()))
    temp = []
    
    while len(temp) != p:
        p_num = p_list.pop(0)
        
        if p_num // 0.75 in p_list:
            temp.append(p_num)
            p_list.remove(p_num // 0.75)
    
    res = ' '.join(map(str, temp))
    print(f'Case #{cnt}: {res}')