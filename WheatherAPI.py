import requests
from tkinter import *
import json
import datetime

x = Tk()
x.title('Weather Focus')
x.iconbitmap('C:\\Users\\USER\\PycharmProjects\\PractiseProjects\\clouds.ico')
x.geometry('1100x550+300+100')
x.configure(bg='purple')
x.resizable(False, False)

Label(x, text=' ', bg='purple').grid(row=5, column=0)

Label(x, text="Temperature :", font=('Times New Roman', 12), bg="black", fg="white").grid(row=2, column=0)
Label(x, text="Humidity :", font=('Times New Roman', 12), bg='black', fg='white').grid(row=3, column=0)
Label(x, text="Air Pressure :", font=('Times New Roman', 12), bg='black', fg='white').grid(row=4, column=0)
Label(x, text="Condition:", bg='black', font=('Times New Roman', 15, 'bold'), fg='white').grid(row=6, column=0)

entry_defn_bg = PhotoImage(file="Images\\logo.png")
Label(x, image=entry_defn_bg, bg="purple").grid(row=0, column=0)
Label(x, text='County/Town:', font=("Times New Roman", 12)).grid(row=0, column=0)

entry_bg = PhotoImage(file="Images\\Rounded Rectangle 3.png")
Label(x, image=entry_bg, bg="purple").grid(row=0, column=4)

search = Entry(x, bg="white", borderwidth=1, font=("Times New Roman", 19), fg="green")
search.grid(row=0, column=4, ipadx=60, ipady=8)


def RESULTS():
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={search.get()}&appid=561873282dd9f39ea5aab7bd9f29e045'
        f'&units=metric')
    weather_data = json.loads(data.text)
    Label(x, text=weather_data['weather'][0]['description'],
          font=("Times New Roman", 15, "bold", 'italic'), bg="purple", fg='white').grid(row=6, column=1)
    Label(x, text=f"{weather_data['main']['temp']} \N{DEGREE SIGN}C",
          font=("Times New Roman", 15, "bold", 'italic'), bg="purple", fg='white').grid(row=2, column=1)
    Label(x, text=f"{weather_data['main']['humidity']} %",
          font=("Times New Roman", 15, "bold", 'italic'), bg="purple", fg='white').grid(row=3, column=1)
    Label(x, text=f"{weather_data['main']['pressure']} hPa",
          font=("Times New Roman", 15, "bold", 'italic'), bg="purple", fg='white').grid(row=4, column=1)
    Label(x, text=f"{weather_data['name']}, {weather_data['sys']['country']}",
          font=("Times New Roman", 18, "bold", 'italic'), bg="purple", fg='yellow').grid(row=1, column=0)


search_button_bg = PhotoImage(file="Images\\Layer 6.png")
search_button = Button(x, image=search_button_bg, bg="purple", command=lambda: RESULTS())
search_button.grid(row=0, column=5)

x.mainloop()
