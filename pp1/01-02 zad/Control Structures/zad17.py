p = 0
n = 0
for x in range(1, 51):
    if x % 2:
        n += x
    else:
        p += x

print( p, n)
