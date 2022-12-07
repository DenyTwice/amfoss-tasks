def findSum(n):
    arr = list(map(int, str(n)))
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

num = int(input())
rounds = 0
while num > 9:
    num = findSum(num)
    rounds += 1

print(rounds)
