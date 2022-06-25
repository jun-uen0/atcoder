# https://atcoder.jp/contests/abc199/tasks/abc199_a

# If A  2  +B  2  <C  2   holds, print Yes; otherwise, print No.

A,B,C=map(int, input().split())

if A**2+B**2<C**2:
  print("Yes")
else:
  print("No")
