import requests
from tkinter import *
import json

x = Tk()
x.title('Weather Focus')
x.geometry('700x600')
location = input('enter location: ')
data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid'
                    f'=561873282dd9f39ea5aab7bd9f29e045')
weather_data = json.loads(data.text)


def exit_task():
    quit()

Label(x, text=weather_data['weather']).pack()

exit_button = Button(x, text='Exit', pady=10, padx=20, command=exit_task)
exit_button.pack()

x.mainloop()
