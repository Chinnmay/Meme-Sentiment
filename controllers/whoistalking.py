import nltk
#from nltk.stem import PorterStemmer
#porter = PorterStemmer()

def who_is_talking(text , person):
	#sent = nltk.sent_tokenize(text)
	#print(sent)
	text = text.lower()
	words = nltk.word_tokenize(text)
	#text = text.lower()
	tagged_words = nltk.pos_tag(words)
	#print(tagged_words)
	if(len(words)<5):
		length = len(words)
	else:
		length = 5
	for x in range(length):
		if words[x] == 'i':
			return(person , 1)
		if words[x] == 'am':
			return(person , 1)
		if words[x] == 'me':
			return(person , 1)


			'''for x in tagged_words:
		for p in person:
			if x[0] == p:
				print('person = ', person)
		if(x[1] == 'PRP'):
			print(x)
	text = text.lower()
	for x in tagged_words:
		if(x[1] == 'PRP'):
			print(x)'''
	return("third_person" , 0)
	#stem_sentence=[]
	##		stem_sentence.append(porter.stem(word))
	##	stem_sentence.append(" ")
	#print(stem_sentence)

#sent = input("enter sentence:")
#print(who_is_talking(sent , ['donald','trump']))
