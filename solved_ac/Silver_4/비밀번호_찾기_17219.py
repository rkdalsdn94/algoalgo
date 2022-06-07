'''
자료 구조 문제

딕셔너리만 활용하면 금방 풀 수 있는 문제다.

in
    16 4
    noj.am IU
    acmicpc.net UAENA
    startlink.io THEKINGOD
    google.com ZEZE
    nate.com VOICEMAIL
    naver.com REDQUEEN
    daum.net MODERNTIMES
    utube.com BLACKOUT
    zum.com LASTFANTASY
    dreamwiz.com RAINDROP
    hanyang.ac.kr SOMEDAY
    dhlottery.co.kr BOO
    duksoo.hs.kr HAVANA
    hanyang-u.ms.kr OBLIVIATE
    yd.es.kr LOVEATTACK
    mcc.hanyang.ac.kr ADREAMER
    startlink.io
    acmicpc.net
    noj.am
    mcc.hanyang.ac.kr
out
    THEKINGOD
    UAENA
    IU
    ADREAMER
'''
n, m = map(int, input().split())
site_dict = {}

for _ in range(n):
    a, b = input().split(' ')
    site_dict[a] = b

for _ in range(m):
    a = input()
    print(site_dict[a])
