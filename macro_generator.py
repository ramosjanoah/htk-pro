total = ''
with open('hmm0/proto', 'r+') as f:
	a = f.readlines()

a = a[0:3]

with open('hmm0/vFloors', 'r+') as f:
	b = f.readlines()

with open('hmm0/macros', 'w+') as f:
	for x in a:
		f.write(x.strip())
		f.write('\n')
	for x in b:
		f.write(x.strip())
		f.write('\n')	