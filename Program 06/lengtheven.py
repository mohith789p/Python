s = input("Enter a String: ").split()
for i in s:
	if len(i) %2 == 0:
		print(i)