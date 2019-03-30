import pandas as pd
import numpy as np


def check(face_name):

    csv_data = pd.read_csv("./controllers/personality_score.csv")

    face_name = face_name[2:face_name.rindex('\'')]

    if face_name == "unknown":
        return ""

    positive_persons = csv_data[csv_data.columns[0]].tolist()
    neutral_persons = csv_data[csv_data.columns[1]].tolist()
    negative_persons = csv_data[csv_data.columns[2]].tolist()

    tag = ""

    if face_name in positive_persons:
        tag = "Positive"
    elif face_name in negative_persons:
        tag = "Negative"
    elif face_name in neutral_persons:
        tag = "Neutral"

    return tag


if __name__ == "__main__":
    print(check("ramnath kovind"))
