mystring = "kakkakakjr"
# for ch in mystring:
# 	if mystring.count(ch) == 1:
# 		print(ch)
# 		break

mydict = {}
for ch in mystring:
	mydict[ch] = mydict.get(ch, 0) + 1
print(mydict)

for k, v in mydict.items():
	if v == 1:
		print(k)
		break


