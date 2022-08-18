'''
백 트래킹, 완전 탐색, 조합 문제

백 트래킹을 이용해 조합하는 문제이다.
백 트래킹을 잘 모른다면 여기 블로그를 참고해보면 좋을거 같다 https://gamedevlog.tistory.com/49

back_tracking 함수 안에서 cnt가 입력받은 l과 같다면
 - 모음의 수와 자음의 수를 확인한 후에 출력한다.

back_tracking 함수 안에서 cnt가 입력받은 l과 같지 않으면
 - 함수 인자로 받은 idx_cnt에서 ~ c번 까지 반복하면서 l까지의 수를 res에 append한다.
    ㄴ> 이 부분이 없으면 무한루프에 빠진다.
 - 후에 재귀로 위의 과정을 반복한다.

'각 줄에 하나씩, -사전식-으로 가능성 있는 암호를 모두 출력한다.'라는 부분을 놓치고 몇 번 틀린 후에
정렬을 한 후에 해결했다..

in
    4 6
    a t c i s w
out
    acis
    acit
    aciw
    acst
    acsw
    actw
    aist
    aisw
    aitw
    astw
    cist
    cisw
    citw
    istw
'''

# l, c = map(int, input().split())
# word = sorted(list(map(str, input().split())))

# 테스트
l, c, word = 4, 6, sorted(['a', 't', 'c', 'i', 's', 'w'])

res = []

def back_tracking(idx_cnt, cnt):
    if cnt == l:
        vowels, consonants = 0, 0

        for i in range(l):
            if res[i] in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonants += 1

        if vowels >= 1 and consonants >= 2:
            print(''.join(res))

        return

    for i in range(idx_cnt, c):
        res.append(word[i])
        back_tracking(i + 1, cnt + 1)
        res.pop()

back_tracking(0, 0)
