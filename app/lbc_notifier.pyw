#The render_teplate method is used to access an HTML filesomewhere in the applicationand displays it
from flask import Flask,render_template


app = Flask(__name__)
@app.route("/")
def home():
    return("asss")
    


import requests
import time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
money=0.03
while True:
    usd=requests.get("https://www.coingecko.com/en/coins/lbry-credits")
    c1=usd.content 
    soup1=BeautifulSoup(c1,"html.parser")
    a=str(soup1.find("span",{"class":"no-wrap"}).text)

    

    if(float(a[1:])>=money):
        server=smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()

        EMAIL="rishavghosh605@gmail.com"
        PASSWORD="sushmitaghosh"
        server.login(EMAIL,PASSWORD)

        message=MIMEText(a)
        message["From"]=EMAIL
        message["To"]=EMAIL
        message["Subject"]="LBC Notification"

        server.sendmail(EMAIL,EMAIL,message.as_string())

        print("Mail is successfully sent")
        money+=0.01
        time.sleep(60)
    else:
        print("False")

if __name__ == '__main__':
    app.run()
