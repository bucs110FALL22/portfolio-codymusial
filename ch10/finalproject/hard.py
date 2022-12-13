from tkinter import *
import random
from tkinter import messagebox
import time
import pygame

pygame.init()

timer = pygame.time.Clock()
init_time = timer.tick()

root = Tk()
root.title('The Ultimate Challenge!')

root.geometry("1000x1000")


global winner, matches
winner = 0


matches = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32]

random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}



def reset():
	global matches, winner
	winner = 0
	
	matches = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32]
	
	random.shuffle(matches)

	my_label.config(text="")

	button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63]
	
	for button in button_list:
		button.config(text=" ", bg="SystemButtonFace", state="normal")



def win():
	my_label.config(text="Congratulations! You Win!!!")
	button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63]

	for button in button_list:
		button.config(bg="green")


  print(timeToFinish())

def timeToFinish():
  global timer, init_time
  completion_time = (timer.tick()-init_time)/1000
  minutes = 0
  if completion_time >= 60:
    minutes = completion_time//60
  seconds = int(completion_time)%60
  minutes_text = ''
  if minutes:
    minutes_text = f"{minutes} minutes and "
  completion_text = f"It took {minutes_text}{seconds} seconds to complete the game."
  return completion_text
  

def button_click(b, number):
	global count, answer_list, answer_dict, winner

	if b["text"] == ' ' and count < 2:
		b["text"] = matches[number]
		answer_list.append(number)
		answer_dict[b] = matches[number]
		count += 1

	if len(answer_list) == 2:
		if matches[answer_list[0]] == matches[answer_list[1]]:
			my_label.config(text="MATCH!")
			for key in answer_dict:
				key["state"] = "disabled"
			count = 0
			answer_list = []
			answer_dict = {}
			winner += 1
			if winner == 32:
				win()
        
		else:
			count = 0
			answer_list = []
			messagebox.showinfo("Incorrect!", "Incorrect")

			
			for key in answer_dict:
				key["text"] = " "

			answer_dict = {}



b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b0, 0), relief="groove")
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b1, 1), relief="groove")
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b2, 2), relief="groove")
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b3, 3), relief="groove")
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b4, 4), relief="groove")
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b5, 5), relief="groove")
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b6, 6), relief="groove")
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b7, 7), relief="groove")
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b8, 8), relief="groove")
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b9, 9), relief="groove")
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b10, 10), relief="groove")
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b11, 11), relief="groove")
b12 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b12, 12), relief="groove")
b13 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b13, 13), relief="groove")
b14 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b14, 14), relief="groove")
b15 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b15, 15), relief="groove")
b16 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b16, 16), relief="groove")
b17 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b17, 17), relief="groove")
b18 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b18, 18), relief="groove")
b19 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b19, 19), relief="groove")
b20 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b20, 20), relief="groove")
b21 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b21, 21), relief="groove")
b22 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b22, 22), relief="groove")
b23 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b23, 23), relief="groove")
b24 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b24, 24), relief="groove")
b25 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b25, 25), relief="groove")
b26 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b26, 26), relief="groove")
b27 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b27, 27), relief="groove")
b28 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b28, 28), relief="groove")
b29 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b29, 29), relief="groove")
b30 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b30, 30), relief="groove")
b31 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b31, 31), relief="groove")
b32 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b32, 32), relief="groove")
b33 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b33, 33), relief="groove")
b34 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b34, 34), relief="groove")
b35 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b35, 35), relief="groove")
b36 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b36, 36), relief="groove")
b37 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b37, 37), relief="groove")
b38 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b38, 38), relief="groove")
b39 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b39, 39), relief="groove")
b40 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b40, 40), relief="groove")
b41 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b41, 41), relief="groove")
b42 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b42, 42), relief="groove")
b43 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b43, 43), relief="groove")
b44 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b44, 44), relief="groove")
b45 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b45, 45), relief="groove")
b46 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b46, 46), relief="groove")
b47 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b47, 47), relief="groove")
b48 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b48, 48), relief="groove")
b49 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b49, 49), relief="groove")
b50 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b50, 50), relief="groove")
b51 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b51, 51), relief="groove")
b52 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b52, 52), relief="groove")
b53 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b53, 53), relief="groove")
b54 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b54, 54), relief="groove")
b55 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b55, 55), relief="groove")
b56 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b56, 56), relief="groove")
b57 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b57, 57), relief="groove")
b58 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b58, 58), relief="groove")
b59 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b59, 59), relief="groove")
b60 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b60, 60), relief="groove")
b61 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b61, 61), relief="groove")
b62 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b62, 62), relief="groove")
b63 = Button(my_frame, text=' ', font=("Helvetica", 20), height=2, width=4, command=lambda: button_click(b63, 63), relief="groove")

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=0, column=4)
b5.grid(row=0, column=5)
b6.grid(row=0, column=6)
b7.grid(row=0, column=7) 

b8.grid(row=1, column=0)
b9.grid(row=1, column=1)
b10.grid(row=1, column=2)
b11.grid(row=1, column=3)
b12.grid(row=1, column=4)
b13.grid(row=1, column=5)
b14.grid(row=1, column=6)
b15.grid(row=1, column=7)

b16.grid(row=2, column=0)
b17.grid(row=2, column=1)
b18.grid(row=2, column=2)
b19.grid(row=2, column=3)
b20.grid(row=2, column=4)
b21.grid(row=2, column=5)
b22.grid(row=2, column=6)
b23.grid(row=2, column=7)

b24.grid(row=3, column=0)
b25.grid(row=3, column=1)
b26.grid(row=3, column=2)
b27.grid(row=3, column=3)
b28.grid(row=3, column=4)
b29.grid(row=3, column=5)
b30.grid(row=3, column=6)
b31.grid(row=3, column=7) 

b32.grid(row=4, column=0)
b33.grid(row=4, column=1)
b34.grid(row=4, column=2)
b35.grid(row=4, column=3)
b36.grid(row=4, column=4)
b37.grid(row=4, column=5)
b38.grid(row=4, column=6)
b39.grid(row=4, column=7) 

b40.grid(row=5, column=0)
b41.grid(row=5, column=1)
b42.grid(row=5, column=2)
b43.grid(row=5, column=3)
b44.grid(row=5, column=4)
b45.grid(row=5, column=5)
b46.grid(row=5, column=6)
b47.grid(row=5, column=7) 

b48.grid(row=6, column=0)
b49.grid(row=6, column=1)
b50.grid(row=6, column=2)
b51.grid(row=6, column=3)
b52.grid(row=6, column=4)
b53.grid(row=6, column=5)
b54.grid(row=6, column=6)
b55.grid(row=6, column=7)

b56.grid(row=7, column=0)
b57.grid(row=7, column=1)
b58.grid(row=7, column=2)
b59.grid(row=7, column=3)
b60.grid(row=7, column=4)
b61.grid(row=7, column=5)
b62.grid(row=7, column=6)
b63.grid(row=7, column=7)


my_label = Label(root, text="")
my_label.pack(pady=20)

my_menu = Menu(root)
root.config(menu=my_menu)

option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

root.mainloop()