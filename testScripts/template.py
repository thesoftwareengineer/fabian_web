#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yattag import Doc
import datetime
from Tkinter import *

#callback function shitty but it works
def getVal(entry, textarea):
    doc, tag, text = Doc().tagtext()

    #Template the only thing that needs to be changed is the body

    with tag('h1'):
        text(entry.get())
    with tag('p', klass='post-text'):
        doc.asis(textarea.get("1.0", END).encode('utf8'))

    print(doc.getvalue())

    #Get timestamp and create the file write to it and close program
    def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
        return datetime.datetime.now().strftime(fmt).format(fname=fname)

    html_file = open('../blog_post/' + timeStamped('.html'), 'w')

    html_file.write(doc.getvalue())

    html_file.close()

#start the GUI and allow user to enter code and text for creating the blog
root = Tk()
root.geometry("800x600")
#body =[];

#create a frame for the GUI
frame = Frame(root)
frame.pack()

#Start by asking for Title
var = StringVar()
label = Message(frame, textvariable=var, relief=RAISED )
var.set("Title")
label.pack()

#Entry for the title
entry = Entry(frame)
entry.pack()

#Ask for the enry of blog posting
var2 = StringVar()
label2 = Message(frame, textvariable=var2, relief=RAISED )
var2.set("Enter the Blog Posting")
label2.pack()

#Get bloposting
textarea = Text(frame, height=30, width=40)
textarea.pack()

#Create two buttons a quit and Put text button.
get_value = Button(frame, text="Put Text", command=lambda: getVal(entry, textarea))
get_value.pack()
button = Button(frame, text="QUIT", fg="red", command=frame.quit)
button.pack()

#Close GUI
root.mainloop()
root.destroy()

#Prepare body and Doc Formatting
#body=body[0]


