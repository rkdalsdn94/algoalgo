# 백준 - 실버1 - 접두사 찾기 - 14426 - 문자열, 트리, 이분 탐색, 트라이 문제
'''
문자열, 트리, 이분 탐색, 트라이 문제

처음에는 startswith 함수와 for문을 사용해서 풀었는데 시간 초과가 나왔다.
그래서 트라이를 사용해 문제를 풀었다.

약간의 풀이 설명
 - 아래 코드는 크게 어렵진 않은 코드인데, 뭔가 복잡하다.
 - IDE나 에디터 같은 툴에서 디버그를 하면서 익숙해지는 방법이 제일 좋은거 같다.
 - 원래의 트라이라면 curr_node.data를 검사해야 하는데, 여기선 search 함수 내에서 for 문을 다 끝냈는데, False가 반환되지 않으면 통과한 것으로 간주한다.
'''

import sys; input=sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for char in string: # for 문 내에서 False를 반환하지 않으면 통과한 것으로 간주
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True

n, m = map(int, input().split())
n_list = [input().rstrip() for _ in range(n)]
m_list = [input().rstrip() for _ in range(m)]

# 테스트
# n, m = 5, 10
# n_list = ['baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh']
# m_list = ['baekjoon', 'star', 'start', 'code', 'sunday', 'coding', 'cod', 'online', 'judge', 'plus'] # 7

res = 0
trie = Trie()

for i in range(n):
    word = n_list[i]
    trie.insert(word)

for i in range(m):
    word = m_list[i]
    if trie.search(word):
        res += 1

print(res)
