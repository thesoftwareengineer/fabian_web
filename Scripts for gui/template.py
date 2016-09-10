#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from yattag import Doc
import datetime

doc, tag, text = Doc().tagtext()
body = "Hello World"
doc.asis('<!DOCTYPE html>')
with tag('html'):
	with tag('head'):
		doc.asis('<meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="author" content="Eli Gonzalez and Patricio Torres"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Blog Post</title><meta name="description" content="Blog Post"><script src="https://use.fontawesome.com/454d2d96bc.js"></script><link rel="stylesheet prefetch" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><link rel="stylesheet" href="index.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
	with tag('body'):
		doc.asis('<!-- header section --><div class="container" id="header-section"><nav class="navbar navbar-default navbar-fixed-top" role="navigation"><div class="navbar-header"><button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button></div><a class="navbar-brand" href="#">Brand</a><div class="navbar-collapse collapse"><ul class="nav navbar-nav navbar-left"><li><a href="index.html">Home</a></li><li><a href="about.html">About Me</a></li></ul><ul class="nav navbar-nav navbar-right" id="pad-left"><li class="active"><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact Me</a></li></ul></div></nav></div><!-- body section -->')
		with tag('div', klass="container", id="body-section"):
			text(body)
			doc.asis('<!-- footer section --><div class="container" id="footer-section"><footer><div class="row"><div class="col-md-2 col-sm-2 col-xs-2"><a href="https://www.facebook.com/" target="_blank"><i class="fa fa-facebook"> My Facebook</i></a></div><div class="col-md-2 col-sm-2 col-xs-2"><a href="https://www.instagram.com" target="_blank"><i class="fa fa-instagram"> My Instagram</i></a></div></div><div class="footer-copy">Copyright © 2016 Leon Photography</div></footer></div>')

print(doc.getvalue())

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
	return datetime.datetime.now().strftime(fmt).format(fname=fname)

html_file = open(timeStamped('.html'), 'w')

html_file.write(doc.getvalue())

html_file.close()