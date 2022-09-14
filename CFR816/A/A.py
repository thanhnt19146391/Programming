
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        print(0)
        continue
    else:
        if (m > n):
            m, n = n, m
        print(n + 2 * m - 2)
