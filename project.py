import tkinter as tk 
from PIL import Image, ImageTk  
import pygame
from tkinter import Scale
from mutagen.mp3 import MP3
from classSong import song


def create_main_window():
    window = tk.Tk()
    window.title("Music App")
    window.geometry("800x600")
    window.resizable(False, False)



    def homePage():

        h = tk.Frame(window)
        h.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        img = Image.open('img/anghami.png')
        img = img.resize((500, 200)) 
        photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(h, image=photo)
        img_label.image = photo 
        img_label.place(relx=0.5, rely=0.3, anchor='center')

        label = tk.Label(h, text='choose play list !', font=('bold', 20) , fg='#D49137')
        label.place(relx=0.5, rely=0.5, anchor='center')

        # English Playlist Button (Image + Label)
        eng_img = Image.open('img/engmusic.jpg')
        eng_img = eng_img.resize((100, 100))
        eng_photo = ImageTk.PhotoImage(eng_img)
        eng_label_img = tk.Label(h, image=eng_photo)
        eng_label_img.image = eng_photo
        eng_label_img.place(relx=0.3, rely=0.7, anchor='center')
        
        eng_label = tk.Label(h, text="English Playlist")
        eng_label.place(relx=0.3, rely=0.8, anchor='center')

        # Arabic Playlist Button (Image + Label)
        arb_img = Image.open('img/armusic.jpg')
        arb_img = arb_img.resize((100, 100))
        arb_photo = ImageTk.PhotoImage(arb_img)
        arb_label_img = tk.Label(h, image=arb_photo)
        arb_label_img.image = arb_photo
        arb_label_img.place(relx=0.7, rely=0.7, anchor='center')
        
        arb_label = tk.Label(h, text="Arabic Playlist" , font=('Arail',10))
        arb_label.place(relx=0.7, rely=0.8, anchor='center')

        # Bind click events to the images and labels
        eng_label_img.bind('<Button-1>', lambda event: songFrame())
        eng_label.bind('<Button-1>', lambda event: songFrame())

        arb_label_img.bind('<Button-1>', lambda event: arabicSongFrame())
        arb_label.bind('<Button-1>', lambda event: arabicSongFrame())


    def arabicSongFrame () :

        s = tk.Frame(window) 
        s.place(relx=0 , rely=0 , relwidth=1 , relheight=1 )

        label = tk.Label(s , text='Arabic Play List'  , font = ('bold' , 25) , fg='#D49137')
        label.place(relx=0.5, y=10, anchor='n')

        createSong(window, 0, "")
        createSong(window, 1, "ana negm" , type='a')
        createSong(window, 2, "w btir" , type='a')
        createSong(window, 3, "Sayer Hanoun" , type='a')
        createSong(window, 4, "kholset Al hkaye" , type='a')
        createSong(window, 5, "bel Ahlam" , type='a')
        

    def songFrame () : 

        s = tk.Frame(window) 
        s.place(relx=0 , rely=0 , relwidth=1 , relheight=1 )

        label = tk.Label(s , text='English Play List'  , font = ('bold' , 25) , fg='#D49137')
        label.place(relx=0.5, y=10, anchor='n')

        createSong(window, 0, "")
        createSong(window, 1, "call out my name")
        createSong(window, 2,  "rewrite the stars")
        createSong(window, 3,  "car's outside")
        createSong(window, 4,  "light switch")
        createSong(window, 5,  "A sky full of stars")


    def createSong (parent, row,  song_name , type = 'e'):

        def imgPath (row) :
            if row == 0 :
                imagBack = 'img/back.png' 
                return imagBack
            if type == 'e' : 
                imagePath = f'img/song{row}.jpg'
                return imagePath

            else : 
                imagePath = f'img/Asong{row}.jpg'
                return imagePath

        # Load and display the image
        image_path = imgPath(row)
        img = Image.open(image_path)
        img = img.resize((50, 50)) 
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(parent, image=photo)
        img_label.image = photo
        img_label.grid(row=row, column=0, padx=10, pady=10)
        
        

        if row > 0 : 
            if type == 'e' : 

                newsong = song(row , song_name , image_path , f'file/song{row}.mp3')
            if type=='a' :
                newsong = song(row , song_name , image_path , f'file/Asong{row}.mp3')

        

        # Display the song name
        song_label = tk.Label(parent, text=song_name, font=("Arial", 16))
        song_label.grid(row=row, column=1, padx=10, pady=10, sticky="w")

        # on click function 

        img_label.bind('<Button-1>' , lambda event: onClickSong(event , newsong , type))
        song_label.bind('<Button-1>' , lambda event: onClickSong(event , newsong , type))
        if row == 0 : 
            img_label.bind('<Button-1>' , lambda event : backClick(event))
        #  the <button-1> is the type of click that hold to do
        # this for right click mouse  



    def onClickSong (event , song , type = 'e') :

        playFrame(song , type)


    def backClick (event) :
        
        homePage()

        
    def playFrame(song , type = 'e'):
        f = tk.Frame(window)
        f.place(relx=0, rely=0, relwidth=1, relheight=1)

        backimg = Image.open('img/back.png')
        backimg = backimg.resize((50, 50))
        photo = ImageTk.PhotoImage(backimg)

        backLabel = tk.Label(f, image=photo)
        backLabel.image = photo
        backLabel.place(relx=0, rely=0)

        if type == 'e' : 
            backLabel.bind('<Button-1>', lambda event: backClick2(event))
        else : 
            backLabel.bind('<Button-1>', lambda event: backClick3(event))

        def backClick2(event):
            pause_song()
            songFrame()

        def backClick3 (event) :
            pause_song()
            arabicSongFrame()

        img = Image.open(song.img)
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)
        imglabel = tk.Label(f, image=photo)
        imglabel.image = photo
        imglabel.place(relx=0.5, rely=0.3, anchor='center')

        detailsLabel = tk.Label(f, text=f"{song.name}" , font=('Arial',20))
        detailsLabel.place(relx=0.5, rely=0.55, anchor='center')

        pygame.mixer.init()

        def play_song():

            pygame.mixer.music.load(song.file)
            if scale.get() == 0 : 
                pygame.mixer.music.play()
            else : 
                pygame.mixer.music.play()
                set_position(float(scale.get()))
                
                

        def pause_song():
            pygame.mixer.music.pause()

        def stop_song():
            pygame.mixer.music.stop()
            scale.set(0)

        def set_volume(volume):
            pygame.mixer.music.set_volume(float(volume) / 100)

        def set_position(position):
            pygame.mixer.music.set_pos(float(position))

        sngleg = song.length()
        user_changing_scale = False

        def on_scale_change(value):
            nonlocal user_changing_scale
            if user_changing_scale:
                set_position(float(value))

        scale = tk.Scale(f, from_=0, to=sngleg, orient=tk.HORIZONTAL, command=on_scale_change, length=200,
                bg='#D49137', fg='white', troughcolor='#D49137', sliderrelief=tk.RAISED, showvalue=True)

        scale.place(relx=0.5, rely=0.8, anchor='center')

        def on_mouse_down(event):
            nonlocal user_changing_scale
            user_changing_scale = True

        def on_mouse_up(event):
            nonlocal user_changing_scale
            user_changing_scale = False

        scale.bind("<Button-1>", on_mouse_down)
        scale.bind("<ButtonRelease-1>", on_mouse_up)

        volume_scale = Scale(f, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume, length=200, label="Volume")
        volume_scale.set(50)
        volume_scale.place(relx=0.5, rely=0.9, anchor='center')

        playB = tk.Button(f, text='Play', command=play_song)
        playB.place(relx=0.4, rely=0.7, anchor='center')
        pauseB = tk.Button(f, text='Pause', command=pause_song)
        pauseB.place(relx=0.6, rely=0.7, anchor='center')
        stop_button = tk.Button(f, text='Stop', command=stop_song)
        stop_button.place(relx=0.5, rely=0.7, anchor='center')

        def update_scale_position(scale_widget):
            if pygame.mixer.music.get_busy() and not user_changing_scale:
                current_position = scale_widget.get() + 1
                scale_widget.set(current_position)
            main_window.after(1000, update_scale_position, scale_widget)

        # Call the update_scale_position function with the scale widget as an argument
        update_scale_position(scale)

        # Load the image
        bottom_left_img = Image.open('img/music.png')
        bottom_left_img = bottom_left_img.resize((150, 150))  # Resize if necessary
        bottom_left_photo = ImageTk.PhotoImage(bottom_left_img)

        # Create a label to hold the image
        bottom_left_label = tk.Label(f, image=bottom_left_photo)
        bottom_left_label.image = bottom_left_photo  # Keep a reference to avoid garbage collection

        # Place the label at the bottom left
        bottom_left_label.place(relx=0, rely=1, anchor='sw')

        # Load the image
        top_right_img = Image.open('img/music2.png')
        top_right_img = top_right_img.resize((150, 150))  # Resize if necessary
        top_right_photo = ImageTk.PhotoImage(top_right_img)

        # Create a label to hold the image
        top_right_label = tk.Label(f, image=top_right_photo)
        top_right_label.image = top_right_photo  # Keep a reference to avoid garbage collection

        # Place the label at the top right
        top_right_label.place(relx=1, rely=0, anchor='ne')




    
    homePage()


    return window



if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()