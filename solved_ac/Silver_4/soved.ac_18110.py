# 백준 - 실버4 - solved.ac - 18110 - 구현, 수학, 정렬 문제
'''
구현, 수학, 정렬 문제

n의 15%를 절사 평균 값으로 둔다. -> trimmed_mean 변수
n_list를 정렬한 후 앞과 뒤에서 절사 평균의 범위에 속한 값을 제거한다.
나머지 원소들의 평균을 출력하면 된다.

단, python에서는 반올림을 구현하는 방식으로 '오사오입' 방식을 사용한다.
이 문제에서는 '사사오입' 방식이 필요해서 함수로 직접 구현하거나 + 0.0000001을 더한 뒤 round 함수를 사용하면 된다.
    사사오입, 오사오입 설명은 아래 링크를 통해 알아보자.
        - https://hleecaster.com/python-round/
        - https://blog.naver.com/noseoul1/221592047071
해당 문제에선 my_round 함수를 구현했다. (0.5를 더한 뒤 int로 형변환을 통해 내림을 한다.)

설명을 추가할 겸 새로운 방식으로 문제를 풀어봤다.
 - 새로 작성한 코드에선 '사사오입'을 구하는 방식을 0.0000001 을 더한 후 round 하는 방식으로 풀었다.
 - 개인적인 기준으론 기존 코드보다 가독성이 더 좋은거 같다.

in
    5
    1
    5
    5
    7
    8
out
    6
in
    10
    1
    13
    12
    15
    3
    16
    13
    12
    14
    15
out
    13
'''


# 새로 작성한 코드
import sys; input=sys.stdin.readline

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n = 5
# n_list = sorted([1, 5, 5, 7, 8]) # 6
# n = 10
# n_list = sorted([1, 13, 12, 15, 3, 16, 13, 12, 14, 15]) # 13

if n == 0:
    print(0)
    exit(0)

trimmed_mean = round((n * 0.15) + 0.0000001)
new_n_list = n_list[trimmed_mean:-trimmed_mean]

if trimmed_mean == 0:
    print(round(sum(n_list) / n) + 0.0000001)
    exit(0)

print(round(sum(new_n_list) / len(new_n_list) + 0.0000001))


'''
기존 코드
import sys; input=sys.stdin.readline

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n = 5
# n_list = sorted([1, 5, 5, 7, 8]) # 6
# n = 10
# n_list = sorted([1, 13, 12, 15, 3, 16, 13, 12, 14, 15]) # 13

def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

if n:
    trimmed_mean = my_round(n * 0.15)
    print(my_round(sum(n_list[trimmed_mean:-trimmed_mean] if trimmed_mean else n_list) / (n - 2 * trimmed_mean)))
else:
    print(0)
'''
