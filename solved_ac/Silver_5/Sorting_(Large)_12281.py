# 백준 - 실버5 - Sorting (Large) - 12281 - 구현, 정렬 문제
'''
구현, 정렬 문제

풀이 과정
 1. 입력값을 받는다.
 2. 입력값을 리스트로 만든다.
 3. 홀수 리스트와 짝수 리스트를 만든다.
 4. 홀수 리스트는 오름차순, 짝수 리스트는 내림차순으로 정렬한다.
 5. 홀수 리스트와 짝수 리스트 각각 인덱스를 확인하기 위한 변수를 만든다.
 6. 처음 입력값 리스트를 확인하면서 짝수면 짝수 리스트에서, 홀수면 홀수 리스트에서 값을 가져와 결과 리스트에 넣는다.
 7. 출력 형식에 맞춰 결과 리스트를 출력한다.

in
    2
    5
    5 2 4 3 1
    7
    -5 -12 87 2 88 20 11
out
    Case #1: 1 4 2 3 5
    Case #2: -5 88 11 20 2 -12 87
'''

t = int(input())
for idx in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    odd_list = [] # 홀수 리스트
    even_list = [] # 짝수 리스트

    for i in n_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
        
    odd_list.sort()
    even_list.sort(reverse=True)

    odd_idx, even_idx = 0, 0
    res = []

    for i in n_list:
        if i % 2 == 0:
            res.append(even_list[even_idx])
            even_idx += 1
        else:
            res.append(odd_list[odd_idx])
            odd_idx += 1
    
    print(f'Case #{idx + 1}:', *res)
