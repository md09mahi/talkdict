from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

eng=pyttsx3.init()

voice=eng.getProperty('voices')
eng.setProperty('voice',voice[0].id)
#get_close_matches(word,possibilities,n,cutoff)
#get_close_matches('appel',[' ape','apple','app'],n=3,cutoff=0.6)
def search():
    data=json.load(open('data.json'))
    word=enterwordentry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        meanwordentry.delete(1.0,END)
        for item in meaning:
            meanwordentry.insert(END,u'\u2022'+item+'\n\n')
    elif len(get_close_matches(word,data.keys()))>0:

        closematch = get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno("confirm",f'Did you mean {closematch} instead?')
        if res == True:
            enterwordentry.delete(0,END)
            enterwordentry.insert(END,closematch)
            meaning=data[closematch]

            meanwordentry.delete(1.0,END)
            for item in meaning:
                meanwordentry.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('error','the word does not exit')
            enterwordentry.delete(0,END)
            meanwordentry.delete(1.0,END)
    else:
        messagebox.showerror('information', 'the word does not exit')
        enterwordentry.delete(0, END)
        meanwordentry.delete(1.0, END)


def clear():
    enterwordentry.delete(0,END)
    meanwordentry.delete(1.0,END)
def exit():
    res=messagebox.askyesno('confirm','Do you want to exit ? ')
    if res == True:
        root. destroy()
def wordaud():
    eng.say(enterwordentry.get())
    eng.runAndWait()
def wa():
    eng.say(meanwordentry.get(1.0,END))
    eng.runAndWait()



root=Tk()
root.geometry('1000x636+100+30')
root.title("Talking Dictionary")
root.resizable(False,False)

bgimage=PhotoImage(file='bg.png')
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)

enterwordlabel=Label(root,text="ENTER WORD",font=('casteller',30,'bold'),foreground='black',background="red")
enterwordlabel.place(x=530,y=20)

enterwordentry=Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=8,relief=GROOVE)
enterwordentry.place(x=500,y=80)

searchimage=PhotoImage(file='mg.png')
searchbutton=Button(root,image=searchimage,activebackground="red",cursor='hand1',bd=8,background='blue',command=search)
searchbutton.place(x=550,y=150)

micimage=PhotoImage(file='mic.png')
micbutton=Button(root,image=micimage,command=wordaud,borderwidth=8,activebackground="red",background='blue',cursor='hand2')
micbutton.place(x=700,y=150)

meanwordlabel=Label(root,text="MEANING",font=('casteller',40,'bold'),foreground='black',background="white smoke"
                                                                                                   "")
meanwordlabel.place(x=540,y=240)

meanwordentry=Text(root,width=20,height=5,font=('arial',23,'bold'),bd=8,relief=GROOVE)
meanwordentry.place(x=500,y=320)

audioimage=PhotoImage(file='mic.png')
audiobutton=Button(root,image=audioimage,command=wa,borderwidth=0,bd=8,activebackground="red",background='blue',cursor='hand2')
audiobutton.place(x=550,y=520)

clearimage=PhotoImage(file='clear.png')
clearbutton=Button(root,image=clearimage,command=clear,borderwidth=0,bd=8,activebackground="red",background='blue',cursor='hand2')
clearbutton.place(x=650,y=520)

exitimage=PhotoImage(file='exit.png')
exitbutton=Button(root,image=exitimage,command=exit,borderwidth=0,bd=8,activebackground="red",background='blue',cursor='hand2')
exitbutton.place(x=750,y=520)
def enter_fun(event):
    searchbutton.invoke()
root.bind('<Return>',enter_fun)
root.mainloop()