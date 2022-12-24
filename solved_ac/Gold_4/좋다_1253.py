# 백준 - 골드4 - 좋다 - 1253 - 정렬, 이진 탐색, 투 포인터 문제
'''
정렬, 이진 탐색, 투 포인터 문제

solved 에서 문제 분류가 여러개로 되어 있는데, 내가 푼 방식은 정렬과 이진 탐색, 투 포인터가 핵심인거 같다.
해당 문제에선 while 문의 조건을 다른 투 포인터 문제들과 유사하게 풀었다가 한 번 틀렸다.
다른 문제들 처럼 while 문의 조건을 start <= end 이렇게 했다가 틀렸다.
문제에서 주어진 예제를 돌려보면 전체 반복문에서 두 번째 반복문 즉, i = 1 일때 mid의 값이 2가 되는 순간이 있다.
그래서, mid와 반복중인 n_list의 값이 같아서 res에 1이 더해졌다.
while 문의 조건을 아래 코드와 같이 start 가 end 보다 작을때 까지로 수정하면 잘 통과한다.

풀이 과정
1. input을 잘 입력 받는다.
2. n - 1만큼 0부터 1씩 커지게 반복하면서 temp에 해당 번째 인덱스를 제거한 리스트를 만들고
    start와 end을 각각 0과 temp 길이의 -1로 초기화한다.
3. start가 end보다 같거나 커지기 전까지 while 반복문을 실행한다.
    3.1. while 문 안에서 temp리스트의 start 인덱스와 end 인덱스를 더한 값으로 mid라는 변수에 담는다.
    3.2. mid 가 제일 바깥쪽 반복중인 n_list의 i번째 인덱스와 값이 같으면 res를 더한다.
        mid의 값이 n_list[i] 보다 작으면 start를 1더하고 while 문을 다시 실행한다.
        mid의 값이 n_list[i] 보다 크거나 같으면 end를 1빼고 while 문을 다시 실행한다.
4. res를 출력한다.
'''

n = int(input())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n = 10
# n_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] # 8

res = 0

for i in range(n):
    temp = n_list[:i] + n_list[i + 1:]
    start, end = 0, len(temp) - 1

    while start < end:
        mid = temp[start] + temp[end]

        if mid == n_list[i]:
            res += 1
            break
        if mid < n_list[i]:
            start += 1
        else:
            end -= 1
    
print(res)