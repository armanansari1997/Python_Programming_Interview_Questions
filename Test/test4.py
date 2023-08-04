mynum = 104350
mylist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
newlist = list(str(mynum))
res = []
for num in newlist:
	res.append(mylist[int(num)])

print(''.join(res))
