def solution(s):
    s, zero_cnt, cnt = s.replace('0', ''), s.count('0'), 1
    # print(s, zero_cnt)
    while 1:
        if len(s) == 1:
            break
        temp = str(bin(len(s)))[2:]
        zero_cnt += temp.count('0')
        s = temp.replace('0', '')
        cnt += 1
    # print(cnt, zero_cnt)
    return [cnt, zero_cnt]
print(solution('110010101001')) # [3,8]
print(solution('01110')) # [3,3]
print(solution('1111111')) # [4,1]