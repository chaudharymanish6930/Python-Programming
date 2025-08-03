import tkinter as tk
def update_label():
    name=entry.get()
    label.config(text=f"hello,{name}!")

root=tk.Tk()
root.title("simple GUI example")
root.geometry("250*260")

label =tk.Label(root, text="enter your name:")
label.pack(pady=10)

entry= tk.Entry(root)
entry.pack(pady=5)

button =tk.Button(root,text="sumbit",command=update_label)
button.pack(pady=10)

root.mainloop()