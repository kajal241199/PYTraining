import Tkinter as tk

def click():
    'to perform acton on button click'
    n1 = float(tf1.get())
    n2 = float(tf2.get())
    rs = n1+n2
    tf3.insert(0, rs)

#creating a frame
root = tk.Tk()
#setting frame size
root.geometry("600x500")
#creating TextField
tf1 = tk.Entry(root)
tf2 = tk.Entry(root)
tf3 = tk.Entry(root)
#creating button
btn = tk.Button(root, text="CLICK", command=click)
#adding controls over frame
tf1.pack()
tf2.pack()
tf3.pack()
btn.pack()
#showing frame
root.mainloop()