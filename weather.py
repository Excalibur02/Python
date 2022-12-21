import tkinter as tk
import requests
import time

def getweather(screen):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=29b56202195e471e213de207a4bb112f"
    json_data = requests.get(api).json()
    if (json_data['cod']=="404") :
        label1.config(text = "")
        label2.config(text = "Randi ke bache ye city hai?? \n Gaand mei daal le aisi city ko !")
    else:
        conditions = json_data['weather'][0]['main']
        avgtemp = round((json_data['main']['temp'] - 273.150),3)
        tempmax = round((json_data['main']['temp_max'] - 273.15000),5)
        tempmin = round((json_data['main']['temp_min'] - 273.15000),5)
        humidity = round((json_data['main']['humidity']),3)
        wind = round((json_data['wind']['speed']),3)
        final_info = conditions + "\n" + str(avgtemp) + "°C"
        final_data = "\n" + "Maximum Temperature : "+str(tempmax) + "\n Minimum Temperature : " + str(tempmin) + "\n Humidity : "+str(humidity)+"\n Wind Speed : "+str(wind) + "\n"

        label1.config(text = final_info)
        label2.config(text = final_data)
screen = tk.Tk()
screen.geometry("500x500")
screen.title("Weather App")
# print(font.names())
f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")
text = tk.Label( text="Wanna know the weather ? Just enter the city !",font=("Times",15,"bold"))
text.place(x=55,y=15)
label0 = tk.Label(screen,font=f)
label0.config( text="Enter the city")
textfield = tk.Entry(screen, font= ("poppins",20,"bold"),borderwidth=5,background="yellow",width=20)
textfield.pack( padx = 30,pady = 50)
textfield.focus()
textfield.bind('<Return>',getweather)

label1 = tk.Label(screen, font = t)
label1.pack()
label2 = tk.Label(screen, font = f)
label2.pack()

screen.mainloop()
