import pandas as pd

def getText(img):

    data = pd.read_csv('./controllers/hugedatasetexcel.csv')

    img = img[:img.index('.')]
    Meme = data[data.columns[0]].tolist()
    Text = data[data.columns[1]].tolist()
    try:
        index = Meme.index(int(img))
        text = Text[index]
    except:
        text = ""

    return text
if __name__ == "__main__":
    getText(int('68'))
