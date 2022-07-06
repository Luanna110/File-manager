import os
from tkinter import *
from tkinter.filedialog import askdirectory

window = Tk()  # tworzenie okna głównego
window.title("File Manager")  # ustawienie tytułu okna głównego
window.geometry("400x500")


label3 = Label(window, text="File manager ", font=('Helvetica', 20,"bold"), foreground='midnight blue')
label3.pack(pady=15)

my_frame = Frame(window)
my_scrollbar = Scrollbar(my_frame,orient=VERTICAL)

list_box = Listbox(my_frame,width=50, font=('Helvetica', 10),yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=list_box.yview)
my_scrollbar.pack(side=RIGHT,fill=BOTH)
my_frame.pack(pady=10)
list_box.pack(pady=10)



def print_all():
    global lst

    clear_text()
    my_entry.config(state=NORMAL)
    director=str(open_file())
    dir_label(director)
    # path = "C:\\cpi\\cad\\"
    if os.path.exists(director):
        lst = os.listdir(director)

        for i in lst:
            list_box.insert(END, i + "\n")
        list_box.pack()  # podpinanie kontrolki pod okno
    else:
        return 'Podana lokacja nie istnieje'
    return lst


def clear_text():
   list_box.delete(0,END)
   my_entry.delete(0, END)
   try:
       label1.destroy()
   except NameError:
       pass
   my_entry.config(state='disabled')


def dir_label(directory):
    global label1
    label1 = Label(window, text="The File is located at : " + str(directory), font=('Helvetica', 10))
    label1.pack()

def open_file():
    directory = askdirectory()
    return directory

def update(data):
    list_box.delete(0,END)
    for item in data:
        list_box.insert(END, item)

def fillout(e):
    my_entry.delete(0,END)
    my_entry.insert(0,list_box.get(ANCHOR))

def check(e):
    #grab what is typed
    typed = my_entry.get()
    if typed == "":
        data = lst
    else:
        data = []
        for item in lst:
            if typed.lower() in item.lower():
                data.append(item)
    #update witch selected data
    update(data)

label2 = Label(window, text="Search condition : ", font=('Helvetica', 10, "bold"),foreground='midnight blue' )
label2.pack()
my_entry = Entry(window,width=30, font=('Helvetica',10))
my_entry.pack()
my_entry.config(state='disabled')

list_box.bind("<<ListboxSelect>>",fillout)
my_entry.bind("<KeyRelease>",check)

button_all = Button(window, text='Directory', font=('Helvetica', 10, "bold"),foreground='midnight blue', command=print_all)
button_all.pack(pady=10)
button_clear = Button(window, text='Clear', font=('Helvetica', 10, "bold"),foreground='midnight blue', command=clear_text)
button_clear.pack(pady=10)
button_close = Button(window, text="Close", font=('Helvetica', 10, "bold"),foreground='midnight blue', command=window.destroy)
button_close.pack(pady=10)




window.mainloop()