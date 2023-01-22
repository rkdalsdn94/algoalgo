# 백준 - 숫자놀이 - 실버4 - 1755 - 수학, 문자열, 정렬 문제
'''
수학, 문자열, 정렬 문제

딕셔너리를 활용해서 해당 숫자를 문자열로 바꾼 후 temp에 담고, res 리스트는 현재 반복중인 i 숫자와 temp 글자를 같이 append 한다.
글자 기준으로 정렬을 진행한 후, 10개씩 숫자를 출력하면 된다.
'''

m, n = map(int, input().split())

# 테스트
# m, n = 8, 28

word = {
    '1':'one', '2':'two', '3':'three',
    '4':'four', '5':'five', '6':'six',
    '7':'seven', '8':'eight', '9':'nine',
    '0':'zero'
}

res = []

for i in range(m, n + 1):
    temp = ' '.join([word[j] for j in str(i) ])
    res.append([i, temp])

res.sort(key=lambda x: x[1])

for i in range(len(res)):
    if i % 10 == 0 and i != 0:
        print(sep = '\n')
    print(res[i][0], end=' ')
