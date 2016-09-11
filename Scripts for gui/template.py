#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from yattag import Doc
import datetime
from Tkinter import *

#callback function shitty but it works
def getVal(entry, textarea, body):
	body.append('<h1>'+entry.get()+'</h1>'+textarea.get("1.0", END).encode('utf8'))


#start the GUI and allow user to enter code and text for creating the blog
root = Tk()
root.geometry("800x600")
body =[];

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
get_value = Button(frame, text="Put Text", command=lambda: getVal(entry, textarea, body))
get_value.pack()
button = Button(frame, text="QUIT", fg="red", command=frame.quit)
button.pack()

#Close GUI
root.mainloop()
root.destroy()

#Prepare body and Doc Formatting
body=body[0]
doc, tag, text = Doc().tagtext()

#Template the only thing that needs to be changed is the body
doc.asis('<!DOCTYPE html>')
with tag('html'):
	with tag('head'):
		doc.asis('<meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="author" content="Eli Gonzalez and Patricio Torres"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Blog Post</title><meta name="description" content="Blog Post"><script src="https://use.fontawesome.com/454d2d96bc.js"></script><link rel="stylesheet prefetch" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link rel="stylesheet" href="index.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
	with tag(body):
		doc.asis('<!-- header section --><div class="container" id="header-section"><nav class="navbar navbar-default navbar-fixed-top" role="navigation"><div class="navbar-header"><button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button></div><a class="navbar-brand" href="#">Brand</a><div class="navbar-collapse collapse"><ul class="nav navbar-nav navbar-left"><li><a href="index.html">Home</a></li><li><a href="about.html">About Me</a></li></ul><ul class="nav navbar-nav navbar-right" id="pad-left"><li class="active"><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact Me</a></li></ul></div></nav></div><!-- body section -->')
		with tag('div', klass="container", id="body-section"):
			doc.asis(body)
		doc.asis('<!-- footer section --><div class="container" id="footer-section"><footer><div class="row"><div class="col-md-2 col-sm-2 col-xs-2"><a href="https://www.facebook.com/" target="_blank"><i class="fa fa-facebook"> My Facebook</i></a></div><div class="col-md-2 col-sm-2 col-xs-2"><a href="https://www.instagram.com" target="_blank"><i class="fa fa-instagram"> My Instagram</i></a></div></div><div class="footer-copy">Copyright © 2016 Leon Photography</div></footer></div>')

print(doc.getvalue())

#Get timestamp and create the file write to it and close program
def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
	return datetime.datetime.now().strftime(fmt).format(fname=fname)

html_file = open(timeStamped('.html'), 'w')

html_file.write(doc.getvalue())

html_file.close()

