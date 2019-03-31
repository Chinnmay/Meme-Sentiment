import pandas as pd

def checkParty(person1 , person2):

    data = pd.read_csv('partyMemberList.csv')

    person1 = person1.lower()
    person2 = person2.lower()

    party1 = data[data.columns[0]].tolist()
    party1 = [x.lower() for x in party1 if str(x) != 'nan']

    party2 = data[data.columns[1]].tolist()
    party2 = [x.lower() for x in party2 if str(x) != 'nan']


    party3 = data[data.columns[2]].tolist()
    party3 = [x.lower() for x in party3 if str(x) != 'nan']

    party4 = data[data.columns[3]].tolist()
    party4 = [x.lower() for x in party4 if str(x) != 'nan']

    for first_person in party1:
        if person1 in first_person:
            for second_person in party1:
                if person2 in second_person:
                    return True
            return False


    for first_person in party2:
        if person1 in first_person:
            for second_person in party2:
                if person2 in second_person:
                    return True
            return False

    for first_person in party3:
        if person1 in first_person:
            for second_person in party3:
                if person2 in second_person:
                    return True
            return False

    for first_person in party4:
        if person1 in first_person:
            for second_person in party4:
                if person2 in second_person:
                    return True
            return False

if __name__ == "__main__":
    print(checkParty("modi" , "Thackrey"))
