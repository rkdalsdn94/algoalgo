# 백준 - 실버5 - 팰린드롬 - 8892 - 문자열, 완전 탐색 문제
'''
문자열, 완전 탐색 문제

i랑 j가 서로 같은 값일 때는 빼야된다. 이 부분을 신경쓰지 못해서 틀렸다..
다른 사람들이 팰린드롬을 검사할 때 word == word[::-1] 이렇게 검사하기도 했다.
'팰린드롬 만들기-1213' 문제에서 상술한 방법을 사용한 적이 있는데, 직접 구현해보고 싶어서 아래처럼 만들어봤다.

전체적인 풀이는 테스트 케이스(t) 만큼 반복하면서 단어들을 입력받는다.
같은 단어가 아닌이상 (if i != j) 두 단어를 합친 후, 팰린드롬이 가능한 지 검사한다.
팰린드롬이면 합친 단어를 출력한 뒤 다음 테스트 케이스를 진행한다.
모든 word_list를 순회했는데도 팰린드롬을 완성하지 못하면 0을 출력한다.
'''

def palindrome_check(word):
    for i in range(1, (len(word) // 2) + 1):
        if word[i - 1] != word[-i]:
            return False
    return True

# # palindrome 테스트
# print(palindrome_check('aba')) # True
# print(palindrome_check('abba')) # True
# print(palindrome_check('abc')) # False

t = int(input())
for _ in range(t):
    k = int(input())
    word_list = [ input() for _ in range(k) ]
    flag = False

    for i in range(k):
        temp_word = word_list[i]

        for j in range(k):
            if i != j: # 이 조건을 까먹고 있다가 몇 번 틀렸다.
                two_sum_word = temp_word + word_list[j]

                if palindrome_check(two_sum_word):
                    print(two_sum_word)
                    flag = True
                    break
        if flag: break
    if not flag:
        print(0)
