'''
import cv2
import emotionDetect

def cropfaces(imagePath , cascPath):

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    faces = faceCascade.detectMultiScale(
    	gray,
    	scaleFactor=1.1,
    	minNeighbors=5,
    	minSize=(30, 30),
    	#flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    count = 1
    output = []
    for (x, y, w, h) in faces:
    	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    	cropped = image[y:y+h , x:x+w]
    	#cv2.imshow("Cropped" , cropped)
    	filename = "image" + str(count) + ".png"
    	count = count + 1
    	cv2.imwrite(filename , cropped)
    for i in range(1 , count):
        out = emotionDetect.predict("image" + str(i) + ".png")
        output.append(out)
        print(out)


    cv2.imshow("Faces found", image)

    return(output)


'''




import cv2
import emotionDetect
from controllers import face_recognition_knn


    
def cropfaces(imagePath , cascPath):
    
    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )


    count = 5
    emotionfile = []	
    hashmap = {}
    finaloutput = []
    for (x, y, w, h) in faces:
        #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #print(str(x) + " " + str(y) + " " +str(w) + " " + str(h))
        cropped = image[y-15:y+h+15 , x-15:x+w+15]
        #cv2.imshow("Cropped" , cropped)
        filename = "image"+str(count)+".png"
        count = count + 1
        cv2.imwrite(filename , cropped)
    
    if(count == 5):
        #print("-----------------Direct model Called------------")
        person = ((face_recognition_knn.get_faces(imagePath , "controllers/trained_knn_model.clf")))
        #emotionfile.append(imagePath)
        emotion = (emotionDetect.predict(imagePath))    
        
        if not person:
            person = "Not Found"
        
        print("Person..........CNT " , person)
        
        hashmap = {person : emotion}
        finaloutput.append(hashmap)
        
        hashmap = {"count" : count - 5}
        
        #for key,value in finaloutput[0].items():
            #print(key , value + "\n")
        #print(finaloutput[0])
        return finaloutput
    
    	
    for i in range(5,count):
        files = "image"+str(i)+".png"
        #print(files)
        person = ((face_recognition_knn.get_faces(files , "controllers/trained_knn_model.clf")))
        print("Person.......... " , person)
        if not person:
            continue
        #emotionfile = []
        #emotionfile.append(files)
        emotion = (emotionDetect.predict(files))
        hashmap = {person : emotion}
        finaloutput.append(hashmap)
	
	#kvn
    hashmap = {"count" : count - 5}
    finaloutput.append(hashmap)
    #print(finaloutput[-1])
    #print(finaloutput)
    return finaloutput	


'''
    
    
    
    
    
    
    
    
    
    print("skjfd")

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )


    count = 5
    emotionfile = []	
    hashmap = {}
    finaloutput = []
    for (x, y, w, h) in faces:
        #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(str(x) + " " + str(y) + " " +str(w) + " " + str(h))
        cropped = image[y-15:y+h+15 , x-15:x+w+15]
        #cv2.imshow("Cropped" , cropped)
        filename = "image"+str(count)+".png"
        count = count + 1
        cv2.imwrite(filename , cropped)
    
    if(count == 5):
        person = ((face_recognition_knn.predict(imagePath , model_path="controllers/trained_knn_model.clf")))
        #emotionfile.append(imagePath)
        emotion = (emotionDetect.predict(imagePath))    
        
        if not person:
            person = "Not Found"
        
        hashmap = {person[0] : emotion}
        finaloutput.append(hashmap)
        #print(finaloutput)
        return finaloutput
    
    	
    for i in range(5,count):
        files = "image"+str(i)+".png"
        #print(files)
        person = ((face_recognition_knn.predict(files , model_path="controllers/trained_knn_model.clf")))
        if not person:
            continue
        #emotionfile = []
        #emotionfile.append(files)
        emotion = (emotionDetect.predict(files))
        hashmap = {person[0] : emotion}
        finaloutput.append(hashmap)
	
	#kvn

    #print(finaloutput)	
    return finaloutput	
#cropfaces("2560.jpg" , "Face_cascade.xml")


#cv2.imshow("Faces found", image)
#cv2.waitKey(0)

'''
