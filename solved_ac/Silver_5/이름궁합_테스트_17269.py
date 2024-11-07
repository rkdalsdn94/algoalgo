# 백준 - 실버5 - 이름궁합 테스트 - 17269 - 문자열, 구현 문제
'''
문자열, 구현 문제

풀이 과정
    1. 이름의 길이  n과 m, 그리고 이름 a와 b를 입력받는다.
    2. 두 이름의 길이가 다를 경우, 짧은 이름의 길이가 길어진 이름과 같아질 때까지 짧은 이름의 마지막 글자를 반복하여 추가합니다.
    3. 두 이름을 번갈아가며 하나의 문자열로 합친다. (ex, a[i] + b[i] 순서로)
    4. 합쳐진 이름의 각 글자를 숫자로 변환다. 각 글자의 숫자는 name 리스트를 참고하여 매핑한다.
    5. 숫자로 변환된 리스트를 이용해 각 자리수를 더하는 과정을 반복하여 최종적으로 두 자리 숫자만 남긴다..
    6. 결과로 나온 두 자리 숫자를 퍼센트(%)로 출력하면 된다.
'''

n, m = map(int, input().split())
a, b = input().split()

# 테스트
# n, m = 8, 14
# a, b = 'LEESIYUN', 'MIYAWAKISAKURA' # 27%
# n, m = 2, 2
# a, b = 'AB', 'CD' # 77%
# n, m = 3, 2
# a, b = 'BOJ', 'IN' # 1%

name = [
    3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1
]

res = ''
min_len = min(n, m)
for i in range(min_len):
    res += a[i] + b[i]

if n > m:
    res += a[m:]
elif n < m:
    res += b[n:]

res = [name[ord(i) - ord('A')] for i in res]

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        res[j] += res[j + 1]

print(f'{res[0] % 10 * 10 + res[1] % 10}%')
