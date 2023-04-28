# 백준 - 실버1 - 개구리 - 23797 - 문자열, 그리디 문제
'''
문자열, 그리디 문제

입력으로 들어온 S 문자열을 한 글자씩 꺼내면서
'K'를 외쳤을 때 p_cnt의 값이 있다면 1을 빼주고(울음이 완성되는 것이므로)
반대로 'P'를 외쳤을 때 k_cnt의 값이 있다면 위와 똑같이 개구리 울음소리가 완성되는 것이므로 k_cnt의 값을 1빼야 한다.

S의 각 문자열에서 다음 글자로 넘어가기 전에 k_cnt, p_cnt, res 의 값 중 제일 큰 값을 res로 담아둔 후에 마지막 res를 출력하면 된다.
'''

s = input()

# 테스트
# s = 'KKPKPPKKKP' # 3

k_cnt, p_cnt, res = 0, 0, 0
for i in s:
    if i == 'K':
        k_cnt += 1

        if p_cnt: p_cnt -= 1
    else:
        p_cnt += 1

        if k_cnt: k_cnt -= 1

    res = max(res, k_cnt, p_cnt)

print(res)
