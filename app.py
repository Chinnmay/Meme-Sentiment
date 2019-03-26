# // console.log(JSON.stringify(textemoval[0]))
#
# //var textemoname = JSON.parse("{{textemoname}}")
# //console.log(textemoname);


from flask import Flask, render_template ,url_for,request
from werkzeug import secure_filename
from controllers import memeocr
from controllers import face_recognition_knn, overall_emotion
import os #oh
import jamspell
import Crop_Faces
from emotionsinglecode import emotion_single
import json



app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/')
print(UPLOAD_FOLDER)
CONTROLLER_FOLDER = os.path.join(APP_ROOT, 'controllers/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONTROLLER_FOLDER'] = CONTROLLER_FOLDER

ocr = memeocr.MemeOCR()


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

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
        print(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
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

        print("Content : ........." , content)

        output = Crop_Faces.cropfaces(file_path , "Face_cascade.xml")
        #print("Output==========" , output)

        count = output[-1]
        count = (count.get("count" , ""))
        output.pop()
        faces = []
        emotions = []
        if(count == ""):
            count = 0
        print("Count :" , count)
        for i in range(0 , count):
            for key , value in output[i].items():
                print(key , value)
                faces.append(key)
                emotions.append({key : value})


        #faces = face_recognition_knn.get_faces(file_path,md_path)
        textemoval , textemoname , stronger_emotion = emotion_single.main_func(content)
        print("=================================")
        # print(textemoval)
		#
        # print(stronger_emotion)
        text_emotion_len = len(textemoval)
        textemoname = json.dumps(textemoname)

        textemonames = {"Emotion" : textemoname}
        print(textemoname)


        overall_sentiment = overall_emotion.overall_sentiment(emotions[0][faces[0]] , stronger_emotion)
        print("Overall Emotions=========="  , overall_sentiment)
		#textsentiment = (textsentiment.drop(textsentiment.index[-1]))
		#print(faces)
        #resultdict['faces'] = faces
        #emotions = emotionDetect.predict(UPLOAD_FOLDER + f.filename)
        #f.save(secure_filename(f.filename))
        #emotions = emotionDetect.predict(f.filename)
        #print(emotions)

    return render_template('module.html', text_emotion_len = text_emotion_len, overall_sentiment = overall_sentiment ,faces = faces , ext_text = content , emotion = emotions , textemoval = textemoval, textemoname = textemoname,stronger_emotion = stronger_emotion, file = f.filename , all_faces = "faces" , img = f)



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
