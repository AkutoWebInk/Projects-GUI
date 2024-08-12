import customtkinter
import sqlite3
from PIL import Image, ImageTk
import warnings
import LocalServer

def loadImage(path, size=(50, 50)):
    image = Image.open(path)
    image = image.resize(size)
    warnings.filterwarnings("ignore")
    return ImageTk.PhotoImage(image)

class Interface: 
    def __init__(self, master, requests):
        self.requests = requests
        self.master = master
        self.background = Interface.Background(self.master,requests)
        self.menu = Interface.Menu(self.master,self.background)

        self.master.title("Ákuto Manager")
        self.master.geometry("1368x420")
        self.master.minsize(1368,420)

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("dark-blue")
    
    class Background: 
        def __init__(self, master, requests):
            self.master = master
            self.requests = requests
            self.WidgetsON = False # Guides loadingInventy()
            
            # Instantiating Frames
            self.BackgroundFrame = customtkinter.CTkFrame(self.master, 
                                                          bg_color="transparent", 
                                                          fg_color="#242424", 
                                                          corner_radius=10)
            
            self.WidgetsCountainer = customtkinter.CTkScrollableFrame(self.BackgroundFrame,
                                                                      bg_color="transparent",
                                                                      fg_color="#242424",
                                                                      corner_radius=5,
                                                                      orientation="horizontal")
            
            # Packing
            self.BackgroundFrame.pack(pady=5, padx=5, fill="both", expand=True)
            self.WidgetsCountainer.pack(expand=True, side="right", fill="both")


           
            self.loadInventory()                 # Loads the results of searchDb() inside WidgetsCountainer.
        
        def loadInventory(self, event = "<Configure>"):
            # C'mon senior, this is closer to engligh than anything else:
            # Note :event: on window resize this function is called again to resize the inventory items on screen.
            
            if not self.WidgetsON: 
            # If the widgets aren't on screen:

                self.WidgetsCountainer.update_idletasks()            # Update the WidgetsCountainer current status/size/any-info before taking measurements.
                self.iHeight = self.WidgetsCountainer.winfo_height() # Storing WidgetsCoutnainer height-information inside a variable used on line 79.

                for idx, item in enumerate(self.requests.results):
                    #Loop that places a Widget on screen for each item returned by the searchDb() function.
                    
                    name = item[0] # searchDb() function used before returns a list for each item, like this // database:
                                                                                                  #                    [ item1:(name,etc...), 
                                                                                                  #                      item2:(name,etc...),
                                                                                                  #                       ... ]
                    frame = customtkinter.CTkFrame(self.WidgetsCountainer,
                                                height= self.iHeight,             # Placing the stored WidgetCountainer-Height here, on window resize they match height.
                                                width= 200,
                                                bg_color= "transparent",
                                                fg_color= "#272727",
                                                border_color= "#282828",
                                                border_width= 2,
                                                corner_radius= 15)
                    frame.pack_propagate(False)                                   # Set to false so the Frame doesn't shrink if the contents dont ocupy its full size.

                    frame.pack(side="left",padx= 5, pady= 2, fill="y" )
                    image = customtkinter.CTkLabel(frame,
                                                   image=loadImage("ConfigIcon.png", size=(150,150)),
                                                   text=" ")
                    image.pack(pady = 5, padx = 5)
            
            self.WidgetsON = True # Update the guide.

    class Menu:
        def __init__(self, master, background):
            self.background = background
            self.master = master
            self.ClickCount = 0 # Guides the ToggleMenu() function.
           
            self.MenuButton = customtkinter.CTkButton(self.master,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image = loadImage("MenuIcon.png", size=(30,30)),
                                                      text="",
                                                      width=10,
                                                      height=5,
                                                      command=self.ToggleMenu)
            self.SearchWidget = customtkinter.CTkEntry(self.master,
                                                       bg_color="transparent",
                                                       fg_color="transparent",
                                                       border_width=1,
                                                       border_color="#323232",
                                                       corner_radius= 10)
            
            self.MenuButton.pack(side="left", pady=5, padx=5)
            self.SearchWidget.pack(side="left",pady=5, padx=5)
            
            
            self.MenuFrame = customtkinter.CTkFrame(self.background.BackgroundFrame,
                                                    bg_color="transparent",
                                                    fg_color="#282828",
                                                    corner_radius=15,
                                                    width=180)
        
        def ToggleMenu(self):
        
            if self.ClickCount % 2 == 0:
                   # If the division betwen the ClickCount is even = Shows the menu
                self.MenuFrame.pack(fill="both", expand=True, padx=5, pady=0)
                
            else:
                   # If it ain't pair after dividing =  Hides the menu  
                self.MenuFrame.pack_forget()

            self.ClickCount += 1 # Itinerate the ClickCount


class Requests:
    def __init__(self, server, interface):
        self.interface = interface
        self.server = server




        self.results = server.searchDb()
        print("Requested through: Server Requests")
        
        for i in self.results:
            print(f"{i}")




if __name__ == "__main__":
    Customtkinter = customtkinter.CTk()
    LocalDb = LocalServer.LocalServer()

    FrontRequests = Requests(LocalDb, None)
    UserInterface = Interface(Customtkinter, FrontRequests)
    FrontEnd = Requests(LocalDb, UserInterface)

    Customtkinter.mainloop()
