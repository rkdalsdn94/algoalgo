# 백준 - 실버2 - 과자 나눠주기 - 16401 - 이분 탐색, 매개 변수 탐색 문제
'''
이분 탐색, 매개 변수 탐색 문제

풀이 과정
1. start(0)와 end(과자의 길이중 가장 큰 값의 + 1)를 설정한다.
2. start와 end의 합의 2로 나눈 몫을 mid값으로 설정한다.
3. 모든 조카에게 같은 길이의 막대 과자를 나눠줄 수 없으면 0을 출력한다는 조건때문에 mid가 0일시 프로그램을 종료한다.
4. 과자 길이 list를 반복문으로 하나씩 꺼내서 과자 길이가 mid값보다 크다면 mid로 나눈 몫을 temp에 더해준다.
5. temp의 길이가 m보다 크거나 같은 경우 start를 mid + 1로 바꾸고, 작으면 end를 mid - 1 한다.
6. 최종 mid값을 출력한다.
'''

m, n = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# m, n = 3, 10
# n_list = [1,2,3,4,5,6,7,8,9,10] # 8
# m, n = 4, 3
# n_list = [10,10,15] # 7

start, end = 0, max(n_list) + 1

while start <= end:
    mid = (start + end) // 2
    temp = 0

    if mid == 0:
        print(0)
        exit(0)

    for i in n_list:
        if i >= mid:
            temp += (i // mid)
    
    if temp >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
