from textwrap import fill
import pyshorteners
from tkinter import *

window = Tk()
window.title("URL Shortener")
window.geometry('400x400')
window.configure(bg="turquoise")

#shortener
def short():
    url=entry.get()
    surl=pyshorteners.Shortener().tinyurl.short(url)
    entry1.insert(END,surl)
    
    
#Label
lab= Label(window,text="Enter the URL to be shortened",font=('calibri 22 bold'),bg='beige',fg='blue')
lab.pack(fill="x") 

 #entry
entry=Entry(window,font=('times 12 '),bd=2, width=45)
entry.pack(pady=40)

#button
Button(window,text="Click to shorten", font=('impack 13 bold'),width=20, bg="blue", fg="white", command=short).pack()

#entry
entry1=Entry(window,font=('courier 11'),bd=0,width=30, bg="turquoise")
entry1.pack(pady=40)

window.mainloop()