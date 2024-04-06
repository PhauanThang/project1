
from tkinter import *
def button(event):
    global text
    text= text+str(event)
    Text.set(text)
def clear():
    global  text
    text=''
    Text.set(text)
def equal():
    try:
        global text
        text= str(eval(text))
        Text.set(text)
    except ZeroDivisionError:
        text= ' IMPOSSIBLE'
        Text.set(text)
    except SyntaxError:
        Text.set("NO Working")
window= Tk()
window.title('Calculartor')
image= PhotoImage(file='img_1.png')
window.iconphoto(True,image)
window.geometry('500x600')
text=''
Text = StringVar()
label = Label(window,font=('Ink free',27),textvariable=Text,width=14,height=2,bg='grey')
label.pack(anchor=N)
frame = Frame(window)
frame.pack()
button1 = Button(frame,text='1',height=2,width=5,font=(10),command=lambda :button(1))
button1.grid(row=0,column=0)
button2 = Button(frame,text='2',height=2,width=5,font=(10),command=lambda :button(2))
button2.grid(row=0,column=1)
button3 = Button(frame,text='3',height=2,width=5,font=(10),command=lambda :button(3))
button3.grid(row=0,column=2)
button4 = Button(frame,text='4',height=2,width=5,font=(10),command=lambda :button(4))
button4.grid(row=1,column=0)
button5 = Button(frame,text='5',height=2,width=5,font=(10),command=lambda :button(5))
button5.grid(row=1,column=1)
button6 = Button(frame,text='6',height=2,width=5,font=(10),command=lambda :button(6))
button6.grid(row=1,column=2)
button7 = Button(frame,text='7',height=2,width=5,font=(10),command=lambda :button(7))
button7.grid(row=2,column=0)
button8 = Button(frame,text='8',height=2,width=5,font=(10),command=lambda :button(8))
button8.grid(row=2,column=1)
button9 = Button(frame,text='9',height=2,width=5,font=(10),command=lambda :button(9))
button9.grid(row=2,column=2)
button0 = Button(frame,text='0',height=2,width=5,font=(10),command=lambda :button(0))
button0.grid(row=3,column=1)
buttonequal = Button(frame,text='=',height=2,width=5,font=(10),command=equal)
buttonequal.grid(row=1,column=3)
buttonclear = Button(frame,text='Clear',height=2,width=5,font=(10),command=clear)
buttonclear.grid(row=0,column=3)
multiple = Button(frame,text='*',height=2,width=5,font=(10),command=lambda :button('*'))
multiple.grid(row=2,column=3)
divisionn = Button(frame,text='/',height=2,width=5,font=(10),command=lambda :button('/'))
divisionn.grid(row=3,column=3)
summ = Button(frame,text='+',height=2,width=5,font=(10),command=lambda :button('+'))
summ.grid(row=4,column=3)
minus = Button(frame,text='-',height=2,width=5,font=(10),command=lambda :button('-'))
minus.grid(row=5,column=3)
decimal = Button(frame,text='.',height=2,width=5,font=(10),command=lambda :button('.'))
decimal.grid(row=3,column=2)
label2=Label(window,text=' Created by Xuân Thắng',font=('Impact',15))
label2.pack(side="bottom", anchor="sw")
window.mainloop()
