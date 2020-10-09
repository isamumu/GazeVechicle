from tkinter import *
import tkinter as tk

def UP( event ):
    print( "up clicked" )  

def DOWN( event ):
    print( "down clicked" )  

def LEFT( event ):
    print( "left clicked" )  

def RIGHT( event ):
    print( "right clicked" )  


window = Tk()

# UP BUTTONS
button = Button(window,text='UP',width=20, height=2)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.config(activebackground='#FF0000')
button.config(activeforeground='#fffb1f')
button.grid(row=0, column=1)

button.bind( "<Button>", UP )   

button10 = Button(window,width=20, height=2)
button10.config(font=('Ink Free',50,'bold'))
button10.config(bg='#ff6200')
button10.config(fg='#fffb1f')
button10.config(activebackground='#FF0000')
button10.config(activeforeground='#fffb1f')
button10.grid(row=1, column=1)

button10.bind( "<Button>", UP )   

# DOWN BUTTONS
button9 = Button(window,text='DOWN',width=20, height=2)
button9.config(font=('Ink Free',50,'bold'))
button9.config(bg='#FF0000')
button9.config(fg='#fffb1f')
button9.config(activebackground='#FF0000')
button9.config(activeforeground='#fffb1f')
button9.grid(row=3, column=1)

button9.bind( "<Button>", DOWN )   

button8 = Button(window,width=20, height=2)
button8.config(font=('Ink Free',50,'bold'))
button8.config(bg='#FF0000')
button8.config(fg='#fffb1f')
button8.config(activebackground='#FF0000')
button8.config(activeforeground='#fffb1f')
button8.grid(row=2, column=1)

button8.bind( "<Button>", DOWN )   

# RIGHT BUTTONS
button2 = Button(window,text='RIGHT',width=10, height=2)
button2.config(font=('Ink Free',50,'bold'))
button2.config(bg='#ff8280')
button2.config(fg='#fffb1f')
button2.config(activebackground='#FF0000')
button2.config(activeforeground='#fffb1f')
button2.grid(row=1, column=2)

button2.bind( "<Button>", RIGHT )   

button4 = Button(window,width=10, height=2)
button4.config(font=('Ink Free',50,'bold'))
button4.config(bg='#ff8280')
button4.config(fg='#fffb1f')
button4.config(activebackground='#FF0000')
button4.config(activeforeground='#fffb1f')
button4.grid(row=0, column=2)

button4.bind( "<Button>", RIGHT )   

button7 = Button(window,width=10, height=2)
button7.config(font=('Ink Free',50,'bold'))
button7.config(bg='#ff8280')
button7.config(fg='#fffb1f')
button7.config(activebackground='#FF0000')
button7.config(activeforeground='#fffb1f')
button7.grid(row=2, column=2)

button7.bind( "<Button>", RIGHT )   

button12 = Button(window,width=10, height=2)
button12.config(font=('Ink Free',50,'bold'))
button12.config(bg='#ff8280')
button12.config(fg='#fffb1f')
button12.config(activebackground='#FF0000')
button12.config(activeforeground='#fffb1f')
button12.grid(row=3, column=2)

button12.bind( "<Button>", RIGHT )   

# LEFT BUTTONS
button3 = Button(window,text='LEFT',width=10, height=2)
button3.config(font=('Ink Free',50,'bold'))
button3.config(bg='#ff8280')
button3.config(fg='#fffb1f')
button3.config(activebackground='#FF0000')
button3.config(activeforeground='#fffb1f')
button3.grid(row=1, column=0)

button3.bind( "<Button>", LEFT )   

button5 = Button(window,width=10, height=2)
button5.config(font=('Ink Free',50,'bold'))
button5.config(bg='#ff8280')
button5.config(fg='#fffb1f')
button5.config(activebackground='#FF0000')
button5.config(activeforeground='#fffb1f')
button5.grid(row=0, column=0)

button5.bind( "<Button>", LEFT )   

button6 = Button(window,width=10, height=2)
button6.config(font=('Ink Free',50,'bold'))
button6.config(bg='#ff8280')
button6.config(fg='#fffb1f')
button6.config(activebackground='#FF0000')
button6.config(activeforeground='#fffb1f')
button6.grid(row=2, column=0)

button6.bind( "<Button>", LEFT )   

button14 = Button(window,width=10, height=2)
button14.config(font=('Ink Free',50,'bold'))
button14.config(bg='#ff8280')
button14.config(fg='#fffb1f')
button14.config(activebackground='#FF0000')
button14.config(activeforeground='#fffb1f')
button14.grid(row=3, column=0)

button14.bind( "<Button>", LEFT )   




window.mainloop()