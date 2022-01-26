import tkinter as tk
import requests
#from Pillow-PIL import ImageTk, Image
#import Pillow as PP

def test_function(entry):
    print("This is the entry!", entry)

def get_weather(city):
    weather_key = "efb71c4aff8eff9a2b5dfb3022e5e7b8"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params = params)
    #print(response.json())
    dict_aux = response.json()
    a = ((dict_aux["main"]["temp"] - 32) * 5 / 9)
    label["text"] = "{:.2f}".format(a) + " ºC"



#?q={city name},{state code},{country code}&appid={API key}

root = tk.Tk()



HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg="#3382ff")
canvas.pack()



#background_image = ImageTk.PhotoImage(Image.open("escenario.png"))
#background_label = tk.Label(root, image = background_image)
#background_label.

frame = tk.Frame(root, bg="#80c1ff", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get weather", font =40, command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root,bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely = 0.35, relwidth = 0.75, relheight = 0.55, anchor = "n")

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)





root.mainloop()

