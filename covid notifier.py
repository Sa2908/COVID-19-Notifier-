import time
import requests
from plyer import notification
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico",
        timeout = 10
    )
def getData(url):
    # return \
    raw = requests.get(url)
    return raw.text


if __name__ == '__main__':
    # notifyMe("Sanket", "Lets beat this disease")

    myHTMLdata = getData("https://www.mohfw.gov.in/")


    soup = BeautifulSoup(myHTMLdata, 'html.parser')


    myStrData = ""


    for tr in soup.find_all('tbody')[0].find_all('tr'):

        myStrData += tr.get_text()


    myStrData = myStrData[1:]

    itemList = myStrData.split("\n\n")

    statesList = ["West Bengal"]     #Add more states if you want to see more. I added only one as I needed only one

    newList = ""
    while True:
        for item in itemList[0:35]:
            newList = item.split("\n")
            if newList[1] in statesList:
                # print(newList)
                nTitle = "COVID-19 Cases"
                nText = f"State : {newList[1]}\nActive Cases : {newList[2]}"\
                    f"\nCured/Discharged : {newList[3]} Deaths : {newList[4]}\n" \
                    f"Total Cases : {newList[5]} "
                notifyMe(nTitle, nText)

        time.sleep(3600)



