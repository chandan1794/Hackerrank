size_m = int(raw_input())
set_m = raw_input().split(" ")
set_m = set(map(int,set_m))

size_n = int(raw_input())
set_n = raw_input().split(" ")
set_n = set(map(int,set_n))

inter = set_m.intersection(set_n)
uni = set_m.union(set_n)

ans = uni.difference(inter)
temp = list(ans)
temp.sort()
for a in temp:
	print a
