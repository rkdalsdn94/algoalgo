'''
구현, 문자열 문제인거 같다.
시간을 분으로 바꾼 다음 계산하는게 훨씬 편한다.
'''

from math import ceil

def hour_to_minute(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []
    a, b, c, d = fees
    dic = dict()

    for i in records:
        time, number, history = i.split()
        number = int(number)
        
        if number in dic:
            dic[number].append([hour_to_minute(time), history])
        else:
            dic[number] = [[hour_to_minute(time), history]]

    # print(sorted(list(dic.items())))
    for i in sorted(list(dic.items())):
        t = 0

        for j in i[1]:
            if j[1] == "IN":
                t -= j[0]
            else:
                t += j[0]

        if i[1][-1][1] == "IN":
            t += hour_to_minute('23:59')

        if t <= a:
            answer.append(b)
        else:
            answer.append(b + ceil((t-a) / c) * d)

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) # [0, 591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"])) # [14841]