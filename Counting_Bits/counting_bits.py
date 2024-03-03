def getOneBits(n):
    collect = []

    while (n // 2) > 0 or n >= 1:
        collect.append(n % 2)
        n = n // 2

    print(collect)
    print(collect.count(1))

    for i in range(len(collect)):
        if collect[i] == 1:
            print(i + 1)


getOneBits(37)
