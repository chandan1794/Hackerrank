no_of_commands = int(raw_input())
ans_list=[]
for i in range(no_of_commands):
	command = raw_input().split(" ") #Make a list
	if(command[0] == "append"):
		ans_list.append(int(command[1]))
	elif(command[0] == "remove"):
		ans_list.remove(int(command[1]))
	elif(command[0] == "pop"):
		ans_list.pop()
	elif(command[0] == "count"):
		print ans_list.count(int(command[1]))
	elif(command[0] == "index"):
		print ans_list.index(int(command[1]))
	elif(command[0] == "sort"):
		ans_list.sort()
	elif(command[0] == "reverse"):
		ans_list.reverse()
	elif(command[0] == "insert"):
		ans_list.insert(int(command[1]),int(command[2]))
	else:
		print ans_list

