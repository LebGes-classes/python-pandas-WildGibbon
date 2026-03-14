import tkinter as tk
import os

window = tk.Tk()


def f(timing):
    os.system(f"shutdown -s -t {int(timing * 3600)}")


window.geometry("300x200")
window.title("ЛИКВИДИРОВАН")

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Поставить таймер(в часах)", command=lambda: f(float(entry.get()))).pack()
tk.Button(window, text="Otmena", command=lambda: os.system("shutdown -a")).pack()


window.mainloop()
