numG = int(input())
numS = list(map(int, input().split()))
cars, cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0, 0

for i in range(len(numS)):
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
print("added", cars, "for cnt4")

#  group 1 and 3 in same car
while cnt1 > 0 and cnt3 > 0:
    cnt1 -= 1
    cnt3 -= 1
    cars += 1
    print("added", cars, "after first while")
# 2 group 2s in same car
while cnt2 > 1:
    cnt2 -= 2
    cars += 1
    print("added", cars, "after second")

if cnt2 == 1 and cnt1 >= 2:
    cars += 1
    cnt2 = 0
    cnt1 -= 2
    print("added", cars, "after first if")

if cnt1 != 0:
    cars += cnt1//4 + 1
    print("added", cars, "after second")

if cnt2 == 1:
    cars += 1
    cnt2 -= 1
    print(cars, "for if for two")

if cnt3 != 0:
    cars += cnt3
    print("added ", cars, "after last")
print(cnt1, cnt2, cnt3, cnt4)
print("final", cars)

"""
One morning, n groups of schoolchildren were waiting outside for their usual school bus, but as they were waiting they got a call saying that the school bus broke down on the way and can't pick them up today. Since there was a new year party going on they just couldn't afford to miss school that day, so they decided to ride an Uber to school. Each Uber car can carry utmost 4 children. We know that the i-th group consists of si friends (1 ≤ si ≤ 4), they decide to go together so as to save money as we all know how expensive ubers can get. What minimum number of cars will the children need if all members of each group should ride in the same Uber (one Uber can take more than 1 group assuming all children of the groups are present)?

Input Format

The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.

Constraints

1 ≤ n ≤ 105 1 ≤ si ≤ 4

Output Format

Print the single number — the minimum number of cars needed for all the children to reach the school.

Sample Input 0

5
1 2 4 3 3
Sample Output 0

4
Explanation 0

There are multiple ways for seating the children.
One such arrangement is as follows
first and second group enter 1 car.
third group consisting of 4 people enter 2nd car.
fourth group consisting of 3 people enter 3rd car.
fifth group consisting of 3 people enter 4th car. So in total the minimum number of cars is 4


algo 

get number of groups of schoolchildren
get number of students in each group
spilt into 3 counts:
    cnt1 = no(one student)
    cnt2 = no(two students)
    cnt3 = no(3 students)
    cnt4 = nno(4 students)
    while cnt1 != 0 or cnt3 != 0:
        cnt1 -= 1
        cnt3 -=1
        add one car
    while cnt2 > 1: 
        cnt2 -= 2
        add one car    
    add cnt4 cars
    
    cnt1 = ctn3.inpt - cnt1 and cnt3 = 0 or cnt3 = cnt1.inppt - cnt3 and cnt1 = 0
    or
    cnt1 = inpt // add two to cnt2 or cnt3 = inpt
    and 
    cnt2 = 1 or cnt2 = 0

    if cnt2 == 1 and cnt1 >= 2:
        add one car
        cnt2 = 0
        cnt1 -= 2
    
    if cnt1 != 0:
        add cnt1/4 + 1 cars 


    if cnt3 != 0:
        add cnt3 cars

"""