def perm(word):
    if len(word) == 1:
        return [word]

    perms = perm(word[1:])
    a = word[0]
    res = []

    for x in perms:
        for k in range(len(x)+1):
            res.append(x[:k]+a+x[k:])

    return res

str = input()
print(perm(str))

