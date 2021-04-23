from math import factorial as fac

n, m = map(int, input().split())  # 100 6
print(fac(n) // (fac(n-m) * fac(m))) # 1192052400