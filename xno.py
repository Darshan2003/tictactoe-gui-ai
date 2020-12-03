from tkinter import *
from tkinter.messagebox import *


p=0
a1=0
a2=-1
a3=3
a4=4
a5=5
a6=6
a7=7
a8=8
a9=9
won=0

p1=0
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0
b8=0
b9=0

def f3():
    comp.deiconify()
    ask.withdraw()

def f4(f):
    global p1
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    global won

    if p1==0:

        if f==1:
            if b1==0:
                cbtn1['text']="X"
                p1=1
                b1=1

        if f==2:
            if b2==0:
                cbtn2['text']="X"
                p1=1
                b2=1
        if f==3:
            if b3==0:
                cbtn3['text']="X"
                p1=1
                b3=1

        if f==4:
            if b4==0:
                cbtn4['text']="X"
                p1=1
                b4=1
        if f==5:
            if b5==0:
                cbtn5['text']="X"
                p1=1
                b5=1
        if f==6:
            if b6==0:
                cbtn6['text']="X"
                p1=1
                b6=1
        if f==7:
            if b7==0:
                cbtn7['text']="X"
                p1=1
                b7=1

        if f==8:
            if b8==0:
                cbtn8['text']="X"
                p1=1
                b8=1
        if f==9:
            if b9==0:
                cbtn9['text']="X"
                p1=1
                b9=1


    if p1==1:
        if (b1==1 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==1 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==1 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0 and b9==1):
            cbtn5['text']="O"
            b5=2
        elif (b1==1 and b2==0 and b3==0 and b4==0 and b5==2 and b6==1 and b7==0 and b8==0 and b9==0) or(b1==2 and b2==0 and b3==0 and b4==0 and b5==1 and b6==0 and b7==0 and b8==0 and b9==1):
            cbtn3['text']="O"
            b3=2
        elif (b1==0 and b2==1 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==1 and b5==0 and b6==0 and b7==0 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==0 and b6==1 and b7==0 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==0 and b6==0 and b7==0 and b8==1 and b9==0):
            cbtn5['text']="O"
            b5=2
        elif (b1==1 and b2==0 and b3==0 and b4==0 and b5==2 and b6==0 and b7==0 and b8==1 and b9==0):
            cbtn7['text']="O"
            b7=2
        elif (b1==0 and b2==0 and b3==1 and b4==0 and b5==2 and b6==0 and b7==0 and b8==1 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==2 and b6==1 and b7==1 and b8==0 and b9==0) or (b1==0 and b2==0 and b3==0 and b4==0 and b5==2 and b6==1 and b7==0 and b8==1 and b9==0):
            cbtn9['text']="O"
            b9=2
        elif (b1==1 and b2==0 and b3==0 and b4==0 and b5==2 and b6==0 and b7==0 and b8==0 and b9==1) or (b1==0 and b2==0 and b3==1 and b4==0 and b5==2 and b6==0 and b7==1 and b8==0 and b9==0):
            cbtn2['text']="O"
            b2=2
        elif (b1==2 and b2==2 and b3==0) or (b1==2 and b3==2 and b2==0) or (b2==2 and b3==2 and b1==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b2==0:
                cbtn2['text']="O"
                b2=2
            elif b3==0:
                cbtn3['text']="O"
                b3=2
        elif (b4==2 and b5==2 and b6==0) or (b5==2 and b6==2 and b4==0) or (b4==2 and b6==2 and b5==0):
            if b4==0:
                cbtn4['text']="O"
                b4=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b6==0:
                cbtn6['text']="O"
                b6=2
        elif (b7==2 and b8==2 and b9==0) or (b8==2 and b9==2 and b7==0) or (b7==2 and b9==2 and b8==0):
            if b7==0:
                cbtn7['text']="O"
                b7=2
            elif b8==0:
                cbtn8['text']="O"
                b8=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b1==2 and b4==2 and b7==0 ) or (b4==2 and b7==2 and b1==0) or (b1==2 and b7==2 and b4==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b4==0:
                cbtn4['text']="O"
                b4=2
            elif b7==0:
                cbtn7['text']="O"
                b7=2
        elif (b2==2 and b5==2 and b8==0 ) or (b5==2 and b8==2 and b2==0) or (b2==2 and b8==2 and b5==0):
            if b2==0:
                cbtn2['text']="O"
                b2=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b8==0:
                cbtn8['text']="O"
                b8=2
        elif (b3==2 and b6==2 and b9==0 ) or (b6==2 and b9==2 and b3==0) or (b3==2 and b9==2 and b6==0):
            if b3==0:
                cbtn3['text']="O"
                b3=2
            elif b6==0:
                cbtn6['text']="O"
                b6=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b1==2 and b5==2 and b9==0 ) or (b5==2 and b9==2 and b1==0) or (b1==2 and b9==2 and b5==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b3==2 and b5==2  and b7==0) or (b5==2 and b7==2 and b3==0) or (b3==2 and b7==2 and b5==0):
            if b3==0:
                cbtn3['text']="O"
                b3=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b7==0:
                cbtn7['text']="O"
                b7=2

        elif (b1==1 and b2==1 and b3==0) or (b1==1 and b3==1 and b2==0) or (b2==1 and b3==1 and b1==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b2==0:
                cbtn2['text']="O"
                b2=2
            elif b3==0:
                cbtn3['text']="O"
                b3=2
        elif (b4==1 and b5==1 and b6==0) or (b5==1 and b6==1 and b4==0) or (b4==1 and b6==1 and b5==0):
            if b4==0:
                cbtn4['text']="O"
                b4=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b6==0:
                cbtn6['text']="O"
                b6=2
        elif (b7==1 and b8==1 and b9==0) or (b8==1 and b9==1 and b7==0) or (b7==1 and b9==1 and b8==0):
            if b7==0:
                cbtn7['text']="O"
                b7=2
            elif b8==0:
                cbtn8['text']="O"
                b8=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b1==1 and b4==1 and b7==0 ) or (b4==1 and b7==1 and b1==0) or (b1==1 and b7==1 and b4==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b4==0:
                cbtn4['text']="O"
                b4=2
            elif b7==0:
                cbtn7['text']="O"
                b7=2
        elif (b2==1 and b5==1 and b8==0 ) or (b5==1 and b8==1 and b2==0) or (b2==1 and b8==1 and b5==0):
            if b2==0:
                cbtn2['text']="O"
                b2=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b8==0:
                cbtn8['text']="O"
                b8=2
        elif (b3==1 and b6==1 and b9==0 ) or (b6==1 and b9==1 and b3==0) or (b3==1 and b9==1 and b6==0):
            if b3==0:
                cbtn3['text']="O"
                b3=2
            elif b6==0:
                cbtn6['text']="O"
                b6=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b1==1 and b5==1 and b9==0 ) or (b5==1 and b9==1 and b1==0) or (b1==1 and b9==1 and b5==0):
            if b1==0:
                cbtn1['text']="O"
                b1=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b9==0:
                cbtn9['text']="O"
                b9=2
        elif (b3==1 and b5==1  and b7==0) or (b5==1 and b7==1 and b3==0) or (b3==1 and b7==1 and b5==0):
            if b3==0:
                cbtn3['text']="O"
                b3=2
            elif b5==0:
                cbtn5['text']="O"
                b5=2
            elif b7==0:
                cbtn7['text']="O"
                b7=2
        elif b1==0:
            cbtn1['text']="O"
            b1=2
        elif b2==0:
            cbtn2['text']="O"
            b2=2
        elif b3==0:
            cbtn3['text']="O"
            b3=2
        elif b4==0:
            cbtn4['text']="O"
            b4=2
        elif b5==0:
            cbtn5['text']="O"
            b5=2
        elif b6==0:
            cbtn6['text']="O"
            b6=2
        elif b7==0:
            cbtn7['text']="O"
            b7=2
        elif b8==0:
            cbtn8['text']="O"
            b8=2
        elif b9==0:
            cbtn9['text']="O"
            b9=2



        p1=0

    if b1==b2 and b2==b3 and b1==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b1==b5 and b5==b9 and b1==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b1==b4 and b4==b7 and b1==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b4==b5 and b5==b6 and b4==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b7==b8 and b8==b9 and b7==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b3==b6 and b6==b9 and b3==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b3==b5 and b5==b7 and b3==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif b2==b5 and b5==b8 and b2==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1

    elif b1!=0 and b2!=0 and b3!=0 and b4!=0 and b5!=0 and b6!=0 and b7!=0 and b8!=0 and b9!=0:
        showinfo("Draw","Game Draw!")
        won=1
    elif b1==b2 and b2==b3 and b1==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1


    elif b1==b5 and b5==b9 and b1==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b1==b4 and b4==b7 and b1==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b4==b5 and b5==b6 and b4==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b7==b8 and b8==b9 and b7==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b3==b6 and b6==b9 and b3==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b3==b5 and b5==b7 and b3==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif b2==b5 and b5==b8 and b2==2:
        showinfo("Congrats!","Player 2 or O won!")
        won=1



    if won==1:
        cbtn1['text']=""
        cbtn2['text']=""
        cbtn3['text']=""
        cbtn4['text']=""
        cbtn5['text']=""
        cbtn6['text']=""
        cbtn7['text']=""
        cbtn8['text']=""
        cbtn9['text']=""
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        won=0

        comp.withdraw()
        ask.deiconify()



def f2():
    root.deiconify()
    ask.withdraw()

def f1(flag):
    global p
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    global won

    if flag==1:
        if p==0 and a1==0:
            btn1['text']="X"
            p=1
            a1=1
        elif p==1 and a1==0:
            btn1['text']="O"
            p=0
            a1=2
        else:
            NONE

    if flag==2:
        if p==0 and a2==-1:
            btn2['text']="X"
            p=1
            a2=1
        elif p==1 and a2==-1:
            btn2['text']="O"
            p=0
            a2=2
        else:
            NONE

    if flag==3:
        if p==0 and a3==3:
            btn3['text']="X"
            p=1
            a3=1
        elif p==1 and a3==3:
            btn3['text']="O"
            p=0
            a3=2
        else:
            NONE

    if flag==4:
        if p==0 and a4==4:
            btn4['text']="X"
            p=1
            a4=1
        elif p==1 and a4==4:
            btn4['text']="O"
            p=0
            a4=2
        else:
            NONE

    if flag==5:
        if p==0 and a5==5:
            btn5['text']="X"
            p=1
            a5=1
        elif p==1 and a5==5:
            btn5['text']="O"
            p=0
            a5=2
        else:
            NONE

    if flag==6:
        if p==0 and a6==6:
            btn6['text']="X"
            p=1
            a6=1
        elif p==1 and a6==6:
            btn6['text']="O"
            p=0
            a6=2
        else:
            NONE

    if flag==7:
        if p==0 and a7==7:
            btn7['text']="X"
            p=1
            a7=1
        elif p==1 and a7==7:
            btn7['text']="O"
            p=0
            a7=2
        else:
            NONE

    if flag==8:
        if p==0 and a8==8:
            btn8['text']="X"
            p=1
            a8=1
        elif p==1 and a8==8:
            btn8['text']="O"
            p=0
            a8=2
        else:
            NONE

    if flag==9:
        if p==0 and a9==9:
            btn9['text']="X"
            p=1
            a9=1
        elif p==1 and a9==9:
            btn9['text']="O"
            p=0
            a9=2
        else:
            NONE

    if a1==a2 and a2==a3 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1


    elif a1==a5 and a5==a9 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a1==a4 and a4==a7 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a4==a5 and a5==a6 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a7==a8 and a8==a9 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a3==a6 and a6==a9 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a3==a5 and a5==a7 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a2==a5 and a5==a8 and p==1:
        showinfo("Congrats!","Player 1 or X won!")
        won=1
    elif a1==a2 and a2==a3 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a1==a5 and a5==a9 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a1==a4 and a4==a7 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a4==a5 and a5==a6 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a7==a8 and a8==a9 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a3==a6 and a6==a9 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a3==a5 and a5==a7 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a2==a5 and a5==a8 and p==0:
        showinfo("Congrats!","Player 2 or O won!")
        won=1
    elif a1!=0 and a2!=-1 and a3!=3 and a4!=4 and a5!=5 and a6!=6 and a7!=7 and a8!=8 and a9!=9:
        showinfo("Draw","Game Draw!")
        won=1

    if won==1:
        btn1['text']=""
        btn2['text']=""
        btn3['text']=""
        btn4['text']=""
        btn5['text']=""
        btn6['text']=""
        btn7['text']=""
        btn8['text']=""
        btn9['text']=""
        p=0
        a1=0
        a2=-1
        a3=3
        a4=4
        a5=5
        a6=6
        a7=7
        a8=8
        a9=9
        won=0

        root.withdraw()
        ask.deiconify()

ask=Tk()
ask.title("Tic tac toe")
ask.geometry("145x130+400+200")
ask.resizable(False,False)
ask_btn1=Button(ask,text="1 player",font=('arial',10,'bold'),command=f3)
ask_btn2=Button(ask,text="2 player",font=('arial',10,'bold'),command=f2)
ask_btn1.pack(pady=5)
ask_btn2.pack(pady=5)
root=Toplevel(ask)
root.title("Tic tac toe")
root.geometry("145x130+400+200")
root.resizable(False,False)
btn1=Button(root,text="",height=2,width=5,command=lambda flag=1: f1(flag))
btn2=Button(root,text="",height=2,width=5,command=lambda flag=2: f1(flag))
btn3=Button(root,text="",height=2,width=5,command=lambda flag=3: f1(flag))
btn4=Button(root,text="",height=2,width=5,command=lambda flag=4: f1(flag))
btn5=Button(root,text="",height=2,width=5,command=lambda flag=5: f1(flag))
btn6=Button(root,text="",height=2,width=5,command=lambda flag=6: f1(flag))
btn7=Button(root,text="",height=2,width=5,command=lambda flag=7: f1(flag))
btn8=Button(root,text="",height=2,width=5,command=lambda flag=8: f1(flag))
btn9=Button(root,text="",height=2,width=5,command=lambda flag=9: f1(flag))


btn1.place(x=5,y=5)
btn2.place(x=50,y=5)
btn3.place(x=95,y=5)
btn4.place(x=5,y=45)
btn5.place(x=50,y=45)
btn6.place(x=95,y=45)
btn7.place(x=5,y=85)
btn8.place(x=50,y=85)
btn9.place(x=95,y=85)

root.withdraw()
comp=Toplevel(ask)
comp.title("Tic tac toe")
comp.geometry("145x130+400+200")
comp.resizable(False,False)
cbtn1=Button(comp,text="",height=2,width=5,command=lambda f=1: f4(f))
cbtn2=Button(comp,text="",height=2,width=5,command=lambda f=2: f4(f))
cbtn3=Button(comp,text="",height=2,width=5,command=lambda f=3: f4(f))
cbtn4=Button(comp,text="",height=2,width=5,command=lambda f=4: f4(f))
cbtn5=Button(comp,text="",height=2,width=5,command=lambda f=5: f4(f))
cbtn6=Button(comp,text="",height=2,width=5,command=lambda f=6: f4(f))
cbtn7=Button(comp,text="",height=2,width=5,command=lambda f=7: f4(f))
cbtn8=Button(comp,text="",height=2,width=5,command=lambda f=8: f4(f))
cbtn9=Button(comp,text="",height=2,width=5,command=lambda f=9: f4(f))


cbtn1.place(x=5,y=5)
cbtn2.place(x=50,y=5)
cbtn3.place(x=95,y=5)
cbtn4.place(x=5,y=45)
cbtn5.place(x=50,y=45)
cbtn6.place(x=95,y=45)
cbtn7.place(x=5,y=85)
cbtn8.place(x=50,y=85)
cbtn9.place(x=95,y=85)

comp.withdraw()
ask.mainloop()
