'''
구현, 문자열 문제

우선 문제에서 종료 조건이 따로 없다.
그래서 while문 안에 try, expect(catch) 입력이 안들어오면 종료할 수 있게 했다.

문제는 문자열을 잘 다루면 된다. 조건은 어렵지 않다.
문자열에서 23:00 이런식으로 들어올때 ':'만 잘 제거하면 된다.
 ㄴ> 방법은 여러가지가 있는데, 본인이 편한걸로 사용하면 될거 같다.
 ㄴ> list로 입력받아서 remove도 사용해봤고, 슬라이싱을 이용해서도 해봤다.

조건은 학생이 입장하는 시간이 s보다 작거나 같으면 되고,
퇴장하는 시간은 종료 시간보다 크거나 같고 스트리밍(q) 시간보다 작거나 같으면 된다.
이때, ck에 있는 학생인지도 체크해야 된다.

in
    22:00 23:00 23:30
    21:30 malkoring
    21:33 tolelom
    21:34 minjae705
    21:35 hhan14
    21:36 dicohy27
    21:40 906bc
    23:00 906bc
    23:01 tolelom
    23:10 minjae705
    23:11 hhan14
    23:20 dicohy27
out
    5

in
    06:00 12:00 18:00
    06:00 shinyo17
    06:00 kimchist
    06:00 swoon
    06:00 kheee512
    06:00 Green55
    09:00 kimchist
    11:59 shinyo17
    12:00 kimchist
    17:59 swoon
    17:59 swoon
    18:00 kheee512
    18:01 swoon
    18:01 Green55
    18:01 kheee512
    18:01 swoon
    18:21 jinius36
    18:40 jeongyun1206
out
    3
'''
import sys; input = sys.stdin.readline

s, e, q = map(list, input().split())
s.remove(':'); e.remove(':'); q.remove(':')
s, e, q = int(''.join(s)), int(''.join(e)), int(''.join(q))
res = 0
ck = set()

while 1:
    try:
        time, student = input().split()
        time = int(time[:2] + time[3:])

        if s >= time:
            ck.add(student)
        elif e <= time <= q and student in ck:
            res += 1
            ck.remove(student)
    
    except:
        print(res)
        break
