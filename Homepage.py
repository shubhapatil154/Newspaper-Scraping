from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        #self.grid()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        '''fm = Frame(root, width=1000, height=3000, bg="white")
        fm.pack(side=TOP, expand=NO, fill=NONE)
        Label(self, text="BMS College of Engineering",font=("Times New Roman", 30)).grid(row=0,column=3)'''
        labelfont = ('times', 30, 'bold')
        widget = Label(root, text='BMS COLLEGE OF ENGINEERING')
        widget.config(fg='blue')  
        widget.config(font=labelfont)          
        widget.config(height=3, width=100)       
        widget.pack(expand=NO, side=TOP)

        labelfont = ('times', 25, 'bold')
        widget = Label(root, text='NEWSPAPER SCRAPING')
        widget.config(fg='red')  
        widget.config(font=labelfont)          
        widget.config(height=0, width=100)       
        widget.pack(expand=NO, side=TOP)

        labelfont = ('times', 20, 'bold')
        widget = Label(root, text="NDTV",fg="green")
        widget.config(font=labelfont) 
        widget.place(x=100,y=200)
        #widget.pack(expand=NO, side=LEFT) 

        labelfont = ('times', 15, 'bold')
        widget = Button(root,text="read")
        widget.config(font=labelfont)
        widget.place(x=180,y=200)




root = Tk()
root.title("Newspaper Scarping")
app = Application(root)
root.geometry("1500x700")
root.mainloop()
