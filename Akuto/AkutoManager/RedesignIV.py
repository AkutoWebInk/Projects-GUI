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
    def __init__(self, master, server):
        self.master = master
        self.server = server
        self.master.title("Ákuto Manager")
        self.master.geometry("1368x420")
        self.master.minsize(1368,420)

        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("dark-blue")
    
        self.localDb = LocalServer.LocalServer()
        self.background = self.Background(self.master, self.server)
        self.menu = self.Menu(self.master, self.background)

    class Background: 
        def __init__(self, master, server):
            self.master = master
            self.server = server
            self.WidgetsON = False
            
            
            self.BackgroundFrame = customtkinter.CTkFrame(self.master, bg_color="transparent", fg_color="#242424", corner_radius=10)

            self.WidgetsCountainer = customtkinter.CTkScrollableFrame(self.BackgroundFrame,
                                                                      bg_color="transparent",
                                                                      fg_color="#242424",
                                                                      corner_radius=5,
                                                                      orientation="horizontal")



            self.BackgroundFrame.pack(pady=5, padx=5, fill="both", expand=True)
            self.WidgetsCountainer.pack(expand=True, fill="both", side="right")

            self.results = server.searchDb()
            self.itemlist = len(self.results)
            print(self.itemlist)

            self.master.after(100, self.loadInventory)
            
        def loadInventory(self, event = "<Configure>"):
                
            if not self.WidgetsON:

                self.WidgetsCountainer.update_idletasks()
                self.iHeight = self.WidgetsCountainer.winfo_height()

                for idx, item in enumerate(self.results):
                    name = item[0]

                    itemf = customtkinter.CTkFrame(self.WidgetsCountainer,
                                                   height= self.iHeight,
                                                   width= 200,
                                                   bg_color= "transparent",
                                                   fg_color= "#272727",
                                                   border_color= "#282828",
                                                   border_width= 2,
                                                   corner_radius= 15)
                
                    imagel = customtkinter.CTkLabel(itemf,
                                                    height= 200,
                                                    width= 200,
                                                    bg_color="transparent",
                                                    fg_color="#242424",
                                                    image= loadImage("ConfigIcon.png", size=(180,180)),
                                                    text= " ")
                
                    infof = customtkinter.CTkLabel(itemf, text= f"{name}")
                    
                    itemf.pack(padx= 5,
                               pady= 2,
                               side= "left",
                               expand= True,
                               fill= "both")
                    imagel.pack()
                    infof.pack()

    
            self.WidgetsON = True




    class Menu:
        def __init__(self, master, background):
            self.background = background
            self.master = master
            self.ClickCount = 0
            

            self.MenuFrame = customtkinter.CTkFrame(self.background.BackgroundFrame,
                                                    bg_color="transparent",
                                                    fg_color="#282828",
                                                    corner_radius=15,
                                                    width=200,
                                                    height=400)
                       
            self.MenuButton = customtkinter.CTkButton(self.background.BackgroundFrame,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image=loadImage("AkutoIcon.png", size=(50,50)),
                                                      text="",
                                                      width=50,
                                                      height=50,
                                                      command=self.ToggleMenu)

            self.MenuButton.pack(side="bottom", pady=5, padx=5)

        def loadSideMenu(self):
            self.MenuButton.pack_forget() 
            self.MenuFrame.pack(padx=5, side="left", fill="both") 
                                

            self.MenuButton = customtkinter.CTkButton(self.MenuFrame,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image=loadImage("AkutoIcon.png", size=(50,50)),
                                                      text="",
                                                      width=50,
                                                      height=50,
                                                      command=self.ToggleMenu)
            
            self.MenuButton.pack(side="bottom", pady=5, padx=5)
        def hideSideMenu(self):

            self.MenuFrame.pack_forget()
            self.MenuButton.pack_forget()

            self.MenuButton = customtkinter.CTkButton(self.master,
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      corner_radius=15,
                                                      hover_color="#282828",
                                                      image=loadImage("AkutoIcon.png", size=(50,50)),
                                                      text="",
                                                      width=50,
                                                      height=50,
                                                      command=self.ToggleMenu)
                
            self.MenuButton.pack(side="left", pady=5, padx=5)

      
        def ToggleMenu(self):
           
            if self.ClickCount % 2 == 0:  #Menu ON 
                self.loadSideMenu()
            
            else:                         #Menu OFF
                self.hideSideMenu()
        
            self.ClickCount += 1






if __name__ == "__main__":
    Customtkinter = customtkinter.CTk()
    LocalDb = LocalServer.LocalServer()
    UserInterface = Interface(Customtkinter, LocalDb)
    Customtkinter.mainloop()
