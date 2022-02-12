# setup screen-
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

mixer.init()


class musicplayer:
    def __init__(self, Tk) -> None:
        self.root = Tk
        self.root.title('Music_Player')
        # width and height
        self.root.geometry('700x400')
        # background color--
        self.root.configure(background='white')
        # adding label
        self.label = Label(text='Select and Play', bg='black', fg='white', font=22).place(x=50, y=20)
        # adding leftsideimage--
        # l=left
        self.L_photo = ImageTk.PhotoImage(file='1.jpg')
        L_photo = Label(self.root, image=self.L_photo).place(x=400, y=100, width=200, height=147)

        # adding main img--
        self.photo = ImageTk.PhotoImage(file='music.jpg')
        photo = Label(self.root, image=self.photo, bg='white').place(x=50, y=50)

        # creating buttons--
        # play button-
        self.photo_B1 = ImageTk.PhotoImage(file='play.png')
        photo_B1 = Button(self.root, image=self.photo_B1, bd=0, bg='white').place(x=50, y=300, width=60, height=60)

        # pause button-
        self.photo_B2 = ImageTk.PhotoImage(file='pause.png')
        photo_B2 = Button(self.root, image=self.photo_B2, bd=0, bg='white').place(x=120, y=300, width=60, height=60)

        # Stop button-
        self.photo_B3 = ImageTk.PhotoImage(file='stop.png')
        photo_B3 = Button(self.root, image=self.photo_B3, bd=0, bg='white').place(x=190, y=300, width=60, height=60)

        # Adding leftsideimage--
        # L=left
        self.L_photo = ImageTk.PhotoImage(file='leftsideimage.jpg')
        L_photo = Label(self.root, image=self.L_photo).place(x=240, y=80, width=500, height=250)

        # Label
        self.label1 = Label(Self.root, text="Let's play it..", bg='black', fg='white', font=20)
        self.label1.pack(side=BOTTOM, fill=x)

        # Functions--

        # PlayButton
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load('4.mp3')
                    mixer.music.play()
                    self.label1['text'] = 'Music_Playing...'
                except:
                    pass
            else:
                mixer.music.unpause()
                self.label1['text'] = 'Music_Unpaused'

        # StopButton
        def stopmusic():
            mixer.music.stop()
            self.label1['text'] = 'Music_Stopped'

        # PauseButton
        def pausemusic():
            @

            global paused
            paused = TRUE
            mixer.music.pause()
            self.label1['text'] = 'Music_Paused'

        # VolumeBar
        def volume(vol):
            volume = int(vol) / 100
            mixer.music.set_volume(volume)

        # Mute Function
        def mute():
            self.scale.set(0)
            self.mute = ImageTk.PhotoImage(file='mute.jpeg')
            mute = Button(self.root, image=self.mute, bg='white', command=unmute).place(x=280, y=310)
            self.label1['text'] = 'Music_Mute'

        # Unmute Function
        def unmute():
            self.scale.set(25)
            self.volimg = ImageTk.PhotoImage(file='6.jpeg')
            volimg = Button(self.root, image=self.volimg, bg='white', bd=0).place(x=260, y=290)
            self.label1['text'] = 'Music_Mute'

        # Creating Buttons--
        # play_button--
        self.photo_B1 = ImageTk.PhotoImage(file='1.jpeg')
        photo_B1 = Button(self.root, image=self.photo_B1, bd=0, bg='white', command=playmusic).place(x=5, y=300)

        # pause_button--
        self.photo_B2 = ImageTk.PhotoImage(file='2.jpeg')
        photo_B2 = Button(self.root, image=self.photo_B2, bd=0, bg='white', command=pausemusic).place(x=85, y=300)

        # stop_button--
        self.photo_B3 = ImageTk.PhotoImage(file='3.jpeg')
        photo_B3 = Button(self.root, image=self.photo_B3, bd=0, bg='white', command=stopmusic).place(x=165, y=300)

        # Volume --Img-
        self.volimg = ImageTk.PhotoImage(file='6.jpeg')
        volimg = Button(self.root, image=self.volimg, bg='white', bd=0, command=mute).place(x=260, y=290)

        # volume bar--
        self.scale = Scale(self.root,
        from = 0, to = 100, orient = HORIZONTAL, bg = 'cyan', length = 120, command = volume(25))
        self.scale.set(25)
        self.scale.place(x=300, y=290)


root = Tk()
object = musicplayer(root)
root.mainloop()
