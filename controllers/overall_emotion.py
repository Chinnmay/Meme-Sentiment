def overall_sentiment(face_emotion, text_emotion):
	try:
	    face_emotion = face_emotion[0]
	except:
		return "no_Emotion"
	print("Face Emotions=====" , face_emotion)
	print("Text Emotions======" , text_emotion)
	if(face_emotion=='happy' and text_emotion=='anger'):
		return 'negative'
	elif(face_emotion=='happy' and text_emotion=='happy'):
		return 'negative'
	elif(face_emotion=='happy' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='happy' and text_emotion=='fear'):
		return 'negative'
	elif(face_emotion=='happy' and text_emotion=='disgust'):
		return 'negative'
	elif(face_emotion=='happy' and text_emotion=='surprise'):
		return 'positive'
	elif(face_emotion=='angry' and text_emotion=='anger'):
		return 'negative'
	elif(face_emotion=='angry' and text_emotion=='happy'):
		return 'positive'
	elif(face_emotion=='angry' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='angry' and text_emotion=='fear'):
		return 'negative'
	elif(face_emotion=='angry' and text_emotion=='disgust'):
		return 'negative'
	elif(face_emotion=='angry' and text_emotion=='surprise'):
		return 'negative'
	elif(face_emotion=='surprise' and text_emotion=='anger'):
		return 'negative'
	elif(face_emotion=='surprise' and text_emotion=='happy'):
		return 'positive'
	elif(face_emotion=='surprise' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='surprise' and text_emotion=='fear'):
		return 'negative'
	elif(face_emotion=='surprise' and text_emotion=='disgust'):
		return 'negative'
	elif(face_emotion=='surprise' and text_emotion=='surprise'):
		return 'positive'
	elif(face_emotion=='sad' and text_emotion=='anger'):
		return 'negative'
	elif(face_emotion=='sad' and text_emotion=='happy'):
		return 'positive'
	elif(face_emotion=='sad' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='sad' and text_emotion=='fear'):
		return 'negative'
	elif(face_emotion=='sad' and text_emotion=='disgust'):
		return 'negative'
	elif(face_emotion=='sad' and text_emotion=='surprise'):
		return 'negative'
	elif(face_emotion=='neutral' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='neutral' and text_emotion=='happy'):
		return 'positive'
	elif(face_emotion=='none' and text_emotion=='sad'):
		return 'negative'
	elif(face_emotion=='none' and text_emotion=='disgust'):
		return 'negative'
	elif(face_emotion=='none' and text_emotion=='happy'):
		return 'positive'
	elif(face_emotion=='none' and text_emotion=='fear'):
		return 'negative'
	elif(face_emotion=='none' and text_emotion=='surprise'):
		return 'positive'
	else:
		return 'no_Emotion'
