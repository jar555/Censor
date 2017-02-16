def censor(message, word):
	x = message.split()
	blanked = ""
	#print(x)

	for i in range(0, len(word)):
		blanked += "*"

	for i in range(0, len(x)):
		if x[i] == word:
			x[i] = blanked

	newString = ' '.join(str(w) for w in x)
	print(newString)
	return newString
censor("hello world my name is hello", "hello")