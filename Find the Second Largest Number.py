N = input()
list_n = raw_input().split(" ")
list_n = [int(x) for x in list_n]

#for removing the duplicates converted it into a set
#and to access it by indexing convert it back to list
x = list(set(list_n))
x.sort() #sorting list in ascending order
if len(x) > 1:
	print x[-2] #using last second element
else:
	print x[0]	#for cases like where input is 1 1 1 then there will only
				#one element remain after set operation
