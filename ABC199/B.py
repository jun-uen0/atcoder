# https://atcoder.jp/contests/abc199/tasks/abc199_b?lang=en

# N=int(input())
# A=list(map(int, input().split))

# print(N)
# print(A)

# import sys
# a=[]
# for i in sys.stdin.readline():
#   a.append(i)

# print(a)


# names = ['Jun', 'Anna', 'Cameron']
# ages = [27, 30 , 24]
# zipped = zip(names, ages)
# print(zipped) # <zip object at 0x10492ac80>
# print(list(zipped)) # [('Jun', 27), ('Anna', 30), ('Cameron', 24)]

# xy = [map(int, input().split()) for _ in range(2)]
# x, y = [list(i) for i in zip(*xy)]
# print(x)
# print(y)

import sys
a=[]
for i in sys.stdin:
  x,y=i.split()
  a.append((int(x),int(y)))

print(a)