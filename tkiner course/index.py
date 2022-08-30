# # import random

# # print("This is a virtual entertaining wolrd\n")
# # n=input("Enter your name =")
# # print("You are playing (snake , water , gun) luck game\n" )
# # list=["s","w","g"]

# # player=0
# # boot=0
# # chance= int (input("How many times do u want to play 'not more than 10 times' = "))

# # i=0
# # while i<chance:
    
# #     chose=input("chose s , w , g = ")
# #     p=chose.lower()
# #     if p!='s' and p!='g' and p!='w':
# #         print('Invalid input! Please enter again')
# #         continue
# #     opt=random.choice(list)
    
# #     if opt=="s" and p=="w" :
# #         print('Oops!You lose in this round', n)
# #         print('Better luck next time')
# #         boot+=1
# #     if opt=="w" and p=="s" :
# #         print('Congarts!You win in this round', n)
# #         player+=1

# #     if opt=="g" and p=="s" :
# #         print('Oops!You lose in this round', n)
# #         print('Better luck next time')
# #         boot+=1
# #     if opt=="s" and p=="g" :
# #         print('Congarts!You win in this round', n)
# #         player+=1
    
# #     if opt=="w" and p=="g" :
# #         print('Oops!You lose in this round', n)
# #         print('Better luck next time')
# #         boot+=1
# #     if opt=="g" and p=="w" :
# #         print('Congarts!You win in this round', n)
# #         player+=1
    

   
 
# #     elif opt==p:
# #         print('Round draw!', n)

# #     i=i+1
# #     print("You have played", i ,"chnaces")

   
# # if player_win>computer_win:
# #     print('Congrats!You win the game', n)  
# # elif player_win<computer_win:
# #     print('Oops!You lose the game', n)
# # else:
# #     print('Match draw!', n)
# # print('Your score : ',player_win)
# # print('Computer score : ',computer_win)  

# # print ("Your total is =" , player)
# # print ("boot total is = " , boot)



# from pygame import mixer
# from datetime import datetime
# from time import time

# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break

# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")

# if __name__ == '__main__':
#     # musiconloop("water.mp3", "stop")
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     watersecs = 5
#     exsecs = 8
#     eyessecs = 12

#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking time. Enter 'drank' to stop the alarm.")
#             musiconloop('water.mp3', 'drank')
#             init_water = time()
#             log_now("Drank Water at")

#         if time() - init_eyes >eyessecs:
#             print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
#             musiconloop('eyes.mp3', 'doneeyes')
#             init_eyes = time()
#             log_now("Eyes Relaxed at")

#         if time() - init_exercise > exsecs:
#             print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
#             musiconloop('physical.mp3', 'donephy')
#             init_exercise = time()
#             log_now("Physical Activity done at")


from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import pygame

pygame.init()
pygame.mixer.init()

music_file = None

def add_music():
    global music_file
    music_file = askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
    if music_file != "":
        songs_list.insert(END, os.path.basename(music_file))

def delete_music():
    current_selection = songs_list.curselection()
    if current_selection:
        songs_list.delete(current_selection)
    else:
        songs_list.delete(1)

def callback(event):
    global music_file
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    if music_file != None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), value))
        pygame.mixer.music.play()

def play_music():
    global music_file

    if music_file != None:
        a = music_file.split(os.path.basename(music_file))[0]
        pygame.mixer.music.load(os.path.join(str(a), os.path.basename(music_file) ))
        pygame.mixer.music.play()

if __name__ == '__main__':

    root = Tk()
    root.geometry("400x400")
    root.minsize(400, 400)
    root.maxsize(400, 400)
    root.title("Simple Music Player")
    # root.wm_iconbitmap("file/music_player.ico")

    # Add ScrollBar to ListBox

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    # ListBox
    songs_list = Listbox(root, name='songs_list', yscrollcommand = scrollbar.set)
    songs_list.pack(fill=BOTH, pady=15, padx=15)
    songs_list.insert(END, "Songs List")
    songs_list.bind("<<ListboxSelect>>", callback)
    scrollbar.config(command=songs_list.yview)

    # Add & Delete Button
    frame = Frame(root)
    Button(frame, text="Add", pady=8, padx=20, font="lucida 10", command=add_music).pack(side=LEFT, padx=20)
    Button(frame, text="Delete", pady=8, padx=16, font="lucida 10", command=delete_music).pack(side=LEFT)
    frame.pack(padx=20)

    # Play Button
    Button(root, text="Play", font="lucida 10 bold", pady=8, padx=16, bg="grey", fg="white", command=play_music).pack(pady=10)

    Label(root, text="Created By Akash Gupta", font="lucida 10", bg="grey", fg="white").pack(fill=X, pady=25)
    Label(root, text="#CodeWithHarry", font="lucida 10", bg="black", fg="white").pack()

    root.mainloop()