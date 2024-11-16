s = input("Enter a String: ")
vc = 0
for i in s:
	if i in "aeiouAEIOU":
		vc += 1
print("No. of Vowels: ", vc)