from collections import Counter

msg_crypto = ['B','B','B','B','B','B','B','U','D','D','D','D','D','D','T','A','G','G','G','U','U','U']

def listAlphabet():
  return list(map(chr, range(97, 123)))


from collections import Counter

msg_crypto = ['B','B','B','B','B','B','B','U','D','D','D','D','D','D','T','A','G','G','G','U','U','U']
print(Counter(msg_crypto).keys())


msg = []
for i in msg_crypto:
	if msg_crypto.count(i) == 1:
		msg.append(i)
print(msg)