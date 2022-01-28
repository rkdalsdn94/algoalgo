'''
    처음에 평소 푸는 습관대로
    n, taesu_score, p = map(int, input().split())
    p_list = list(map(int, input().split()))

    이런 식으로 인풋을 입력받고 시작했다가,
    제일 마지막 테스트케이스인 (0, 0, 50) 이 경우에서 에러가 났다.
    혼자 코드를 실행했을 땐 빈 리스트를 만들고 시작을 해서 에러가 안 났는데,
    문제를 보니까 n이 0이면 빈 리스트가 아니라 입력 정보가 들어오지 않는다..
    그래서 채점 결과 90% 이후에 '런타임 에러(EOFError)' 이렇게 나와 당황하면서 삽질을 좀 하다가
    n이 0 이였을 땐 바로 1등을 반환할 수 있도록 수정했다. ( 문제에서의 p 조건이 {10 <= p <= 50} 이여서 어떤 수라도 들어오면 랭킹 리스트에 올라갈 수 있다. )
'''

n, taesu_score, p = map(int, input().split())

# 테스트
# n, taesu_score, p = 3, 90, 10
# n, taesu_score, p = 10, 1, 10
# n, taesu_score, p = 10, 1, 10
# n, taesu_score, p = 0, 0, 50   # 1   (빈 리스트 만들면 안됨)

if n == 0:
    print(1)
else:
    p_list = list(map(int, input().split()))

    # 테스트리스트
    # p_list = [100, 90, 80] # 2
    # p_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # -1
    # p_list = [10, 9, 8, 7, 6, 5, 4, 3, 3, 0] # 10

    p_list.append(taesu_score)
    res = sorted(p_list, reverse=True).index(taesu_score) + 1

    if res > p or (n == p and p_list[-2] == taesu_score):
        print(-1)
    else:
        print(res)
