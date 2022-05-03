if __name__ == '__main__':
  lst = list(map(int, input().split()))

a = [lst[0],lst[1]]
b = [lst[2],lst[3]]
c = [lst[4],lst[5]]

s = ((lst[0] - lst[4]) * (lst[3] - lst[5]) - (lst[2] - lst[4]) * (lst[1] - lst[5])) / 2

print(abs(s))