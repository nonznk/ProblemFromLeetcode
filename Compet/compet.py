def getPotentialOfWinner(potential, k):
    count = 0
    win = []

    for i in range(len(potential)):
        if potential[i - 1] > potential[i]:
            potential.remove(potential[i])
            potential.append(potential[i])
            win.append(potential[i - 1])
        else:
            potential.remove(potential[i - 1])
            potential.append(potential[i - 1])
            win.append(potential[i])

        count += 1

        if count > 1 and count == k:
            if win[0] == win[1]:
                break
            else:
                count = 0

    return potential[0]


print(getPotentialOfWinner([1, 3, 2, 4, 5], 2))
