numG = int(input())
numS = list(map(int, input().split()))

cars, cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0, 0

for i in range(numG):
    if numS[i] == 1:
        cnt1 += 1
    elif numS[i] == 2:
        cnt2 += 1
    elif numS[i] == 3:
        cnt3 += 1
    else:
        cnt4 += 1

# one car for each group 4s
cars += cnt4
cnt4 = 0
#print("added", cars, "for cnt4")

#  group 1 and 3 in same car
while cnt1 >= 1 and cnt3 >= 1:
    cnt1 -= 1
    cnt3 -= 1
    cars += 1
    #print("added", cars, "after first while")
# 2 group 2s in same car
while cnt2 >= 2:
    cnt2 -= 2
    cars += 1
    #print("added", cars, "after second")

if cnt2 == 1 and cnt1 >= 2:
    cars += 1
    cnt2 = 0
    cnt1 -= 2
    #print("added", cars, "after first if")
if cnt2 == 1 and cnt1 == 1:
    cars += 1
    cnt2 = 0
    cnt1 -=1

if cnt1 != 0:
    cars += cnt1//4 + 1 
    #print("added", cars, "after second")

if cnt2 == 1:
    cars += 1
    cnt2 -= 1
    #print(cars, "for if for two")

if cnt3 != 0:
    cars += cnt3
    #print("added ", cars, "after last")
#print(cnt1, cnt2, cnt3, cnt4)
print(cars)