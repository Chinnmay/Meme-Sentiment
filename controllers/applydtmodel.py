import numpy as np
import pandas as pd
import pickle

def genrules():
    #Genreated 1728 Rules!!! Happy Tracing
    personality=[1,-1,0]
    text_sent=[1,-1,0,9]
    face_sent=[1,-1,0,9]
    whoistalking=[1,0,9]
    aboutwhom=[1,0,9]
    about_whom_detail=[1,-1,0,9]
    sameparty=[2]

    map1={1:'+ve',-1:'-ve',0:'nt',9:'unk'}
    map2={1:'Self',0:'oth',9:'unk'}
    map3={2:'No'}


    loaded_model = pickle.load(open('controllers/models/balancedrf2', 'rb'))
    pred=-999
    count=0
    #shit code dont judge

    for i1 in personality:
        for i2 in text_sent:
            for i3 in face_sent:
                for i4 in whoistalking:
                    for i5 in aboutwhom:
                        for i6 in about_whom_detail:
                            for i7 in sameparty:
                                pred=loaded_model.predict(np.array([[i1,i2,i3,i4,i5,i6,i7]]))[0]
                                if pred==1:
                                    pred='+ve'
                                elif pred==-1:
                                    pred='-ve'
                                loaded_model.predict_proba(np.array([[i1,i2,i3,i4,i5,i6,i7]]))[0]   #to get probablities of class variables for all rules
                                print('Psnlty:',map1[i1],' ,TSent:',map1[i2],' ,Fsent:',map1[i3],' , WisT:',map2[i4],' , AbtWhm:',map2[i5],' , AbtWhmDet:',map1[i6],' , SP:',map3[i7],'->','Ovl Snt:',pred)
                            count=count+1
    print(count)


def predict_overall(who_is_talking, about_whom, about_whom_detail, text_sentiment, same_party, face_sentiment, personality_status):

    negative_list = ['sad' , 'disgust' , 'fear' , 'anger' , 'angry']
    positive_list = ['happy' , 'surprise']
    neutral_list = ['neutral']

    # print("Text Sentiment" , text_sentiment)
    text_sentiment = text_sentiment.split(" :")[0]
    try:
        if text_sentiment in negative_list:
            text_sentiment = -1
        elif text_sentiment in positive_list:
            text_sentiment = 1
        elif text_sentiment == "Neutral" or text_sentiment == "neutral":
            text_sentiment = 0
        else:
            text_sentiment = 9
    except:
        print("Error")
        text_sentiment = 9
    #--------------------------------------------------------

    try:
        if face_sentiment[0].lower() in negative_list:
            face_sentiment = -1
        elif face_sentiment[0].lower() in positive_list:
            face_sentiment = 1
        elif face_sentiment[0].lower() in neutral_list:
            face_sentiment = 0
        else:
            face_sentiment = 9
    except:
    	face_sentiment = 9
    #--------------------------------------------------------

    if who_is_talking != 0 and who_is_talking != 1:
        who_is_talking = 9

    if about_whom != 0 and about_whom != 1:
        about_whom = 9

    if about_whom_detail == 2:
        about_whom_detail = 9

    var_list = [personality_status, text_sentiment, face_sentiment, who_is_talking, about_whom, about_whom_detail, same_party]
    print("-----------Parameters-----------------\n" , var_list)
    # return var_list
    return predict(var_list)


def predict(l):
    loaded_model=pickle.load(open('controllers/models/balancedrf2','rb'))
    pred=loaded_model.predict(np.array([l]))[0]
    # if pred==1:
    #     pred='Positive'
    # elif pred==-1:
    #     pred='Negative'
    probspercent=loaded_model.predict_proba(np.array([l]))[0]*100
    print("Pred : " , pred)
    return pred

'''
val,probs=predict([0,1,1,1,1,0,2])
print(val)
print(probs)
'''

#genrules()
