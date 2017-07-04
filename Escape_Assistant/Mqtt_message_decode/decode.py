def de(msg_decode):
	str2 = ''
	i=0
	while i < len(msg_decode):
		if msg_decode[i] is '\\':
			if msg_decode[i+1] is 'n':
				str2 = str2+'\n'
				i=i+2
			elif msg_decode[i+1] is 't':
				str2 = str2+'\t'
				i=i+2
			else:
				i=i+1
		else:
			str2 = str2+msg_decode[i]
			i=i+1
	f = open('execute.py', 'w')
	f.write(str2)
	f.close()