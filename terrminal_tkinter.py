from tkinter import *

# Settings
Fullscreen = FALSE

def execute_command(event):
    command = terminalWidget.get("end-2l linestart", "end-1c").strip()  # Pobierz ostatnią linię
    if command == "/exit":
        window.quit()
    elif command == "/fullscreen":
        global Fullscreen
        Fullscreen = not Fullscreen
        window.attributes("-fullscreen", Fullscreen)

window = Tk()
window.geometry("800x600")
window.config(background="#141414")
window.attributes("-fullscreen", Fullscreen)

# Terminal widget
terminalWidget = Text(bg="#141414", fg="white", font=("Consolas", 12), insertbackground="white")
#terminalWidget.insert(END, "Terminal> ")
terminalWidget.focus()
terminalWidget.bind("<Return>", execute_command)
terminalWidget.pack(expand=True, fill=BOTH)

mainloop()

