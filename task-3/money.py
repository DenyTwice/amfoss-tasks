val = input().split()
# for i in [x for x in range(int(val[1])) if x % 2 == 0]:
mltpl = int(val[0])//int(val[1])
if mltpl % 2 != 0:
    mltpl = mltpl - 1
remain = int(val[1]) - (mltpl*int(val[0]))
if remain % int(val[1]) == 0:
    print((mltpl*int(val[0])+remain))
else:
    print(-1)
