import customtkinter
from PIL import Image, ImageTk
import warnings
import LocalServer

def loadImage(path, size=(50, 50)):
    image = Image.open(path)
    image = image.resize(size)
    warnings.filterwarnings("ignore")
    return ImageTk.PhotoImage(image)

class Interface: 
    def __init__(self, master, background, menu, server):
        self.master = master
        self.background = background
        self.menu = menu
        self.server = server

        self.master.title("Ákuto Manager")
        self.master.geometry("1368x420")
        self.master.minsize(1368,420)

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("dark-blue")
    
        

        

    class Background: 
        def __init__(self, master, server):
            self.master = master
            self.server = server

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


            #Search Data-base to return inventory items used in loadInventory() (line 62)
            
            self.results = server.searchDb()     # searchDb() is a function inside the backend that returns all items within the selected SQL table
            self.itemlist = len(self.results)    # Gotta len, else loadinventory() doesn't read as a list (go figure it out)
            print(self.itemlist)                 # Just to meake sure everything is returned alright, no need to print
            
            self.loadInventory()                 # Loads the results of searchDb() inside WidgetsCountainer.




        def loadInventory(self, event = "<Configure>"):
            # C'mon senior, this is closer to engligh than anything else:
            # Note :event: on window resize this function is called again to resize the inventory items on screen.
            
            if not self.WidgetsON: 
            # If the widgets aren't on screen:

                self.WidgetsCountainer.update_idletasks()            # Update the WidgetsCountainer current status/size/any-info before taking measurements.
                self.iHeight = self.WidgetsCountainer.winfo_height() # Storing WidgetsCoutnainer height-information inside a variable used on line 79.

                for idx, item in enumerate(self.results):
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
            
            self.WidgetsON = True # Update the guide.



    class Menu:
        def __init__(self, master, background):
            self.background = background
            self.master = master
            self.ClickCount = 0 # Guides the ToggleMenu() function.
           
           
            self.MenuFrame = customtkinter.CTkFrame(self.background.BackgroundFrame,
                                                    bg_color="transparent",
                                                    fg_color="#282828",
                                                    corner_radius=15,
                                                    width=180)
            self.MenuButton = customtkinter.CTkButton(self.master,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image = loadImage("AkutoIcon.png", size=(50,50)),
                                                      text="",
                                                      width=50,
                                                      height=50,
                                                      command=self.ToggleMenu)
            
            self.MenuButton.pack(side="left", pady=5, padx=5) 

        def ToggleMenu(self):
        
            if self.ClickCount % 2 == 0:
                   # If the division betwen the ClickCount is even = Shows the menu
                self.MenuFrame.pack(padx=5, fill="both", expand=True)
            else:
                   # If it ain't pair after dividing =  Hides the menu  
                self.MenuFrame.pack_forget() 

            self.ClickCount += 1 # Itinerate the ClickCount






if __name__ == "__main__":
    LocalDb = LocalServer.LocalServer()                                 # Accessing the LocalServer CLASS inside the LocalServer.py File 
    Customtkinter = customtkinter.CTk()                                 # Customtkinter is the "master" of the the front-end CLASSES
    Background = Interface.Background(Customtkinter,LocalDb)            # Accessing the Background sub-class inside the Interface CLASS
    Menu = Interface.Menu(Customtkinter, Background)                    # Accessing the Menu sub-class inside the Interface CLASS
    UserInterface = Interface(Customtkinter, Background, Menu, LocalDb) # Putting everything together
    Customtkinter.mainloop()                                            # Program's Loop