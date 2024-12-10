def all_variants(n):
    i = 0
    while i in range(len(n)):
        yield n[i]
        i += 1
    i = 0
    while i in range(len(n)):
        yield n[i-1] +n[i]
        i += 1
    i = 0
    while i in range(len(n)):
        yield n[0:]
        i = n
a = all_variants('abcde')
for j in a:
    print(j)