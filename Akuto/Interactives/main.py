import customtkinter
from tkinter import *
from PIL import Image, ImageTk
  

# Function to load icons for buttons:
def load_icon(path, size=(50, 50)):
    image = Image.open(path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image) 
 # Call the function on button instantiation. i.e.: line 34
 # pass the path and size (standard menu size is 25) i.e.: load_icon("path", size=25,25)

def testfunc():
    print("Function call OK")

# Configs for the root itself:
class windowConfig:
    def __init__(self, master):
        self.master = master
        self.master.title("Ákuto Manager")
        self.master.geometry("1920x800")
        self.master.minsize(400, 800)
        self.master.after(0, lambda: root.state('zoomed'))
        customtkinter.set_appearance_mode('system')
        customtkinter.set_default_color_theme("dark-blue")
        # Bind a method to hide the menu when clicking on it

# Button to raise the menu:
class AkutoButton:
    def __init__(self, master, menu):
        self.master = master
        self.menu = menu
        self.aktimg = load_icon("icons\icon.png")

        # AkutoButton:
        self.aktimg = load_icon("icons\icon.png")
        self.AButton = customtkinter.CTkButton(self.master,
                                               image=self.aktimg,
                                               text="",
                                               width=50,
                                               height=40,
                                               fg_color="transparent",
                                               bg_color="transparent",
                                               hover=True,
                                               hover_color="#282828",
                                               command=self.menu.show
                                               ) 
        self.AButton.pack(pady=5, side="bottom", anchor="n")

# Small menu akin to Windows 11 start button:
class Menu:
    def __init__(self, master, background):
        self.master = master
        self.background = background
        self.menu_frame = customtkinter.CTkFrame(self.background, fg_color="#242424", width=200, height=400, border_width=0, corner_radius=10, bg_color="transparent")
        self.menu_frame.pack_propagate(False) #Make it so the menu frame doesnt shrinks to the size of its widgets
        self.menu_frame.place_forget()  # Initially hide the menu frame

        #Buttons within the menu:
        self.config_button_icon = load_icon("icons\ConfigIcon.png", size=(25,25))
        self.config_button = customtkinter.CTkButton(self.menu_frame,
                                                     image=self.config_button_icon,
                                                     text="",
                                                     width=30,
                                                     height=30,
                                                     fg_color="transparent",
                                                     bg_color="transparent",
                                                     hover=True,
                                                     hover_color="#282828",
                                                     command=lambda:testfunc()) #add function here 
        
        self.weather_button_icon = load_icon("icons\Weather.png", size=(25,25))
        self.weather_button= customtkinter.CTkButton(self.menu_frame,
                                                image=self.weather_button_icon,
                                                text="",
                                                width=30,
                                                height=30,
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                hover=True,
                                                hover_color="#282828",
                                                command=lambda:testfunc()) #add function here
        
        #self.config_button3_icon = load_icon("ConfigIcon.png", size=(25,25))
        self.config_button3 = customtkinter.CTkButton(self.menu_frame,
                                                #image=self.config_button_icon,
                                                text="",
                                                width=30,
                                                height=30,
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                hover=True,
                                                hover_color="#282828",
                                                command=lambda:testfunc()) #add function here
        
       #self.config_button4_icon = load_icon("ConfigIcon.png", size=(25,25))
        self.config_button4 = customtkinter.CTkButton(self.menu_frame,
                                                #image=self.config_button_icon,
                                                text="",
                                                width=30,
                                                height=30,
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                hover=True,
                                                hover_color="#282828",
                                                command=lambda:testfunc()) #add function here

    # Function to unhide the menu and load its widgets:
    def show(self): 
        self.menu_frame.place(x=self.master.winfo_width()/2, y=self.master.winfo_height()-270, anchor="center") # Placing the menu on screen 
        self.menu_frame.bind("<Button-1>", self.hide_menu)                                                      # Hide the menu when clicking somewhere empty inside the menu iself
        self.menu_frame.update_idletasks()                                                                      # Update the position of the widgets inside the menu before placing the menu on screen


        self.config_button.place(x=self.menu_frame.winfo_width()-45, y=self.menu_frame.winfo_height()-55)       # Placing the buttons on screen (has to be here so it loads on "show" function call)

        self.weather_button.place(x=self.menu_frame.winfo_width()-95, y=self.menu_frame.winfo_height()-55)

        self.config_button3.place(x=self.menu_frame.winfo_width()-145, y=self.menu_frame.winfo_height()-55) 

        self.config_button4.place(x=self.menu_frame.winfo_width()-195, y=self.menu_frame.winfo_height()-55) 

    def hide_menu(self, event):
        self.menu_frame.place_forget()

# Program's background, any option selected within the menu will be launched in this background:
class Background:
    def __init__(self, master):
        self.master = master
        self.background = customtkinter.CTkFrame(master, fg_color="grey", bg_color="transparent", corner_radius= 5)
        self.background.pack(expand=True, fill="both")

    def bind_hide_menu(self, menu):
        self.background.bind("<Button-1>", menu.hide_menu)







if __name__ == "__main__":
    root = customtkinter.CTk()
    rootWindow = windowConfig(root)
    background = Background(root)
    menu = Menu(root, background.background)
    background.bind_hide_menu(menu) #Bind the hide_menu method after both instances are created
    root.bind("<Configure>", menu.hide_menu) #Bind the hide_menu method on window resize
    AButton = AkutoButton(root, menu)
    root.mainloop()