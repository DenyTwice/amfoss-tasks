def findSum(n):
    lstN = list(map(int, str(n)))
    sum = 0
    for i in range(len(lstN)):
        sum += lstN[i]
    return sum

num = input()
rounds = 0
while int(num) > 9:
    num = findSum(num)
    rounds += 1
print(rounds)
