from tkinter.ttk import Progressbar
from pyowm.exceptions import api_response_error, api_call_error
from weather import *
from twitterBot import *
import requests
from PIL import Image, ImageTk
import io
from tkinter import Tk, StringVar, Frame, Message, Label, Entry, Button, HORIZONTAL


class UI:
    def __init__(self):
        self.name = StringVar
        window = Tk()
        window.geometry('500x550')
        window.title('Daily Assistant Made by Max')
        frame = Frame(window)
        frame.pack()

        def temperatureclick():
            try:
                for i in range(1, 10):
                    Message(frame, text='            ', font=100, width=500).grid(row=i, column=2)

                weather = Weather(city.get())
                Message(frame, text=weather.status(), font=100, width=500).grid(row=2, column=2)
                Message(frame, text=weather.temperature(), font=100, width=500).grid(row=3, column=2)
                Message(frame, text=weather.temperatureMax(), font=100, width=500).grid(row=4, column=2)
                Message(frame, text=weather.temperatureMin(), font=100, width=500).grid(row=5, column=2)
                Message(frame, text=weather.wind(), font=100, width=700).grid(row=6, column=2)
                Message(frame, text=weather.cloudcoverage(), font=100, width=700).grid(row=7, column=2)
                Message(frame, text=weather.pressure(), font=100, width=700).grid(row=8, column=2)
                Message(frame, text=weather.humidity(), font=100, width=700).grid(row=9, column=2)
                response = requests.get(weather.icon())
                img = Image.open(io.BytesIO(response.content))
                img = ImageTk.PhotoImage(img)
                panel = Label(frame, image=img)
                panel.image = img
                panel.grid(row=1, column=2)
            except api_response_error.NotFoundError:
                for i in range(1, 10):
                    Message(frame, text='Error', font=100, width=500).grid(row=i, column=2)

            except api_call_error.APICallError:
                for i in range(1, 10):
                    Message(frame, text='Error', font=100, width=500).grid(row=i, column=2)

        def tweeter():

            acc = account.get()
            pas = password.get()
            twt = tweet.get()
            twtBot = twitterBot(acc, pas, twt)
            twtBot.tweeter()
            pgBar['value'] = 100
            Message(frame, text='Tweet Sent!', font=100, width=700).grid(row=15, column=3)

        Label(frame, text='Enter your city:', font=100).grid(row=0, column=1)
        city = Entry(frame, font=100)
        Button(frame, text='Check!', font=100, command=temperatureclick).grid(row=0, column=3)
        city.grid(row=0, column=2)

        Label(frame, text='Weather ', font=100).grid(row=1, column=1)
        Label(frame, text='Weather Status:', font=100).grid(row=2, column=1)
        Label(frame, text='Temperature:', font=100).grid(row=3, column=1)
        Label(frame, text='Highest temperature:', font=100).grid(row=4, column=1)
        Label(frame, text='Lowest temperature:', font=100).grid(row=5, column=1)
        Label(frame, text='Wind Speed:', font=100).grid(row=6, column=1)
        Label(frame, text='Cloud Coverage:', font=100).grid(row=7, column=1)
        Label(frame, text='Pressure:', font=100).grid(row=8, column=1)
        Label(frame, text='Humidity:', font=100).grid(row=9, column=1)

        Label(frame, text='', font=100).grid(row=10, column=1)
        Label(frame, text='Twitter Account:', font=100).grid(row=11, column=1)
        Label(frame, text='Twitter Password:', font=100).grid(row=12, column=1)
        Label(frame, text='Tweet:', font=100).grid(row=13, column=1)

        pgBar = Progressbar(frame, length=200, orient=HORIZONTAL, value=0, maximum=100, mode='determinate')

        pgBar.grid(row=15, column=2)

        account = Entry(frame, font=100)
        password = Entry(frame, font=100)
        tweet = Entry(frame, font=100)
        account.grid(row=11, column=2)
        password.grid(row=12, column=2)
        tweet.grid(row=13, column=2)
        Button(frame, text='Send your tweet!', font=100, command=tweeter).grid(row=14, column=2)
        twitterImage = Image.open('twitter.png')
        twitterImage = twitterImage.resize((70, 70), Image.ANTIALIAS)
        twitterImage = ImageTk.PhotoImage(twitterImage)
        panel = Label(frame, image=twitterImage)
        panel.image = twitterImage
        panel.grid(row=14, column=1)

        window.mainloop()


UI()
