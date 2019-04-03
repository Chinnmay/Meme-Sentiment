import pandas as pd
personalities=pd.read_csv('./controllers/personality_score.csv')
#print(personalities)
positive_persons=personalities.iloc[:,0]
neutral_persons=personalities.iloc[:,1]
negative_persons=personalities.iloc[:,2]


positive_persons = [person for person in positive_persons if str(person) != 'nan']
neutral_persons = [person for person in neutral_persons if str(person) != 'nan']
negative_persons = [person for person in negative_persons if str(person) != 'nan']

trained_names=[]
for name in positive_persons:
    trained_names.append(name)
for name in negative_persons:
    trained_names.append(name)
for name in neutral_persons:
    trained_names.append(name)

#print(trained_names)

#about whom himself (1) or other (0)  if other then names
# about_who that is if other then
# 1 positive
# 2 inknown
# 0 neutral
# -1 negative


def personabout(face_name,text):
    persons=[]
    for word in text.split():
        for name in trained_names:
            #print(word.lower())
            #print(name.lower())
            if(word.lower() in name.lower().split()):
                persons.append(name)
    #print(personabout)

    if(len(persons)==0):
        for name in face_name:
            persons.append(name)
        return(list(set(persons)))
    else:
        return(list(set(persons)))






def gethimselforothers(face_name,text,whoistalking):
#face_name: list of faces identified, text: text in image whoistalking: Chinmay's output(String)
    whoistalking = whoistalking[0]
    persons=personabout(face_name,text)

    if(whoistalking in persons):
        return(1)
    else:
        return(0)



def getgradientinothers(face_name,text):
    persons=personabout(face_name,text)
    name=persons[0].replace('[','')
    name=name.replace(']','')
    name=name.replace('\'','')
    if(name in positive_persons):
        return(1)
    elif(name in negative_persons):
        return(-1)
    elif(name in neutral_persons):
        return(0)
    else:
        return(2)




#for third person, last parameter 'third_person'
#print(personabout(['Abdul Kalam'], "Claimed 100 seats delivered in binary",))
#print(gethimselforothers(['Abdul Kalam'],"Claimed 100 seats delivered in binary",''))
#print(getgradientinothers(['Abdul Kalam'],"Claimed 100 seats delivered in binary"))
