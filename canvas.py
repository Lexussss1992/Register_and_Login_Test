import tkinter as tk


def create_app():
    window = tk.Tk()
    window.geometry("7000x600+0+0")
    window.title("GUI Product shop")
    generate_button = tk.Button(window, text="Login", height=1)
    generate_button.place(x=0, y=0)
    return tk


create_app().mainloop()