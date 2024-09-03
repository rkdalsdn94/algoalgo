# 백준 - 실버2 - 패턴 - 17300 - 구현 문제
'''
구현 문제

문제가 잘 안 풀려서 다음의 블로그를 참고했다.
    - https://blog.naver.com/parkhj2416/221863824755 (자바로 되어 있음)
사실 위 블로그의 코드를 python으로 변경한 것 뿐인데, 설명이 너무 잘 되어 있어서 좋았다.
구현 문제에서 규칙을 찾는 것도 중요한 것 같다.

풀이 과정
    1. l을 입력받는다.
    2. l_list를 입력받는다.
    3. ck를 만들어 0으로 초기화한다.
    4. l_list를 돌면서 다음을 확인한다.
        4.1. ck[l_list[i]]를 방문(1)했거나 l이 3보다 작다면 NO를 출력하고 종료한다.
        4.2. ck[l_list[i]]를 방문했다는 표시를 위해 1로 바꾼다.
        4.3. i가 0이면 다음으로 넘어간다.
        4.4. mid를 구한다.
        4.5. l_list[i]가 짝수라면 l_list[i - 1]이 10 - l_list[i]와 같고 ck[mid]가 0이면 NO를 출력하고 종료한다.
        4.6. l_list[i - 1]이 홀수이고 ck[mid]가 0이고 l_list[i - 1]이 5가 아니고 l_list[i]가 5가 아니라면 NO를 출력하고 종료한다.
    5. 코드가 끝까지 돌았다면 YES를 출력한다.
'''

l = int(input())
l_list = list(map(int, input().split()))

# 테스트
# l = 4
# l_list = [1, 2, 3, 6] # YES
# l = 3
# l_list = [1, 3, 6] # NO
# l = 4
# l_list = [1, 9, 6, 5] # NO
# l = 5
# l_list = [1, 5, 9, 6, 5] # YES
# l = 5
# l_list = [1, 5, 9, 6, 5] # YES

ck = [0] * 10

for i in range(l):
    if ck[l_list[i]] or l <3:
        print('NO')
        exit(0)

    ck[l_list[i]] = 1
    if i == 0:
        continue

    mid = (l_list[i] + l_list[i - 1]) // 2
    if l_list[i] % 2 == 0:
        if l_list[i - 1] == 10 - l_list[i] and not ck[mid]:
            print('NO')
            exit(0)
    else:
        if l_list[i - 1] % 2 == 1 and ck[mid] == 0 and l_list[i - 1] != 5 and l_list[i] != 5:
            print('NO')
            exit(0)

print('YES')
