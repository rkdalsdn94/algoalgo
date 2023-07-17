# 백준 - 실버1 - 기타 레슨 - 2343 - 이진 탐색, 매개 변수 탐색 문제
'''
이진 탐색, 매개 변수 탐색 문제

처음 제출했을 때 50% 에러 틀렸습니다가 나왔다. 그래서 문제도 다시 보고 코드로 다시 봤는데, 어떤 부분이 문제일지 감이 잘 안 와 질문 게시판을 찾던 중
질문 게시판에서 어떤 분의 반례 모음집을 보고 어디가 틀렸는지 해결할 수 있었다. (반례 모음집 링크 - https://bingorithm.tistory.com/10)

mid 가 n_list의 max 값 보다 작으면 당연히 start를 더 크게 했어야 됐는데, 이 부분을 신경 쓰지 못했다.
이 부분을 추가한 뒤 해결할 수 있었다. (if 조건 분기 추가)

문제를 푸는 방법은 이진 탐색으로 풀면 된다. 단, bluelay의 크기를 조절해야 되므로 cnt와 temp를 같이 이용했다.
cnt는 이진 탐색의 범위를 위한 변수로 사용했고(m보다 크거나 작는 기준), temp는 블루레이의 크기를 위해 사용했다.
아래 적어논 두 예제로 한 단계씩 디버깅 하다보면 감이 온다.
'''

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, m = 9, 3
# n_list = [1,2,3,4,5,6,7,8,9] # 17
# n, m = 7, 6
# n_list = [100, 400, 300, 100, 500, 101, 400] # 500

res = sum(n_list)
start, end = 0, 10001 * n

while start <= end:
    mid = (start + end) // 2
    temp, cnt = 0, 1

    if mid < max(n_list): # 여기가 없으면 50% 에서 '틀렸습니다.'가 나온다.
        start = mid + 1
        continue

    for i in range(n):
        if temp + n_list[i] <= mid:
            temp += n_list[i]
        else:
            temp = n_list[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
        res = min(res, mid)
    else:
        start = mid + 1

print(res)

