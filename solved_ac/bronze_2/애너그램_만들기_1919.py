# 백준 - 브론즈2 - 애너그램 만들기 - 1919 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

알파벳 소문자만 들어오니까 총 알파뱃의 길이로 리스트를 만든 후, 아스키 코드 값을 빼면서 해당 인덱스의 값을 더하고(a), 뺀다(b).
    - a 글자의 값은 더하고, b 글자의 값은 뺀다.
위와 같이 진행하고, list의 전체 값을 절댓값으로 만든 뒤 총 합을 출력하면 된다.
'''

a, b = input(), input()

# 테스트
# a, b = 'aabbcc', 'xxyybb' # 8

word_list = [0] * 26
for i in a:
    word_list[ord(i) - 97] += 1
for i in b:
    word_list[ord(i) - 97] -= 1

print(sum(map(abs, word_list)))
