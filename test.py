import tkinter as tk
# print(tk.TkVersion)
root = tk.Tk()
root.geometry('300x300')

btn = tk.Button(root, text='hello', fg='red')
btn.pack()

root.mainloop()