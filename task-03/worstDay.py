numG = int(input())
numS = list(map(int, input().split()))

cars, cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0, 0

cnt1 = numS.count(1)
cnt2 = numS.count(2)
cnt3 = numS.count(3)
cnt4 = numS.count(4)

cars += cnt4
cnt4 = 0

while cnt1 > 0 and cnt3 > 0:
    cnt1 -= 1
    cnt3 -= 1
    cars += 1

while cnt2 >= 2:
    cnt2 -= 2
    cars += 1

if cnt2 == 1 and cnt1 >= 2:
    cars += 1
    cnt2 -= 1
    cnt1 -= 2

if cnt2 == 1 and cnt1 == 1:
    cars += 1
    cnt2 = 0
    cnt1 -=1

if cnt1 != 0:
    cars += cnt1//4
    if cnt1 % 4 != 0:
        cars += 1

if cnt2 == 1:
    cars += 1
    cnt2 -= 1

if cnt3 != 0:
    cars += cnt3

print(cars)