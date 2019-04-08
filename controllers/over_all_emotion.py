def overall_sentiment(who_is_talking, about_whom, about_who, text_sentiment, same_party, face_sentiment, personality_status):

	negative_list = ['sad' , 'disgust' , 'fear' , 'anger']
	positive_list = ['happy' , 'surprise' , 'neutral']

	try:
		if text_sentiment.lower() in negative_list:
			text_sentiment = -1
		elif text_sentiment.lower() in positive_list:
			text_sentiment = 1
	except:
		text_sentiment = 0		

	try:
		if face_sentiment[0].lower() in negative_list:
			face_sentiment = -1
		elif face_sentiment[0].lower() in positive_list:
			face_sentiment = 1
		else:
			face_sentiment = 0
	except:
		face_sentiment = 0

	print("who_is_talking", who_is_talking)
	print("about_whom", about_whom)
	print("about_who", about_who)
	print("text_sentiment",text_sentiment)
	print("same_party,",same_party)
	print("face_sentiment",face_sentiment)
	print("personality_status" , personality_status)
	''' personality status
		 positive 1
		negative -1
		neutral/unknown 0
	Text sentiment
		positive 1
		negative -1
	who is talking
		himself 1
		third person 0
	about whom
		himself 1
		other 0
	about who
		positive 1
		negative -1
		neutral 0
		unknown 2
	same party
		yes 1
		no 0
    face sentiment
    	positive 1
    	negative -1

	'''
	if personality_status == 0:
		if who_is_talking == 1:
			if about_whom == 1:
				if text_sentiment == -1:
					return -1
				elif text_sentiment == 1:
					return 1
				else:
					return "Error in text_sentiment"
			elif about_whom == 0:
				if text_sentiment == -1:
					if about_who == 1:
						return -1
					elif about_who == 0:
						return -1
					elif about_who == -1:
						return 1
					elif about_who == 2:
						return	-1
					else:
						return "Error in about_who"
				elif text_sentiment == 1:
					if about_who == 1:
						return 1
					elif about_who == 0:
						if same_party == 1:
							return 1
						elif same_party == 0:
							return -1
						else:
							return "Error at same_party"
					elif about_who == -1:
						return -1
					elif about_who == 2:
						return	1
					else:
						return "Error in about_who"
				else:
					return "Error at text_sentiment"
			else:
				return"Error at about_whom"
		elif who_is_talking == 0:
			if text_sentiment == -1:
				return -1
			elif text_sentiment == 1:
				if face_sentiment == 1:
					return 0
				elif face_sentiment == -1:
					return -1
				else:
					return "Error in face_sentiment"
			else:
				return "Error in text_sentiment"
		else:
			return "Error"
	elif personality_status == 1:
		if text_sentiment == -1:
			return -1
		elif text_sentiment == 1:
			return 1
		else:
			return "Error in text_sentiment"
	elif personality_status == -1:
		if who_is_talking == 1:
			return -1
		elif who_is_talking == 0:
			if text_sentiment == 1:
				return -1
			elif text_sentiment == -1:
				return 1
			else:
				return "Error in text_sentiment"
		else:
			return "Error"
	else:
		return "Error in personality_status"
	return "Error"

#sent = input("enter sentence:")
#who_is_talking = input("who_is_talking")
#about_whom  = input("about_whom")
#about_who = input("about_who")
#text_sentiment = input("text_sentiment")
#same_party = input("same_party")
#face_sentiment = input("face_sentiment")
#personality_status = input("personality_status")
#print(overall_sentiment(int(who_is_talking), int(about_whom), int(about_who), int(text_sentiment), int(same_party), int(face_sentiment), int(personality_status)))
