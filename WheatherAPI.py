import requests
from tkinter import *
import json

x = Tk()
x.title('Weather Focus')
x.iconbitmap('C:\\Users\\USER\\Downloads\\clouds.ico')
x.geometry('700x600')

entry_defination = Label(x,text= 'County/Town:').grid(row=0,column=1)

def exit_task():
    quit()
exit_button = Button(x, text='Exit', pady=10, padx=20, fg='red', command=exit_task)
exit_button.grid(row=1,column=4)


search = Entry(x,width=50,borderwidth=5)
search.grid(row=0,column=4)
search.get()

spacing_label1 = Label(x,text=' ').grid(row=2)
spacing_label2 = Label(x,text=' ').grid(row=3)


def RESULTS():
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={search.get()}&appid=561873282dd9f39ea5aab7bd9f29e045')
    weather_data = json.loads(data.text)
    weather_result = Label(x,text=weather_data['weather'][0]['description'])
    weather_result.grid(row=3,column=4)

search_button = Button(x,text='search',command=lambda:RESULTS())
search_button.grid(row=0,column=5)

x.mainloop()
