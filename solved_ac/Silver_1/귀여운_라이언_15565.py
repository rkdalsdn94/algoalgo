# 백준 - 귀여운 라이언 - 실버1 - 15565 - 투 포인터, 슬라이딩 윈도우 문제
'''
투 포인터, 슬라이딩 윈도우 문제

처음에 코드가 효율적이지 않아서 시간 초과가 나서 다시 수정했다. -> 시간 초과 코드는 제일 아래에 있음
다시 푼 방식은 비슷하지만(윈도우을 어떤식으로 활용할지는 비슷함) 조금 더 효율적으로 계산했다.

풀이 과정
1. left와 right를 0와 k - 1인 상태로 변수를 만든다.
2. 입력 값들을 다 입력받고, 인형들(n_list) 중 라이언 인형(1)이 나올때 temp에 해당 인덱스를 추가한다.
3. temp의 길이가 k보다 작으면 라이언 인형을 포함하는 연속된 인형들의 집합이 없는 것이라 -1을 출력하고 프로그램을 종료한다.
4. right 인덱스의 값이 temp의 끝까지 오면 while 문을 멈추고 res를 출력한다.
    4.1 끝까지 오지 않으면 left와 right를 하나씩 증가시켜 window의 범위를 바꾸고 다시 검사한다.
'''

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 10, 3
# n_list = [1,2,2,2,1,2,1,2,2,1] # 6
# n, k = 1, 1
# n_list = [2] # -1
# n, k = 4, 3
# n_list = [2,2,2,2] # -1

res = 10000000000000
temp = []
left, right = 0, k - 1

for i in range(n):
    if n_list[i] == 1:
        temp.append(i)

if len(temp) < k:
    print(-1)
    exit(0)

while 1:
    length = temp[right] - temp[left] + 1
    res = min(res, length)

    if right == len(temp) - 1:
        break

    left += 1
    right += 1

print(res)

'''
시간 초과 코드
n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 10, 3
# n_list = [1,2,2,2,1,2,1,2,2,1] # 6
# n, k = 1, 1
# n_list = [2] # -1
# n, k = 4, 3
# n_list = [2,2,2,2] # -1

res = 10000000000000
one_cnt = 0
temp = []
flag = False

for i in range(n):
    if n_list[i] == 1:
        temp.append(i)

if len(temp) < k:
    print(-1)
    exit(0)

for i in temp:
    one_cnt += 1

    if one_cnt >= k:
        res = min(len(n_list[temp[0]:temp[one_cnt - 1]]), res)
        one_cnt -= 1
        temp.pop(0)
        flag = True

print(res)
'''