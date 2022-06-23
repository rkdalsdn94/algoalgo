'''
구현, 정렬 문제

마지막 반복문 없이 제출하니까 예제만 통과한다.

lambda를 이용해서 금, 은, 동 순으로 정렬한 후 (내림차순을 위해 reverse를 했다)
첫 번째 반복문에서 인덱스를 찾고, 두 번째 반복문을 돌면서
k랑 같은 국가의 메달 수와 동일한 국가 있으면 어차피 공동 점수이므로 해당 인덱스를 찾자마자 + 1 후 출력하면 된다.

ex) 
1 3 0 0 --> 1등
3 0 0 2 --> 4등
4 0 2 0 --> 공동 2등
2 0 2 0 --> 공동 2등
위와 같은 조건에서 k가 2 였을 때 마지막 반복문에서 어떻게 될진 모르지만 0 2 0 이라는 메달을 획득한 국가의
i + 1 을 하면 된다.
'''

n, k = map(int, input().split())
k_list = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: (x[1], x[2], x[3]), reverse=True)

# 테스트
# n, k = 4, 3
# k_list = sorted([[1,1,2,0], [2,0,1,0], [3,0,1,0], [4,0,0,1]], key=lambda x: (x[1], x[2], x[3]), reverse=True) # 2
# n, k = 4, 2
# k_list = sorted([[1,3,0,0], [3,0,0,2], [4,0,2,0], [2,0,2,0]], key=lambda x: (x[1], x[2], x[3]), reverse=True) # 2

idx = 0

for i in range(len(k_list)):
    if k == k_list[i][0]:
        idx = i

for i in range(len(k_list)):
    if k_list[idx][1:] == k_list[i][1:]:
        print(i + 1)
        break
