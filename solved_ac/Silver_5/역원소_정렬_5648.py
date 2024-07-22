# 백준 - 실버5 - 역원소 정렬 - 5648 - 정렬 문제
'''
정렬 문제

풀이 과정
 - 입력이 들어오면 입력받은 숫자를 뒤집어서 정렬 후 출력하면 되느 문제이다.
 - 단, 입력을 받을 때가 까다롭다. (이런 입력 문제는 처음 봤음)
 - 제일 첫 글자가 n이고, 나머지는 n 만큼 들어오는데, 방식을 알 수 없다.
    - 다음의 링크에 있는 질문 게시판의 글을 참고해서 풀 수 있었다.
        - https://www.acmicpc.net/board/view/86900
'''

import sys; input=sys.stdin.read

n, *res = input().split()

for i in range(int(n)):
    res[i] = int(res[i][::-1])

for i in sorted(res):
    print(i)
