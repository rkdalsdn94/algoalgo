# 백준 - 실버2 - 앵무새 - 14713 - 구현, 문자열, 자료 구조(큐) 문제
'''
구현, 문자열, 자료 구조(큐) 문제

n : 앵무새 수
n_list : 각 앵무새가 말한 문장
l : cseteram이 받아 적은 문장

리스트에서 0번째 인덱스에 값이 있는지 확인하면 되는 문제이다.
deque으로 popleft를 이용해서 풀면 시간이 좀 더 빠르게 되지만, 리스트의 pop(0)로 풀었다.

처음에 flag 부분이 없어서 9% 에서 '틀렸습니다.'가 나왔다. (9% 쯤에 틀렸습니다 나오면 flag를 추가)

풀이 과정
 1. n, n_list, l을 입력받는다.
 2. l의 각 단어를 하나씩 꺼내서 n_list의 단어와 비교한다.
 3. 만약 n_list의 단어와 l의 단어가 같다면 n_list의 단어를 pop(0)한다.
 4. 만약 n_list의 단어와 l의 단어가 다르다면 'Impossible'을 출력하고 종료한다.
    4.1. 이때 flag를 활용했다. (이 부분이 없다면 9%에서 틀린다.)
 5. 만약 n_list의 단어가 남아있다면 'Impossible'을 출력하고 종료한다.
 6. 여기까지 프로그램이 종료되지 않는다면 'Possible'을 출력한다.
'''

n = int(input())
n_list = [input().split() for _ in range(n)]
l = input().split()

# 테스트
# n = 3
# n_list = [
#     'i want to see you'.split(),
#     'next week'.split(),
#     'good luck'.split()
# ]
# l = 'i want next good luck week to see you'.split() # Possible
# n = 2
# n_list = [
#     'i found'.split(),
#     'an interesting cave'.split()
# ]
# l = 'i found an cave interesting'.split() # Impossible
# n = 2
# n_list = [
#     'please'.split(),
#     'be careful'.split()
# ]
# l = 'pen pineapple apple pen'.split() # Impossible

for i in l:
    flag = True

    for j in range(n):
        if n_list[j] and i == n_list[j][0]:
            n_list[j].pop(0)
            flag = False
            break

    if flag: # 9% 에서 틀린다면 이 부분을 확인해보자.
        print('Impossible')
        exit(0)

for i in n_list:
    if i:
        print('Impossible')
        exit(0)

print('Possible')
