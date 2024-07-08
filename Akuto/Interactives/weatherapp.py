import requests
import datetime as datetime
import customtkinter
from apiKey import *
import geocoder



class location:
    def __init__(self):
        self.userLoc = geocoder.ip("me") 
        return(self.userLoc)
#get current user location based on IP.


class functions:
    def __init__(self, master, interface):

        self.master= master
        self.interface= interface
    
    def returnWeatherData(self,event=None):
        self.event = event
        locationInput = lambda: self.interface.entry.get()# Retrieve the input from the entry widget

        key = apiKey #Key is inside another file for safety.

        weatherData = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={locationInput}&appid={key}"
        )
        if weatherData.status_code == 200:
            print(weatherData.json())
        else:
            print(f"Error {weatherData.status_code}")




class interface:
    def __init__(self, master, functions, app):

        self.master = master
        self.functions = functions 
        self.app = app
        self.app.title("WeatherApp")
        self.app.geometry("400x200")
        self.app.minsize(400,200)
        self.app._set_appearance_mode("system")
 

        self.frame = customtkinter.CTkFrame(app, bg_color="transparent", fg_color= "white")
        self.frame.pack_propagate(False) #Prevents from shrinking to the size of its content.
        self.frame.pack(expand=True, fill="both")

        self.entry = customtkinter.CTkEntry(self.frame, 
                                            fg_color="grey", 
                                            placeholder_text="Your location here:", 
                                            text_color="white",
                                            )                        
        self.entry.pack(pady=5, padx=5)
        self.entry.bind("<KeyRelease>", lambda event: self.functions.returnWeatherData(event))


 

if __name__ == "__main__":
    app = customtkinter.CTk()

    # Step 1: Instantiate interface without functions
    rootApp = interface(app, None, app)

    # Step 2: Instantiate functions with interface and master
    functionalities = functions(app, rootApp)

    # Step 3: Update interface with functions
    rootApp.functions = functionalities

    app.mainloop()