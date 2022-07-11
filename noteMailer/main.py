#!/usr/bin/env python 
# Script modified from https://github.com/L0WK3Y-IAAN/Auto-Mailer/blob/master/automailer.py
# by Ponder Stine
# 10 July 2022

import sys
import smtplib
import datetime
import schedule
import subprocess
import time
from twilio.rest import Client

#Twilio Variables
# TODO
account_sid = "ENTER TWILIO ACCOUNT ID HERE"
auth_token = "ENTER TWILIO AUTH TOKEN HERE"
client = Client(account_sid, auth_token)

#SMTP Variables
# TODO
sender_email = ""
password = "INSERT SMTP PASSWORD HERE"
receiver_email = ["stine.ponder@gmail.com"]
message = "DEFAULT EMAIL MESSAGE HERE" 
recipients = '\n'.join(receiver_email)

#Data Variables
date = datetime.datetime.now()
currentDate = date.strftime("%B %d %Y, %I:%M:%S%p %Z")
print(date.strftime("%B %d %Y, %I:%M:%S%p EST"))

subprocess.call(['cls'],shell=True)
print('Waiting for execution time...')

#Mailing function
def send_email(randomMessage): 

    subprocess.call(['cls'],shell=True)
    server = smtplib.SMTP('smtp.gmail.com', 587) # TODO Change SMTP client here.
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    print("Login Successful.")
    message = randomMessage
    for receiver in receiver_email: 
        server.sendmail( sender_email, receiver, "Daily Random Second Brain Thought" + message )
        print("Email has been sent to " + receiver)
    server.quit()
    subprocess.call(['cls'],shell=True)
    print('Waiting for execution time...')
    
    #Creates log of when check-in was sent.
    f = open("logs.txt", "a")
    f.write("Note sent for: " + currentDate + ".\nNote:" + message + "\n")
    f.close()
    
    #Sends a text notification when email was sent.
    # txt = client.messages.create(
    # to="INSERT TO NUMBER HERE. ex. +1234567890", 
    # from_="INSERT FROM NUMBER HERE. ex. +1234567890",
    # body="INSERT TEXT MSG BODY HERE.")
    # print(txt)

#Schedule Functions
# def off_day():
#     print("Today is Sunday, enjoy your off day! :)")

def main():
    randomMessage = sys.argv[1] # TODO ensure python script can receive a random Note message as a CLI argument
    # print(randomMessage)
    schedule.every().day.at("07:00").do(send_email, randomMessage)

    # TODO validate all this logic that it starts a process running in the background that will initiate emails every day
    while 1:
        n = schedule.idle_seconds()
        if n is None:
            # no more jobs
            continue
        elif n > 0:
            # sleep exactly the right amount of time
            time.sleep(n)
        schedule.run_pending()

if __name__=="__main__":
    main()