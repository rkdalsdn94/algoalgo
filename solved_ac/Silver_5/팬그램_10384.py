# 백준 - 실버5 - 팬그램 - 10384 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
- 테스트 케이스(t) 만큼 입력을 받으면서 다음의 과정을 계산한다.
- 입력이 들어오는 단어(word)를 띄어쓰기를 빈칸으로 만들고, 모든 문자를 소문자로 만든다.
    - replace, lower
- 위 과정을 통해 모든 문자가 띄어쓰기 없이, 소문자로 만든 상태에서 한 글자씩 꺼낸다.
    - 해당 글자가 알파벳에 속하면 alpha_num 인덱스의 1을 더한다.
- 위 과정을 다 마무리 한 뒤, alpha_num의 min 값을 res에 담고, res의 값에 따라 다음과 같이 출력한다.
    - res가 0 일 때 : Not a pangram
    - res가 1 일 때 : Pangram!
    - res가 2 일 때 : Double pangram!!
    - res가 3 일 때 : Triple pangram!!!
'''

t = int(input())
for i in range(1, t + 1):
    word = input().replace(' ', '').lower()
    alpha_num = [0] * 26

    for j in word:
        if j.isalpha():
            alpha_num[ord(j) - 97] += 1

    res = min(alpha_num)
    if res == 0:
        print(f'Case {i}: Not a pangram')
    elif res == 1:
        print(f'Case {i}: Pangram!')
    elif res == 2:
        print(f'Case {i}: Double pangram!!')
    elif res == 3:
        print(f'Case {i}: Triple pangram!!!')
