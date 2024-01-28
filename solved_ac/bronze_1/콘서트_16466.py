# 백준 - 브론즈1 - 콘서트 - 16466 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

단순히 정렬한 뒤 n_list의 값 보다 더 작은 값을 찾는 구현 문제이다.
단, 조심해야 될 부분으로는 아래 테스트 중 마지막 예제 부분에서 n과 모든 숫자가 1부터 순서대로 5까지 있다면 6을 출력해야 된다.
    - 이 부분을 해결하기 위해 ck변수를 활용했다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 5
# n_list = sorted([4, 1, 2, 7, 8]) # 3
# n = 3
# n_list = sorted([7, 8, 9]) # 1
# n = 5
# n_list = sorted([1, 2, 3, 4, 5]) # 6

ck = True
for i in range(n):
    if (i + 1) != n_list[i]:
        print(i + 1)
        ck = False
        break

if ck:
    print(n + 1)
