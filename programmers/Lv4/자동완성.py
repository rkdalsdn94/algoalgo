# 프로그래머스 - Lv4 - 자동완성 - 문자열, 구현, 트라이 문제
"""
문자열, 구현, 트라이 문제

트라이를 구현하면 풀 수 있다는건 알았지만 잘 구현이 되지 않아.. 풀이를 참고해서 풀었다. 나중에 다시 풀어보려고 한다.

[핵심 아이디어]
    1. 트라이(Trie) 자료구조를 사용하여 단어들을 효율적으로 저장 및 검색
    2. 각 노드마다 해당 노드를 지나는 단어 수를 저장하여 중복 여부 판단
    3. 각 단어를 찾을 때 필요한 최소 입력 문자 수는 해당 단어가 유일하게 식별될 때까지의 글자 수
    4. 노드를 지나는 단어 수가 1개라면 더 이상 입력이 필요 없음(단어의 끝은 예외)

[풀이 과정]
    1. 트라이(Trie) 자료구조 구현:
       - 각 노드는 자식 노드들의 맵과 해당 노드를 지나는 단어 수 정보를 가짐
       - insert 메서드로 단어를 트라이에 삽입하며 지나는 경로의 모든 노드의 단어 수 증가
    2. 각 단어마다 필요한 입력 문자 수 계산:
       - 트라이를 따라가면서 현재 노드를 지나는 단어 수가 1이면 그 위치까지의 글자 수 반환
       - 단, 단어의 마지막 문자는 항상 입력해야 함(단어의 끝을 나타내기 위해)
       - 단어 끝까지 도달해야 한다면 전체 단어 길이 반환
    3. 모든 단어에 대한 필요 입력 문자 수의 합을 계산하여 반환
"""

class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드를 저장하는 딕셔너리
        self.word_count = 0  # 이 노드를 지나는 단어의 수

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """단어를 트라이에 삽입"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1  # 이 노드를 지나는 단어 수 증가

    def count_input_chars(self, word):
        """단어를 찾기 위해 입력해야 하는 문자 수 계산"""
        node = self.root
        count = 0

        for i, char in enumerate(word):
            node = node.children[char]
            count += 1

            # 이 노드를 지나는 단어가 1개뿐이라면 더 이상 입력할 필요 없음
            # 단, 단어의 마지막 문자는 제외 (단어의 끝을 나타내기 위해 입력 필요)
            if node.word_count == 1 and i < len(word) - 1:
                return count

        return count  # 전체 단어를 입력해야 하는 경우

def solution(words):
    trie = Trie()

    # 모든 단어를 트라이에 삽입
    for word in words:
        trie.insert(word)

    # 각 단어에 대해 입력해야 하는 문자 수 계산
    total_count = 0
    for word in words:
        total_count += trie.count_input_chars(word)

    return total_count

print(solution(["go", "gone", "guild"]) == 7)
print(solution(["abc", "def", "ghi", "jklm"]) == 4)
print(solution(["word", "war", "warrior", "world"]) == 15)
