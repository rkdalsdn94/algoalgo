# 백준 - 트럭 - 13335 - 구현, 큐, 시뮬레이션 문제
'''
구현, 큐, 시뮬레이션 문제

프로그래머스의 '다리를 지나는 트럭' 이라는 문제랑 똑같은 문제이다.

풀이 과정
1. 현재 다리를 지나는 트럭을 확인하기 위해 temp_list 라는 이름을 가진 리스트 자료형 변수를 만든다.
2. 문제의 입력으로 주어지는 트럭의 무게를 하나씩 꺼내면서 for 반복문을 실행한다.
3. for 반복문 안 while 반복문으로 다리에 올려진 트럭이 없을 경우 (temp_list가 비어있을 경우) 트럭을 추가한다.
    3.1 - temp_list의 len이 다리의 수(w)와 같다면 temp_list의 첫 번째 트럭을 뺀다.
    3.2 - temp_list의 전체 합의 값이 다리의 최대하중 보다 크다면 시간(res)은 1 추가, temp_list엔 0을 추가한다.
    3.3 - 작다면 temp_list(다리를 지나고 있는 트럭)에 i 값을 추가하고, res에 1을 더한다.
4. 최종적으로 res를 출력할 때 전체 다리의 길이인 w를 더한 후 출력해야 된다.
'''

n, w, l = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, w, l = 4, 2, 10
# n_list = [7,4,5,6] # 8
# n, w, l = 1, 100, 100
# n_list = [10] # 101
# n, w, l = 10, 100, 100
# n_list = [10,10,10,10,10,10,10,10,10,10] # 110

res = 0
temp_list = []

for i in n_list:
    while 1:
        if not temp_list:
            temp_list.append(i)
            res += 1
            break
        elif len(temp_list) == w:
            temp_list.pop(0)
        else:
            if sum(temp_list) + i > l:
                res += 1
                temp_list.append(0)
            else:
                temp_list.append(i)
                res += 1
                break

print(res + w)
