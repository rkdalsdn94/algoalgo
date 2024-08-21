# 백준 - 실버1 - URLs - 6324 - 문자열, 파싱, 많은 조건 분기, 정규 표현식 문제
'''
문자열, 파싱, 많은 조건 분기, 정규 표현식 문제

나중에 정규 표현식으로도 풀어보고 싶다.
입력 예제만 다 풀고, 25% 쯤에서 틀렸습니다가 계속 나왔다.
왜 틀린지 이해가 어려워 질문 계시판에서 가져온 다음의 예제를 통해 해결할 수 있었다.
    in
        1
        http://www.acmicpc.net/abc://def
    out
        URL #1
        Protocol = http
        Host     = www.acmicpc.net
        Port     = <default>
        Path     = abc://def
위 입력 예제의 마지막 Path 부분이 abc://def로 나와야 하는데 abcdef로 나왔다.
처음 temp 를 만들 때 '://'.join(url.split('://')[1:]) 이 부분이 없어서 틀린 것이었다.
이 부분을 수정하고 제출하니 통과되었다. 25% 쯤에서 틀린다면 위 경우를 생각해보자.

풀이 과정
    1. 입력을 받는다.
    2. url을 '://'을 기준으로 split하여 0번째 인덱스인 protocol을 구한다.
    3. temp를 만들어 '://'을 기준으로 split하여 1번째 인덱스인 host_port를 구한다.
        3.1. 이때 '://'.join()을 사용하여 '://'을 붙여줘야 한다.
    4. 위에서 구한 temp를 /를 기준으로 split하여 0번째 인덱스인 host_port를 다시 구한다.
    5. host_port의 길이가 2보다 크다면 host와 port를 구한다.
        5.1. host_port의 길이가 1이라면 host만 구하고, port를 default로 설정한다.
    6. temp의 길이가 2보다 크다면 path를 구한다.
        6.1. temp의 길이가 1이라면 path를 default로 설정한다.
    7. 출력 형식에 맞춰 출력한다.
'''

n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# n = 4
# n_list = [
#     'ftp://acm.baylor.edu:1234/pub/staff/mr-p',
#     'http://www.informatik.uni-ulm.de/acm',
#     'gopher://veryold.edu',
#     'http://www.acmicpc.net/abc://def'
# ]
'''
out
    URL #1
    Protocol = ftp
    Host     = acm.baylor.edu
    Port     = 1234
    Path     = pub/staff/mr-p

    URL #2
    Protocol = http
    Host     = www.informatik.uni-ulm.de
    Port     = <default>
    Path     = acm

    URL #3
    Protocol = gopher
    Host     = veryold.edu
    Port     = <default>
    Path     = <default>

    URL #4
    Protocol = http
    Host     = www.acmicpc.net
    Port     = <default>
    Path     = abc://def
'''

for idx, url in enumerate(n_list):
    protocol = url.split('://')[0]
    temp = '://'.join(url.split('://')[1:]) # '://'.join() 이 부분이 없으면 틀렸습니다.가 나온다.
    extra = temp.split('/')
    host_port = extra[0].split(':')

    if len(host_port) > 1:
        host, port = host_port
    else:
        host, port = ''.join(host_port), '<default>'

    if len(extra) > 1:
        path = '/'.join(extra[1:])
    else:
        path = '<default>'

    print(f'URL #{idx + 1}')
    print('Protocol = %s' % protocol)
    print('Host     = %s' % host)
    print('Port     = %s' % port)
    print('Path     = %s' % path)
    print()
