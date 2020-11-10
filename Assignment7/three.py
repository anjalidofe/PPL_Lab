#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.show()

#observe: All class names are in "Title case".
#Line below: b becomes an object of type Button with the text
# Hello PPL on in.
b = gtk.Button("Hello PPL")

# this adds the button to the window. Try commenting the line below.
w.add(b)

#the button should also show itself. Try commenting the line below and see the result.
b.show()

#Now we'll set some "event handlers"
def hello(widget):
	print "hello there!"
#in the above, observe what is printed for p. Note that it is the object (self) getting passed.

b.connect("clicked", hello) # "clicked" has been pre-defined by gtk to mean left-mouse click.
gtk.main()
# Now try clicking on the button "Hello PPL" 
