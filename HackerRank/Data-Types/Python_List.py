#Consider a list (list = []). You can perform the following commands:
#
#    insert i e: Insert integer  at position .
#    print: Print the list.
#    remove e: Delete the first occurrence of integer .
#    append e: Insert integer  at the end of the list.
#    sort: Sort the list.
#    pop: Pop the last element from the list.
#    reverse: Reverse the list.


if __name__ == '__main__':
	N = int(input())
	list= []
	for i in range(0,N):
		toDo = input().split()
		command = toDo[0]
		if(command == "insert"):
			i = int(toDo[1])
			e = int(toDo[2])
			list.insert(i,e)	
		elif(command == "print"):
			print(list)
		elif(command == "remove"):
			e= int(toDo[1])
			list.remove(e)
		elif(command == "append"):
			e = int(toDo[1]) 
			list.append(e)
		elif(command == "sort"):
			list.sort()
		elif(command == "reverse"):
			list.reverse()
		elif(command == "pop"):
			list.pop()

