from tkinter import *  
from PIL import ImageTk,Image  
class image_display:
    def __init__(self,root):
        canvas = Canvas(root, width = 2000, height = 1000)  
        canvas.pack()  
        fm = Frame(root,height=2000, width=1000, bg="blue")
        fm.pack(side=TOP,expand=NO,fill=NONE)
        # img = ImageTk.PhotoImage(Image.open("C:/Users/shubsush/Documents/PYTHON PROJECT/feed-globe.jpg"))  
        # canvas.create_image(-40, -30, anchor=NW, image=img) 
root = Tk()
display = image_display(root)
root.mainloop()  