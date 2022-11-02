# 백준 - 골드5 - 4와 7 - 2877 - 구현, 수학 문제
'''
구현, 수학 문제

원래 2진수에서는
0 = '0'
1 = '1'
2 = '10'
3 = '11'
   .
   .
   . 
이렇게 동작한다.
아래 풀이 과정에도 적혀있듯이 위 상태에서 0을 4로 바꾸고 1을 7로 바꾸면 문제를 맞출 수 없다.
그래서, 입력받은 k를 + 1 한 상태에서 제일 첫 번째 글자를 자르면 된다.
 ㄴ> 파이썬에서 bin으로 진법을 바꾸면 앞에 0bxx 이런식으로 되기 때문에 총 3글자를 자르는 것이다.
 ㄴ> + 1 한 후 첫 번째 글자를 자르는게 이해가 잘 안된다면 예제 2를 보면 된다.
 ㄴ> 원래 2진법에서의 2는 10으로 표현한다.
 ㄴ> 그러나, 답은 7로 나와야 된다. (k + 1 값에서 첫 번째 글자를 자른 후 replace 하면 된다.)

풀이 과정
1. k를 2진수로 바꾼 후 replace 함수를 통해 0을 4로 1을 7로 바꾸면 된다.
    1.1 위 과정 중에 k를 + 1 한 상태에서 3글자를 잘라야 정확하게 동작한다.

'''

k = int(input())

# 테스트
# k = 1 # 4
# k = 2 # 7
# k = 3 # 44

res = bin(k + 1)[3:].replace('0', '4').replace('1', '7')

print(res)
