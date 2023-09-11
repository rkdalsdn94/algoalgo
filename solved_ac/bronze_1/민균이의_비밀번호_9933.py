# 백준 - 브론즈1 - 민균이의 비밀번호 - 9933 - 구현, 자료 구조(해시), 문자열 문제
'''
구현, 자료 구조(해시), 문자열 문제

문제의 분류엔 해시를 활용해서 풀 수 있다고 하는데, 단순한 구현과 문자열을 응용해서 풀었다.
다른 사람풀이에 해시를 활용한 부분을 봤는데, 딕셔너리로 글자의 수를 체크해서 2가 됐을 때 푸는 방식이였다. (팰린드롬 체크도 해야 됨)

아래 풀이는 다음과 같다.
비밀번호든 파일 목록을 미리 입력받고(word_list) new_i 라는 이름으로 문자열을 뒤집고, new_i 가 word_list에 있다면 반복문을 종료하고, 정답 형식에 맞춰 출력한다.
없다면, 팰린드롬 체크진행 했다. 펠린드롬이 이루어지면 반복문을 멈추고 정답 형식에 맞춰 출력했다.
'''

n = int(input())
word_list = [input() for _ in range(n)]

# 테스트
# n = 4
# word_list = ['las', 'god', 'psala', 'sal'] # 3 a
# n = 4
# word_list = ['kisik', 'ptq', 'tttrp', 'tulipan'] # 5 s
# n = 4
# word_list = ['abcdf', 'ptq', 'tttrp', 'fdcba'] # 5 c
# n = 4
# word_list = ['aabcbaa', 'ptq', 'tttrp', 'aaa'] # 7 c

res_len, res = 0, ''
for i in word_list:
    new_i = i[::-1]

    if new_i in word_list:
        res_len, res = len(new_i), new_i[len(new_i) // 2]
        break

    if i[len(i) // 2 + 1:] == i[:len(i) // 2 - 1]:
        res_len, res = len(new_i), new_i[len(new_i) // 2]
        break

print(res_len, res)
