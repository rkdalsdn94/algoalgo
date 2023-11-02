# 백준 - 골드4 - 오큰수 - 17298 - 자료 구조(스택) 문제
'''
자료 구조(스택) 문제

입력으로 들어오는 범위과 O(n^2 = 1,000,000 ** 2)이므로 이중 for 문을 이용해 풀면 시간 초과가 난다.
    수열 A의 크기 N (1 ≤ N ≤ 1,000,000)
    A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)

문제 분류의 스택이 들어가서 '스택을 이용해야겠다'라는 생각은 갖고 있지만 어떻게 활용해야 할 지 몰라서 꽤 헤맸다.
https://hooongs.tistory.com/329 여기 블로그의 풀이가 잘 되어 있어 참고하고 풀었다.
참고한 블로그를 활용하면 O(n) 의 복잡도를 가져서 시간안에 해결할 수 있다.
 - 위의 블로그를 참고해서 그런지 코드가 거의 비슷하다.

풀이 과정
 - res를 n의 범위만큼 -1로 초기화 한다.
 - idx로 사용하기 위해 for문으로 반복중인 i의 값과 n_list의 값을 stack의 append한다.
 - stack에서 이미 담겨있는 값(value)보다 큰 값(n_list[i])이 들어오면 해당 번째 res 인덱스를 n_list[i]의 값으로 바꿔준다.
 - 위 과정을 while문으로 반복한 뒤 res를 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
n = 4
n_list = [3, 5, 2, 7] # 5 7 7 -1
n = 4
n_list = [9, 5, 4, 8] # -1 8 8 -1

res = [-1] * n
stack = []

for i in range(n):
    while stack and stack[-1][-1] < n_list[i]:
        idx, value = stack.pop()
        res[idx] = n_list[i]
    stack.append([i, n_list[i]])

print(*res)
