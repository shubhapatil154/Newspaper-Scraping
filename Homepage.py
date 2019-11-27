from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        labelfont = ('times', 30, 'bold')
        widget = Label(root, text='BMS COLLEGE OF ENGINEERING')
        widget.config(fg='blue')  
        widget.config(font=labelfont)          
        widget.config(height=3, width=100)       
        widget.pack(expand=NO, side=TOP)

        labelfont = ('times', 25, 'bold')
        widget = Label(root, text='NEWSPAPER SCRAPING')
        widget.config(fg='blue')  
        widget.config(font=labelfont)          
        widget.config(height=0, width=100)       
        widget.pack(expand=NO, side=TOP)

        labelfont = ('times', 20, 'bold')
        widget = Label(root, text="NDTV",fg="green")
        widget.config(font=labelfont) 
        widget.place(x=80,y=200) 
        labelfont = ('times', 15, 'bold')
        widget = Button(root,text="read")
        widget.config(font=labelfont)
        widget.place(x=80,y=250)
        labelfont = ('times', 20, 'bold')

        widget = Label(root, text="NDTV",fg="green")
        widget.config(font=labelfont) 
        widget.place(x=80,y=200) 
        labelfont = ('times', 15, 'bold')
        widget = Button(root,text="read")
        widget.config(font=labelfont)
        widget.place(x=80,y=250)




root = Tk()
root.title("Newspaper Scarping")
app = Application(root)
root.geometry("1500x700")
root.mainloop()
