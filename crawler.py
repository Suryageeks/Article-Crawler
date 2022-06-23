# THIS IS AN GUI BASED CRAWLER THAT IS USE TO SCRAPE ARTICLE

from tkinter import *
from goose3 import Goose

def details():
    pages = Goose().extract(entry1.get())
    title.set(pages.title)
    meta.set(pages.meta_description)
    string = pages.cleaned_text
    file = open(entry2.get(),"w+")
    file.write(string)
    nextLine.set(string.split('\n'))
    
gui = Tk()
gui.title('Article Scraper')
gui.configure(bg='#C5F9E9')

# converting to String
title = StringVar()
meta = StringVar()
nextLine = StringVar()

# Now creating GUI for labels
Label(gui,text='URL - ',bg='#C5F9E9').grid(row=0,sticky=W)
Label(gui,text='Title - ',bg='#C5F9E9').grid(row=3,sticky=W)
Label(gui,text='Meta Info - ',bg='#C5F9E9').grid(row=4,sticky=W)
Label(gui,text='Article - ',bg='#C5F9E9').grid(row=5,sticky=W)
Label(gui,text='File Name - ',bg='#C5F9E9').grid(row=6,sticky=W)


# Now creating GUI for text-boxes
Label(gui,text="",textvariable=title,bg='#C5F9E9').grid(row=3,column=1,sticky=W)
Label(gui,text="",textvariable=meta,bg='#C5F9E9').grid(row=4,column=1,sticky=W)
Label(gui,text="",textvariable=nextLine,bg='#C5F9E9').grid(row=5,column=1,sticky=W)

# Now this is for entering website URL
entry1 = Entry(gui,width=100)
entry1.grid(row=0,column=1,sticky=W)
entry2=Entry(gui,width=100)
entry2.grid(row=6,column=1,sticky=W)

# Button for implementing the procedure
button = Button(gui,text='Submit',command=details,bg='#E2C5F9',font='bold')
button.grid(row=10,column=0,columnspan=2,rowspan=2,padx=0,pady=10,sticky=W)

#executing the tkinter application
mainloop()


