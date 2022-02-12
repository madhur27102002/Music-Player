#setup screen-
from tkinter import *
from PIL import Image, ImageTk

class musicplayer:
    def __init__(self,Tk) -> None:
        self.root=Tk
        self.root.title('Music_Player')
        #width and height
        self.root.geometry('700x400')
        #background color--
        self.root.configure(background='white')
        #adding label
        self.label=Label(text='Select and Play', bg='black', fg='white', font=22).place(x=50, y=20)
        #adding leftsideimage--
        #l=left
        self.L_photo= ImageTk.PhotoImage(file='1.jpg')
        L_photo=Label(self.root, image=self.L_photo).place(x=400,y=100, width=200,height=147)
        
        
        #adding main img--
        self.photo=ImageTk.PhotoImage(file='music.jpg')
        photo=Label(self.root,image=self.photo,bg='white').place(x=50, y=50)
        
        #creating buttons--
        #play button-
        self.photo_B1=ImageTk.PhotoImage(file='play.png')
        photo_B1=Button(self.root, image=self.photo_B1, bd=0, bg='white').place(x=50, y=300, width=60, height=60)

        #pause button-
        self.photo_B2=ImageTk.PhotoImage(file='pause.png')
        photo_B2=Button(self.root, image=self.photo_B2, bd=0, bg='white').place(x=120, y=300, width=60, height=60)

        #Stop button-
        self.photo_B3=ImageTk.PhotoImage(file='stop.png')
        photo_B3=Button(self.root, image=self.photo_B3, bd=0, bg='white').place(x=190, y=300, width=60, height=60)
root=Tk()
object=musicplayer(root)
root.mainloop()