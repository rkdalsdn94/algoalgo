# 백준 - 실버4 - 수강변경 - 23305 - 구현, 그리디 문제
'''
구현, 그리디 문제

처음 나이브하게 구현했을 때 시간 초과가 떴다.
그리디 알고리즘을 사용해야 된다는 것을 깨달았다.

풀이 과정
 1. a_list와 b_list를 입력받고, ck 리스트를 만든다. (ck를 입력 가능한 수업 번호의 최대 조건인 1_000_001 크기로 만들었다.)
 2. a_list의 단어를 하나씩 꺼내서 ck 리스트에 해당 인덱스 값을 1씩 더한다.
 3. b_list의 단어를 하나씩 꺼내서 ck에 인덱스 값이 0보다 크면 1씩 빼고, 0보다 작거나 같으면 res를 1씩 증가시킨다.
 4. res를 출력한다.
'''

for i in a_list:
    ck[i] += 1

for i in b_list:
    if ck[i] > 0:
        ck[i] -= 1
    else:
        res += 1

print(res)

'''
시간 초과 코드
n ** 2 이라서 시간 초과가 뜬다.

ck = [0] * n

for i in range(n):
    for j in range(n):
        if a_list[i] == b_list[j] and ck[j] == 0:
            ck[j] = 1
            break

print(ck.count(0))
'''
