from tkinter import *
from docx import *
import os 
window = Tk()
window.title("File Manager")
window.geometry("900x500")
window.config(bg="#3d444d")
xx = 50
number = 1
arr = []
lst = list(str(open("lst.txt" , "r").read()).split())

def fun_1():
    global xx 
    global number
    n = entry_name.get()
    if (len(n) != 0)and (n not in arr):
        name_file = n + '.docx'
        name_file_1 = 'files' + '\ '
        name_file_1 = name_file_1[0: -1]
        name_file_1 += name_file
        list_box.insert(-1, n)
        with open("lst.txt" , "a") as file:
            file.write(' ')
            file.write(n)
        docx = Document()
        docx.save(name_file_1)
        button=Button(width=100, bg="#4d5561",fg="#ffffff", text=n, anchor="w", command = lambda : os.startfile(name_file_1))
        button.place(x=20, y=xx)
        lable = Label(text=number, bg="#4d5561",fg="#ffffff").place(x=5, y=xx + 2)
        number += 1
        xx+=26
        arr.append(n)
        lst.append(n)
        list_box.config(listvariable = Variable(value=arr))

def fun_2(n):
    global xx 
    global number
    if (len(n) != 0) and (n not in arr):
        name_file = n + '.docx'
        name_file_1 = 'files' + '\ '
        name_file_1 = name_file_1[0: -1]
        name_file_1 += name_file
        docx = Document()
        docx.save(name_file_1)
        button=Button(width=100, bg="#4d5561",fg="#ffffff", text=n, anchor="w", command = lambda : os.startfile(name_file_1))
        button.place(x=20, y=xx)
        lable = Label(text=number, bg="#4d5561",fg="#ffffff").place(x=5, y=xx + 2)
        number += 1
        xx+=26
        arr.append(n)

def fun_2_1(n):
    global xx 
    global number
    name_file = n + '.docx'
    name_file_1 = 'files' + '\ '
    name_file_1 = name_file_1[0: -1]
    name_file_1 += name_file
    button=Button(width=100, bg="#4d5561",fg="#ffffff", text=n, anchor="w", command = lambda : os.startfile(name_file_1))
    button.place(x=20, y=xx)
    lable = Label(text=number, bg="#4d5561",fg="#ffffff").place(x=5, y=xx + 2)
    number += 1
    xx+=26

def fun_3(): 
    n = list_box.curselection()
    n = list(n)
    n = n[0]
    m = ''
    list_box.delete(n)
    k = lst[n]
    del lst[n]
    del arr[n]
    open_file_3 = open("lst.txt" , "w")
    for i in lst:
        m += i
        m += ' '
    open_file_3.write(m)
    name_file = k + '.docx'
    name_file_1 = 'files' + '\ '
    name_file_1 = name_file_1[0: -1]
    name_file_1 += name_file
    os.remove(name_file_1)
    restart_program()

def fun_4():
    global lst
    if (len(entry_name.get()) != 0) and (entry_name.get() not in arr):
        lst_1 = ''
        m = entry_name.get()
        n = list_box.curselection()
        n = list(n)
        n = n[0]
        k = list_box.get(n)
        lst.remove(k)
        lst.append(m)
        # print(lst)
        for i in lst:
            lst_1 += i
            lst_1 += ' '
        # print(lst_1)
                    
        with open("lst.txt" , "w") as file:
            file.write(lst_1)
        
        name_file_2 = m + '.docx'
        name_file_3 = 'files' + '\ '
        name_file_3 = name_file_3[0: -1]
        name_file_3 += name_file_2

        name_file = k + '.docx'
        name_file_1 = 'files' + '\ '
        name_file_1 = name_file_1[0: -1]
        name_file_1 += name_file
        os.rename(name_file_1, name_file_3)
        restart_program()

def restart_program():
    for i in window.winfo_children():
        if isinstance(i, Button) and i not in [add, delete, rename, entry_name]:
            i.destroy()
    list_box.delete(0, END) 
    global xx, number, arr
    xx = 50
    number = 1
    # with open("lst.txt", "r") as f:
    #     lst = f.read().split()
    # print(lst)
    for i in lst:
        fun_2_1(i)
    list_box.config(listvariable=Variable(value=lst))

for i in lst:
    fun_2(i)

lable = Label(text='Введите название:', bg="#3d444d",fg="#ffffff").place(x=120, y=11)

entry_name = Entry(bg="#3d444d",fg="#ffffff")
entry_name.place(x=230, y=12)

add = Button(text='Создать Файл', command=fun_1, bg="#4d5561", fg="#ffffff")
add.place(x= 10, y=10)

list_box = Listbox(listvariable = Variable(value=lst), bg="#4d5561", fg="#ffffff")
list_box.place(x=750, y=10)

delete = Button(text='Удалить файл', command=fun_3, bg="#4d5561", fg="#ffffff")
delete.place(x=642, y=10)

rename = Button(text='Переиминовать', command=fun_4, bg="#4d5561", fg="#ffffff")
rename.place(x=530, y=10)

window.mainloop()