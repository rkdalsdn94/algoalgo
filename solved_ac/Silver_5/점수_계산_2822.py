# 백준 - 실버5 - 점수 계산 - 2822 - 단순 정렬 문제
'''
단순 정렬 문제

문제에 주어진 조건을 입력 받은 후 해당 5번째 까지의 인덱스 + 1 과 해당 합을 출력하면 된다.

풀이 과정
1. n_list 라는 이름으로 숫자 8 개를 입력 받는다.
2. temp 라는 이름의 리스트에 내림차순으로 정렬된 n_list의 수 5개를 담는다.
3. temp 의 총 합을 sum_score 라는 이름으로 값을 담고 나중에 출력할 때 사용한다.
4. temp 의 값을 하나씩 꺼내면서 해당 값이 n_list의 몇 번째 index 인지 계산한다.
    단, 해당 인덱스의 + 1한 상태로 res_index라는 변수에 값을 추가한다. -> 값을 추가할 때 문자열로 형 변환을 시켜야 된다.
5. res_index를 한 줄로 출력한다. -> 문자열로 형 변환을 시켰으므로 join 함수를 사용했다.
'''

n_list = [ int(input()) for _ in range(8) ]

# 테스트
# n_list = [ 20,30,50,48,33,66,0,64 ] # 261  \ 3 4 5 6 8
# n_list = [ 20,0,50,80,77,110,56,48 ] # 373  \ 3 4 5 6 7
# n_list = [ 20,30,50,80,110,11,0,85 ] # 355  \ 2 3 4 5 8

temp = sorted(n_list, reverse=True)[:5]
sum_score = sum(temp)
res_index = []

for i in temp:
    res_index.append(str(n_list.index(i) + 1))
res_index.sort()

print(sum_score)
print(' '.join(res_index))
