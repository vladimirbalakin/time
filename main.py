from tkinter import Tk, Label, Button

import battle

root = Tk()
root.title("Time game 1.0.0")
root.geometry("640x480")


def start_battle():
    battle.start()


caption = Label(root, text="Time game 1.0.0", font=("Arial Bold", 50))
caption.grid(column=0, row=0)

solar_system = Button(root, text="Battle", command=start_battle)
solar_system.grid(column=0, row=1)

root.mainloop()
