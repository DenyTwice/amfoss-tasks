t = int(input())
for i in range(t):
    numTank = int(input())
    zroTanks = []
    tank = list(map(int,input().split()))
    for num, ltr in enumerate(tank):
        if ltr == 0:
            zroTanks.append(num)
            # print(f'{zroTanks}')
    for ltr in tank:
        if tank[ltr] > len(zroTanks) and zroTanks != []:
                for badTank in zroTanks:
                    tank[ltr] -= 1
                    tank[badTank] += 1
                    zroTanks.remove(badTank)
    tank.pop()
    operations = 0
    for x in tank:
        operations += int(x)
    print(operations)
