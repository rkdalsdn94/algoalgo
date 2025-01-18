# 백준 - 실버4 - 페이지 세기 - 4821 - 구현, 문자열, 파싱 문제
'''
구현, 문자열, 파싱 문제

핵심 아이디어
  1. 페이지 범위를 표시하기 위해 배열을 사용하여 각 페이지의 인쇄 여부를 표시한다.
  2. 입력된 페이지 범위를 파싱하여 단일 페이지와 범위를 구분하여 처리한다.
  3. 페이지 범위가 문서의 전체 페이지 수를 벗어나는 경우, 유효한 범위만 처리한다.

풀이 과정
  1. 전체 페이지 수만큼의 크기를 가진 배열을 생성하여 각 페이지의 인쇄 여부를 0으로 초기화한다.
  2. 입력받은 문자열을 콤마(,)를 기준으로 분리하여 각 페이지 범위를 처리한다.
  3. 각 범위에 대해:
     - 하이픈(-)이 있는 경우: 시작 페이지(low)와 끝 페이지(high)를 구분하여 처리
     - 하이픈이 없는 경우: 단일 페이지로 처리하되, 유효한 범위인지 확인
  4. 페이지 범위가 유효한 경우(low가 high보다 작거나 같은 경우)에만 처리한다.
  5. 범위가 문서의 전체 페이지를 벗어나는 경우, 유효한 범위로 조정한다.
  6. 최종적으로 인쇄해야 할 페이지의 총 개수를 계산하여 출력한다.

in
    30
    10-15,25-28,8-4,13-20,9,8-8
    19
    10-15,25-28,8-4,13-20,9,8-8
    0
out
    17
    12
'''

while 1:
    total_page = int(input())
    if total_page == 0:
        break

    page = input().split(',')
    res = [0] * (total_page + 1)
    for i in page:
        if '-' in i:
            low, high = map(int, i.split('-'))
        else:
            if 1<= int(i) <= total_page:
                res[int(i)] = 1
            continue

        if low > high or low > total_page:
            continue

        if low < 1:
            low = 1
        if high > total_page:
            high = total_page

        for j in range(low, high + 1):
            res[j] = 1

    print(sum(res))
