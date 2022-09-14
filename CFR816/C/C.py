import numpy as np

n, m = map(int, input().split())
a = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(m)]
a.insert(0, 0)
# print(a)
# print(query)


for q in query:
    i, x = q
    a[i] = x
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1]
        if a[i] != a[i - 1]:
            s[i] = s[i - 1] + 1
    res = 0
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            print(s[r] - s[l - 1])
            res += max(1, s[r] - s[l - 1])
    print(res)
    break