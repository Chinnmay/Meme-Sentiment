# // console.log(JSON.stringify(textemoval[0]))
#
# //var textemoname = JSON.parse("{{textemoname}}")
# //console.log(textemoname);


from flask import Flask, render_template ,url_for,request
from werkzeug import secure_filename
from controllers import memeocr
from controllers import face_recognition_knn, overall_emotion, personality_score
import os #oh
import jamspell
import Crop_Faces
from emotionsinglecode import emotion_single as emotion_single
import json
from collections import Counter



app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/')
CONTROLLER_FOLDER = os.path.join(APP_ROOT, 'controllers/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONTROLLER_FOLDER'] = CONTROLLER_FOLDER

ocr = memeocr.MemeOCR()


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')


def edit_output(output):
    content = str(output)
    b = "[]{}.\""
    content = corrector.FixFragment(content)
    for char in b:
        content = content.replace(char , '')
    return content


@app.route('/')
def home():
    return render_template('module.html')

@app.route('/', methods=['GET','POST'])

def upload_file():
    resultdict={}
    if request.method == 'POST':

        f = request.files['photo']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))
        md_path = os.path.join(app.config['CONTROLLER_FOLDER'],"trained_knn_model.clf")
        #print("Model Path ........" , md_path)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        ext_text = ocr.recognize(UPLOAD_FOLDER + f.filename)

        file_content = str(ext_text).split(',')
        content = "".join(file_content)

        content = content.upper()
        content = content.replace('!J' , 'U')
        content = content.replace('$' , 'S')
        content = content.replace('()' , 'O')
        content = content.replace('1' , 'T')
        b = "[]<()!@#$%^&*-_:{}.,''?/|\~`\""
        content = corrector.FixFragment(content)
        for char in b:
            content = content.replace(char , '')


        output = Crop_Faces.cropfaces(file_path , "Face_cascade.xml")
        #print("Output==========" , output)

        count = output[-1]
        count = (count.get("count" , ""))
        output.pop()
        faces = []
        emotions = []
        if(count == ""):
            count = 0

        if(count == 0):
            for key,value in output[0].items():
                if len(key) == 0:
                    continue
                faces.append(key)
                emotions.append({key : value})

        for i in range(0 , count):
            for key , value in output[i].items():
                if len(key) == 2:       #key is [].........trated as a string hence length 2
                    continue
                faces.append(key)
                emotions.append({key : value})


        #faces = face_recognition_knn.get_faces(file_path,md_path)
        textemoval , textemoname , stronger_emotion = emotion_single.main_func(content)
        #print("=================================")
        # print(textemoval)
    #
        # print(stronger_emotion)
        text_emotion_len = len(textemoval)
        textemoname = json.dumps(textemoname)

        textemonames = {"Emotion" : textemoname}


        overall_sentiment = []
        count = 0
        for i in emotions:
            overall = (overall_emotion.overall_sentiment(i[faces[count]] , stronger_emotion))
            if(overall != 'no_Emotion'):
                overall_sentiment.append(overall)
            count = count + 1
        most_common = ""
        overall_sentiment_score = []
        if overall_sentiment:
            overall_sentiment.sort()

            length = len(overall_sentiment)
            try:
                negative_occurences = length - overall_sentiment[::-1].index('negative')
            except:
                negative_occurences = 0
            overall_sentiment_score.append(negative_occurences)
            try:
                positive_occurences = length - overall_sentiment.index('positive')
            except:
                 positive_occurences = 0
            overall_sentiment_score.append(positive_occurences)

            neutral_occurences = length - positive_occurences - negative_occurences
            if(neutral_occurences < 0):
                neutral_occurences = 0
            overall_sentiment_score.append(neutral_occurences)

            most_common,num_most_common = Counter(overall_sentiment).most_common(1)[0]

    #overall_sentiment = overall_emotion.overall_sentiment(emotions[0][faces[0]] , stronger_emotion)
        #print("Overall Emotions=========="  , overall_sentiment)
    #textsentiment = (textsentiment.drop(textsentiment.index[-1]))
    #print(faces)
        #resultdict['faces'] = faces
        #emotions = emotionDetect.predict(UPLOAD_FOLDER + f.filename)
        #f.save(secure_filename(f.filename))
        #emotions = emotionDetect.predict(f.filename)
        #print(emotions)

    face_with_tag = []

    for face in faces:
        tag = personality_score.check(face)
        if tag == "":
            face_with_tag.append(face)
        else:
            face_with_tag.append({face : tag})

    face_with_tag = edit_output(face_with_tag)
    emotions = edit_output(emotions)

    return render_template('module.html', strongest_overall_emotion = most_common,text_emotion_len = text_emotion_len, overall_sentiment = overall_sentiment_score ,faces = face_with_tag , ext_text = content , emotion = emotions , textemoval = textemoval, textemoname = textemoname,stronger_emotion = stronger_emotion, file = f.filename , all_faces = "faces" , img = f)



@app.route('/example1')
def example1():
    return render_template('test1.html')


@app.route('/example2')
def example2():
    return render_template('test2.html')

@app.route('/example3')
def example3():
    return render_template('test3.html')


@app.route('/example4')
def example4():
    return render_template('test4.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
