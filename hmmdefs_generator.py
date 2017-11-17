with open('monophones0', 'r+') as f:
	a = f.readlines()

with open('hmm0/proto', 'r+') as f:
	x = f.readlines()

additional = x[4:]

data = []
for b in a:
	ins = ''
	ins += '~h ' + b.strip() + '\n'
	ins += ''.join(additional)
	data.append(ins)

with open('hmmdefs', 'w+') as f:
	for b in data:
		f.write(b)

