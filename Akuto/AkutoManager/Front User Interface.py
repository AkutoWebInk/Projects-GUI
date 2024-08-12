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

class Requests:
    def __init__(self, server):
        self.server = server

        self.results = server.searchDb()
        print("Requested through: Server Requests")
        
        for i in self.results:
            print(f"{i}")


class Interface:    
    def __init__(self, master, requests):
        self.requests = requests
        self.master = master

        self.master.title("Ákuto Manager")
        self.master.geometry("1368x420")
        self.master.minsize(720,420)

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("dark-blue")
    
    class Horizontal:
        def __init__(self,master,requests):
            self.master = master
            self.requests = requests
            
            self.WidgetsON = False # Guides loadingInventy()
            
            self.BackgroundFrame = customtkinter.CTkFrame(self.master, 
                                                        bg_color="transparent", 
                                                        fg_color="#242424", 
                                                        corner_radius=10)
            
            self.WidgetsCountainer = customtkinter.CTkScrollableFrame(self.BackgroundFrame,
                                                                    bg_color="transparent",
                                                                    fg_color="#242424",
                                                                    corner_radius=5,
                                                                    orientation="horizontal")
            
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

    class Vertical:
        def __init__(self,master,requests):
            self.master = master
            self.requests = requests
            
            self.WidgetsON = False # Guides loadingInventy()
            
            self.BackgroundFrame = customtkinter.CTkFrame(self.master, 
                                                            bg_color="transparent", 
                                                            fg_color="#242424", 
                                                            corner_radius=10)
            
            self.WidgetsCountainer = customtkinter.CTkScrollableFrame(self.BackgroundFrame,
                                                                        bg_color="transparent",
                                                                        fg_color="#242424",
                                                                        corner_radius=5,
                                                                        orientation="vertical")
            
            self.BackgroundFrame.pack(pady=5, padx=5, fill="both", expand=True)
            self.WidgetsCountainer.pack(expand=True, side="right", fill="both")
            
            self.loadInventory()                 # Loads the results of searchDb() inside WidgetsCountainer.

        def loadInventory(self, event = "<Configure>"):
            # C'mon senior, this is closer to engligh than anything else:
            # Note :event: on window resize this function is called again to resize the inventory items on screen.
            
            if not self.WidgetsON: 
            # If the widgets aren't on screen:

                self.WidgetsCountainer.update_idletasks()            # Update the WidgetsCountainer current status/size/any-info before taking measurements.
                self.iWidth = self.WidgetsCountainer.winfo_width() # Storing WidgetsCoutnainer height-information inside a variable used on line 79.

                for idx, item in enumerate(self.requests.results):
                    #Loop that places a Widget on screen for each item returned by the searchDb() function.
                    
                    name = item[0] # searchDb() function used before returns a list for each item: item1 = (name,info2,info3...), item2...
                    frame = customtkinter.CTkFrame(self.WidgetsCountainer,              # name   = item     [0] , [1] , [2]     
                                                height=30,                              # Placing the stored WidgetCountainer-Height here, on window resize they match height.
                                                width=self.iWidth,
                                                bg_color="transparent",
                                                fg_color="#282828",
                                                border_color="#262626",
                                                border_width=1,
                                                corner_radius=5)
                    
                    button = customtkinter.CTkButton(frame,
                                                     height=26,
                                                     width=26,
                                                     bg_color="transparent",
                                                     fg_color="transparent",
                                                     corner_radius=5,
                                                     image=loadImage("ExpandIcon.png", size=(28,28)),
                                                     text="",
                                                     hover_color="#262626",
                                                     border_spacing=1,
                                                     command=None)
                    
                    
                    frame.pack_propagate(False)                                         # Set to false so the Frame doesn't shrink if the contents dont ocupy its full size.
                    frame.pack(padx=5, pady=2, fill="both", expand=True)
                    button.pack(side = "right", pady=1, padx=3)
                   
                    
            
            self.WidgetsON = True # Update the guide.


    class Menu:
        def __init__(self, master):
            self.master = master
            self.ClickCount = 0 # Guides the ToggleMenu() function.
           
            self.MenuButton = customtkinter.CTkButton(self.master.master,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image = loadImage("MenuIcon.png", size=(30,30)),
                                                      text="",
                                                      width=10,
                                                      height=5,
                                                      command=self.ToggleMenu)
            
            self.SearchWidget = customtkinter.CTkEntry(self.master.master,
                                                       bg_color="transparent",
                                                       fg_color="transparent",
                                                       border_width=1,
                                                       border_color="#323232",
                                                       corner_radius= 10)
            
            self.MenuButton.pack(side="left", pady=5, padx=5)
            self.SearchWidget.pack(side="left",pady=5, padx=5)
            
            
            self.MenuFrame = customtkinter.CTkFrame(self.master.BackgroundFrame,
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






if __name__ == "__main__":
    Customtkinter = customtkinter.CTk()
    LocalDb = LocalServer.LocalServer()
    ServerRequests = Requests(LocalDb)
    
    UserInterface = Interface(Customtkinter, ServerRequests)
    Background = UserInterface.Vertical(Customtkinter, ServerRequests)
    Menu = Interface.Menu(Background)


    Customtkinter.mainloop()
