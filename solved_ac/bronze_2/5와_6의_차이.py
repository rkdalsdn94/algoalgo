'''
그리디 문제
문제를 단순하게 생각하면 된다.
5를 6으로 6을 5로 바꾼 후, 더한 값을 출력하면 된다
'''
a, b = input().split()

# 테스트
# a, b = '11', '25' # 36 37
# a, b = '1430', '4862' # 6282 6292
# a, b = '16796', '58786' # 74580 85582

six_temp_a = int(a.replace('5', '6'))
six_temp_b = int(b.replace('5', '6'))
five_temp_a = int(a.replace('6', '5'))
five_temp_b = int(b.replace('6', '5'))

print(five_temp_a + five_temp_b, six_temp_a + six_temp_b)
