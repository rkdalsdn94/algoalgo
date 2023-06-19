# 백준 - 골드4 - 가장 긴 바이토닉 부분 수열 - 11054 - dp, 가장 긴 증가(감소)하는 부분 수열(LIS) 문제
'''
dp, 가장 긴 증가(감소)하는 부분 수열(LIS) 문제

LIS로 문제를 풀어야 된다는 감은 있었는데, 증가하는 수열과 감소하는 수열을 사용할 생각은 못했다.
그래서 다른 사람의 유튜브 풀이를 참고하고, 내 입맛대로 바꿔서 풀었다.
참고한 링크 주소는 https://www.youtube.com/watch?v=SEdX0CrOfCg 여기이다.

풀이 과정
 - 증가하는 수열과 감소하는 수열 두 개를 준비한 뒤 두 리스트의 합이 제일 큰 값을 출력하면 된다.
 - 단, 출력할 때 1을 빼고 출력해야 되는데, 이유는 증가하는 수의 제일 큰 수와 감소하는 수의 제일 큰 수와 동일하다.
 - 따라서, 중복된 값을 제거하기 위해 -1을 해야된다.
 - 문제에 있는 예제로 설명하면 1 5 2 1 4 3 4 5 2 1 이렇게 입력됐을 때 증가하는 수열에서 마지막 5와 감소하는 수열에서 처음 5의 값이 중복된다.
        - 증가하는 수열 : {1, 2, 3, 4, 5}
        - 감소하는 수열 : {5, 2, 1}
        - 5가 중복된다. 하나만 사용하기 위해 -1을 해야된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 10
# n_list = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1] # 7

reverse_n_list = n_list[::-1]
increase = [1] * (n) # 증가하는 부분 수열을 위한
decrease = [1] * (n) # 감소하는 부분 수열을 위한 (n_list를 뒤에서 부터 검사해야 된다. for n-1 로 구하던가 revers를 이용해야 된다.)
res = 0 # 정답을 출력하기 위한

for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_n_list[i] > reverse_n_list[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

decrease.reverse()
for i in range(n):
    res = max(res, increase[i] + decrease[i])

print(res - 1)
