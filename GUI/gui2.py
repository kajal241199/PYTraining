import Tkinter as tk
import Tkinter 
import tkMessageBox
import Tkinter
import ttk

def click():
    'to perform acton on button click'
    n1 = float(tf1.get())
    n2 = float(tf2.get())
    #getting current item from combobox
    item = cb1.get()
    if item=="+":
        rs = n1+n2
        tkMessageBox.showinfo("MessageBox", "addition is : " +str(rs))
    elif item=="-":
        rs = n1-n2
        tkMessageBox.showinfo("MessageBox", "Subtaction is : " +str(rs))
    elif item=="x":
        rs = n1*n2
        tkMessageBox.showinfo("MessageBox", "multiplication is : " +str(rs))
    elif item=="/":
        rs = n1/n2
        tkMessageBox.showinfo("MessageBox", "divsion is : " +str(rs))
    else:
        tkMessageBox.showinfo("MessageBox", " select an action ")
    #setting result into textfield
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
ls = ['Select Action', '+', '-', 'x', '/']
#creating combo box
cb1 = ttk.Combobox(root, values=ls, state='readonly')
cb1.current(0)
#adding controls over frame
cb1.pack()
tf1.pack()
tf2.pack()
tf3.pack()
btn.pack()
#showing frame
root.mainloop()