import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile , asksaveasfile
from functions import *

bg='#444444'

win = tk.Tk()
win.iconphoto(False, tk.PhotoImage(file = "./settings.png"))
win.title('Tool')
win.geometry('%dx%d+%d+%d' %(700,450,400,200))
win.resizable(False, False)
win.configure(bg = bg)

selection = [0,0,0,0]

def run():
    file1 = open('./facttest.cpp', 'r')
    file2 = open('./newfacttest.txt','+w')

    Lines = file1.readlines()
        
    if selection[-1] == 1:
        Lines = remove_blockcommand(Lines)
        Lines = remove_singlecommand(Lines)
        Lines = remove_whitespace(Lines)
        Lines = remove_externallibraries(Lines)

    if selection[0] == 1:
        Lines = remove_whitespace(Lines)

    if selection[1] == 1:
        Lines = remove_singlecommand(Lines)
        Lines = remove_blockcommand(Lines)

    if selection[2] == 1:
        Lines = remove_externallibraries(Lines)


    for line in Lines :
        file2.write(line)

    file1.close()
    file2.close()

    page2('./newfacttest.txt')

def show():
    if var1.get()==1:
        selection[0]=1
    if var2.get()==1:
        selection[1]=1
    if var3.get()==1:
        selection[2]=1
    if var4.get()==1:
        for i in range(0,2):
            selection[i]=0
        selection[3]=1


def home() :
    lbl = tk.Label(win,width=29,text='put c++ file',fg= "#e06c75",bg="#fffff4",font= 'Inter 13').place(relx=0.5, rely=0.3, anchor='s')
    lbl2 = tk.Label(win,text='File name :',bg="#fffff4",font= 'Inter 13').place(relx=0.3, rely=0.3, anchor='s')
    B = tk.Button(win, text ="browse",command = upload_file, borderwidth=1,font= 'Inter 11').place(relx=0.7, rely=0.4, anchor='s')

    global var1
    global var2
    global var3
    global var4
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()

    c=0.5
    for txt ,var in [('Remove white space',var1),('Remove commands',var2),('Remove all Call external libraries',var3),('ALL of this',var4)]:
        Check_B=tk.Checkbutton(win, 
                   text=txt,
                   padx = 20, 
                   variable=var,
                   onvalue=1,
                   offvalue=0,
                   command=show
                   )
        Check_B.place(anchor='w',relx=0.2,rely=c)
        Check_B.configure(bg=bg)
        c+=0.1
        

    B2 = tk.Button(win, text ="ok",command = lambda:run(), width=4,
          height=0, borderwidth=1,font= 'Inter 15').place(relx=0.45,rely=0.8)

def upload_file() :
    global file
    file =filedialog.askopenfilename()
    lbl = tk.Label(win,width=25,text=file.split('/')[-1],bg= "#fffff4",font= 'Inter 13').place(relx=0.53, rely=0.3, anchor='s')
    
    if file is not None:
        pass
    file = open(file, 'r')
    file1 = open('./facttest.cpp', "w")
    file1.write(file.read())
    file.close()
    file1.close()

def save_file():
    name = asksaveasfile(mode='w',initialfile = 'Untitled.txt',
      defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    name.write(data)
    name.close


def page2(filename):
    
    tf = open(filename, 'r')
    global data
    data = tf.read()
    tf.close()
    win2 = tk.Tk()
    win2.title('Tool')
    win2.geometry('%dx%d+%d+%d' %(450,450,500,200))
    win2.resizable(False, False)

    txtarea = tk.Text(win2, width=200, height=25)
    txtarea.insert(tk.END, data)
    txtarea.pack()

    btn= tk.Button(win2, text= "Save", command= lambda:save_file())
    btn.pack(pady=10)

home()

win.mainloop()