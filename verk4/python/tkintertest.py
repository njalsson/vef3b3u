import tkinter as tk

root = tk.Tk()


logo = logo = tk.PhotoImage(file="../images/ethereum.png")


w1 = tk.Label(root, image=logo).pack(side="right")

nr1 = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""


nr2 = """this is a test, no need to panic """
w1 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=nr1,
              font = "Helvetica 16 bold italic").pack(side="left")
w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=nr2,
              font = "Helvetica 16 bold italic").pack(side="left")



root.mainloop()

