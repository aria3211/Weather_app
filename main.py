import requests
from bs4 import BeautifulSoup
import tkinter as tk
from pil import Image


form = tk.Tk()
form.geometry('500x300')
form.title('Weather App')
form.resizable(False,False)


fream = tk.Frame(form,bg='#fff',width=500,height=200)
fream.place(x=0,y=0)

fream2 = tk.Frame(form,bg='#536e64',width=600,height=200)
fream2.place(x=0,y=200)

fream3 = tk.Frame(form,bg='#33FFDD',width=300,height=100)
fream3.place(x=300,y=200)

file = 'cloud1.gif'
info = Image.open(file)
frames = info.n_frames
im = [tk.PhotoImage(file = file, format=f'gif -index {i}') for i in range(frames)]

count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]
    gif_lab.configure(image=im2)

    count += 1
    if count == frames:
        count = 0
    anim = form.after(50,lambda :animation(count))




gif_lab = tk.Label(form,image = "",bg="#fff")
gif_lab.place(x=120,y=15)


global city
city = tk.StringVar()

tk.Label(form,text = "Enter the City Name:",font = ("Rounded MT Bold",12),bg = "#fff")
# lab.place()
entry1 = tk.Entry(form,textvariable=city, width=22, bg='#D0FFBC')
entry1.place(x=130,y=25)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



def Weather():
    global city
    city1 = city.get() + "Weather"
    city1 = city1.replace(" " , "+")

    res = requests.get(f'https://www.google.com/search?q={city1}&oq={city1}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)

    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    print(soup.select('#wob_dts'))
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    tk.Label(form,text = location,font=('Caveat 12 bold',9),bg = '#536e64',fg='white').place(x=123, y=250)
    tk.Label(form, text=info, font=('ROBOTO 15 bold',14), bg="#536e64", fg='#fff').place(x=121, y=220)
    tk.Label(form, text=f'{weather}°C', font='ROBOTO 35 bold', bg="#536e64", fg='#fff').place(x=4, y=210)

    time = time.split(",")
    n1 = tk.Label(form, text=time[0], font=('Caveat 20 bold',12), bg="#33FFDD", fg='#428df5')
    n1.place(x=350, y=236)
    n2 = tk.Label(form, text=time[1].upper(), font=('ROBOTO 15 bold',12), bg="#33FFDD", fg='#428df5')
    n2.place(x=325, y=240)
    entry1.delete('0', tk.END)
    entry1.get()



n3 = tk.Button(form, text='Check', font=("Arial Rounded MT Bold",10), bg="#D0FFBC", command=Weather)
n3.place(x=280, y=25)

animation(count)


form.mainloop()