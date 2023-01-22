import requests
from tkinter import *
import json
from PIL import Image,ImageTk

x = Tk()
x.title('Weather Focus')
x.iconbitmap('C:\\Users\\USER\\Downloads\\clouds.ico')
x.geometry('1100x550+300+100')
x.configure(bg='purple')
x.resizable(0,0)


entry_defn_bg = PhotoImage(file="Images\\logo.png")
Label(x,image=entry_defn_bg,bg="purple").grid(row=0,column=1)
entry_defination = Label(x,text= 'County/Town:').grid(row=0,column=1)

entry_bg = PhotoImage(file="Images\\Rounded Rectangle 3.png")
Label(x,image=entry_bg,bg="purple").grid(row=0,column=4)

search = Entry(x,bg="white",borderwidth=1,font=("Times New Roman",19),fg="green")
search.grid(row=0,column=4,ipadx=60,ipady=8)
search.get()

spacing_label1 = Label(x,text=' ',bg='purple').grid(row=2)
spacing_label2 = Label(x,text=' ',bg='purple').grid(row=3)


def RESULTS():
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={search.get()}&appid=561873282dd9f39ea5aab7bd9f29e045')
    weather_data = json.loads(data.text)
    weather_result = Label(x,text=weather_data['weather'][0]['description'],font=("Times New Roman",15))
    weather_result.grid(row=3,column=4)

search_button_bg = PhotoImage(file="Images\\Layer 6.png")
search_button = Button(x,image=search_button_bg, bg="purple",command=lambda:RESULTS())
search_button.grid(row=0,column=5)

x.mainloop()
