from tkinter import *
import math
import random
import tkinter

master = Tk()
master.title("Hangman: The Game")
master.iconbitmap("ico.ico")
canvas_width = 1024
canvas_height = 576
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()


img = PhotoImage(file="t.gif")
w.create_image(0,30, anchor=NW, image=img)
imgo = PhotoImage(file="go.gif")
imgw = PhotoImage(file="win.gif")


def rotate(points, angle, center):
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points


def wrong(nwa):
    if nwa == 1:                    # w.create_line(0, y, canvas_width, y, fill="#476042")
        global base
        base=w.create_rectangle(324, 440, 650, 460, fill="#000000")      # base

    elif nwa == 2:
        global pole
        pole=w.create_rectangle(370, 230, 390, 460, fill="#000000")          # pole

    elif nwa == 3:
        global t1,t2
        t1=w.create_rectangle(390, 230, 600, 250, fill="#000000")          # top1
        t2=w.create_rectangle(580, 250, 585, 270, fill="#000000")          # top2

    elif nwa == 4:
        global head
        head=w.create_oval(570, 270, 595, 295, outline="#000000", width=3)   # head

    elif nwa == 5:
        global spine
        spine=w.create_rectangle(582, 295, 584, 350, fill="#000000")          # spine

    elif nwa == 6:
        leg1 = rotate([[582, 350], [584, 350], [584, 400], [582, 400]], 30, [583, 350])     #leg1
        global l1,l2
        l1=w.create_polygon(leg1)                                                              #leg1
        leg2 = rotate([[582, 350], [584, 350], [584, 400], [582, 400]], -30, [583, 350])    #leg2
        l2=w.create_polygon(leg2)                                                              #leg2

    elif nwa == 7:
        global h1,h2
        h1 = rotate([[582, 315], [584, 315], [584, 355], [582, 355]], 30, [583, 315])     #hand1
        h1=w.create_polygon(h1)                                                              #hand1
        h2 = rotate([[582, 315], [584, 315], [584, 355], [582, 355]], -30, [583, 315])    #hand2
        h2=w.create_polygon(h2)                                                              #hand2
        game_over()


d={1:"HALFWAY",2:"ATTENTION",3:"DAZZLE",4:"TOGETHER",5:"PASSION",6:"SUCCESS",7:"CLARITY",8:"GAMING",9:"PYTHON",10:"SMART",11:"GAMING",12:"COMPUTERS",13:"SMARTPHONES",14:"ANIMALS",15:"COMMANDS",16:"PICTURES",17:"MOVIES",18:"DOCUMENTS",19:"DOWNLOADS",20:"VIDEOS",21:"TELEVISION",22:"CHOCOLATE",23:"MUSIC",24:"ALPHABETS",25:"NUMBERS",26:"LETTERS",27:"MAMMALS",28:"FOOD",29:"LEGENDS",30:"ANACONDA"}


def sel_rand_word():
    n=random.randint(1,len(d))
    sel_word=d[n]
    return sel_word



word=sel_rand_word()
wordd = Label(master, text="The word was: "+word)
cgd = Label(master, text='')
wgd = Label(master, text='')
e1 = Text(master, height=1, width=1)

nwa=0
ui="_"*len(word)
dui=""
ecg=''
ewg=''

for i in ui:
    dui+=i+" "
uiw=""
uid = Label(master, text=dui)


def game_over():

    global uid
    global go, wordd
    go=w.create_image(380,500, anchor=NW, image=imgo)
    uid.place_forget()     #underscore+text
    rbut.place(x=760, y=225)
    e1.place_forget()         #box
    eal.place_forget()        #text
    l_enter.place_forget()   #button
    wordd.place(x=370,y=470)   #word

def strip_and_get_last(s):
    
    if len(s) > 1:
        s = s.strip()
        s = s.replace(' ', '').replace('\n', '').replace('\r', '')
    return s[-1]

g = StringVar()

def get_inp():
    global g
    global nwa, uiw, uid, dui, ecg, ewg, cgd, wgd, e1
    dui=""
    
    
    g.set(e1.get("1.0", "end-1c"))
    input_char = strip_and_get_last(g.get().upper())
    global ui
    e1.delete(1.0, END)
    if input_char in word and input_char not in ecg:
        ecg+=input_char+" "
        for i in range(len(word)):
            if word[i] == input_char:
                nui=ui[:i]+input_char+ui[i+1:]
                ui=nui
        for i in ui:
            dui+=i+" "
        uid.place_forget()
        uid = Label(master, text=dui)
        uid.place(x=492, y=520)
        if set(ecg) == set(word+' '):
            win()
    elif input_char in ewg or input_char in ecg:
        pass
    else:
        ewg+=input_char+" "
        nwa+=1
        uiw+=input_char
        wrong(nwa)
    cgd.place_forget()
    wgd.place_forget()
    cgd = Label(master, text="Correct guesses made: "+ecg)
    wgd = Label(master, text="Wrong guesses made:\n"+ewg)
    cgd.place(x=60, y=200)
    wgd.place(x=60, y=230)

def play():

    pbut.place_forget()
    global g
    global ui
    global word, uid, e1, l_enter, eal, wordd, cgd, wgd, dui
    e1 = Text(master, height=1, width=1)
    e1.place(x=860, y=250)
    word=sel_rand_word()
    ui="_"*len(word)
    dui = '' 
    for i in ui:
        dui+=i+" "
    uid = Label(master, text=dui)
    eal = Label(master, text="Enter a letter: ")
    wordd = Label(master, text="The word was: "+word)
    uid.place(x=492, y=520)
    eal.place(x=830, y=230)
    
    l_enter = Button(master, text="Enter", fg="red", command=lambda: get_inp(), width=10 )
    l_enter.place(x=830, y=275)
    cgd = Label(master, text="Correct guesses made: "+ecg)
    wgd = Label(master, text="Wrong guesses made:\n"+ewg)
    cgd.place(x=60, y=200)
    wgd.place(x=60, y=230)

def clear_canv():

    if nwa>=1:
        w.delete(base)
    if nwa>=2:
        w.delete(pole)
    if nwa>=3:
        w.delete(t1)
        w.delete(t2)
    if nwa>=4:
        w.delete(head)
    if nwa>=5:
        w.delete(spine)
    if nwa>=6:
        w.delete(l1)
        w.delete(l2)
    if nwa==7:
        w.delete(h1)
        w.delete(h2)
    e1.place_forget()   #text
    eal.place_forget()   #box
    l_enter.place_forget()  #button
    cgd.place_forget()    #correct text
    wgd.place_forget()    #wrong  text


def restart(rb):

    rb.place_forget()
    global nwa,ui,ecg,uid,ewg,g,uiw,wordd,cgd,wgd,wn,go
    if set(ecg) == set(word+' '):
        w.delete(wn)
    else:
        w.delete(go)
    clear_canv()
    nwa=0
    g = StringVar()
    nwa=0
    ui="_"*len(word)
    dui=""
    ecg=''
    ewg=''
    for i in ui:
        dui+=i+" "
    uiw=""
    uid.place_forget()
    wordd.place_forget()
    uid = Label(master, text=dui)
    cgd.place_forget()
    wgd.place_forget()
    play()


def win():
    global uid
    global wn
    wn=w.create_image(370,470, anchor=NW, image=imgw)
    uid.place_forget()
    rbut.place(x=760, y=225)  #restart button
    e1.place_forget()
    eal.place_forget()
    l_enter.place_forget()


pbut = Button(master, text="PLAY", fg="red", command=lambda: play(), width=20)
rbut = Button(master, text="PLAY AGAIN", fg="red", command=lambda: restart(rbut), width=20)
pbut.place(x=492, y=520)


mainloop()
