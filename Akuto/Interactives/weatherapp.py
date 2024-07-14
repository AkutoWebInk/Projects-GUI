import requests
import datetime 
import customtkinter
import apiKey
import geocoder
from PIL import Image, ImageTk



def load_icon(path, size=(50, 50)):
    image = Image.open(path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)


class Location:
    def returnWeatherData(self):

        self.currentLoc = geocoder.ip("me") #get user current location by ip
        self.userCity = self.currentLoc.city #filter returned ip data to city only to be insert inside API request

        self.key = apiKey.apiKey 

        weatherData = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={self.userCity}&appid={self.key}"
        )
        self.data = (  
            f"{weatherData.json()}"
            )
        
        if weatherData.status_code == 200:
            print(f"{self.data}")
            
            return self.data

        else:
            print(f"Error {weatherData.status_code}")

#weather_description = weather_json['weather'][0]['description']

class Interface:
    def __init__(self, master, location):
        self.location = location
        self.master = master
        self.master.title("WeatherApp")
        self.master.minsize(400,200)
        self.master.geometry("200x100")
    
        self.frame = customtkinter.CTkFrame(self.master,
                                            fg_color="white", 
                                            border_width=0, 
                                            corner_radius=10, 
                                            bg_color="transparent")
        self.frame.pack(expand=True, fill = "both")


        self.weatherInfo=customtkinter.CTkLabel(self.frame,
                                                text=self.location.data,
                                                fg_color="grey",
                                                text_color="white"
                                                )
        self.weatherInfo.pack()
        event = self.weatherInfo.bind("<Motion>",Location.returnWeatherData)






        self.button = customtkinter.CTkButton(self.master,
                                              image = load_icon("icons\Weather\Weather.png", size=(25,25)),
                                              text="",
                                              width=50,
                                              height=50,
                                              fg_color="transparent",
                                              bg_color="transparent",
                                              hover_color="#282828",
                                              command= lambda: location.returnWeatherData()
                                              )
        self.button.pack(pady = 5, side = "bottom", anchor ="n")                                   
        














if __name__ == "__main__":

    location = Location()
    app = customtkinter.CTk()
    location.returnWeatherData()
    interface = Interface(app,location)
    

    app.mainloop()