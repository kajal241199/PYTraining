import tkinter as tkinter 
from tkinter import ttk, messagebox
import mysql.connector

frame =tk.Tk()
frame.geometry("600x400")

def insert():
    'to insert into empmaster'
    try:
        ec = tfEC.get()
        en = tfEN.get()
        es = tfES.get()
        edob = tfEDOB.get()
        ecity = cbCity.get()
        #db cnnection
        con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="aptech",database="kajal")
        if con:
            print("Db connected")
        else:
            print("Db not connected")

