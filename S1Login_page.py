import tkinter as tk
from PIL import ImageTk,Image
import S2Signup_page

pencere = tk.Tk()
pencere.configure(bg = "#458b74")
pencere.title("eomail")
pencere.iconbitmap("lockicon2.ico")
pencere.geometry("700x750+450+10")

main_frame = tk.Frame(pencere,bg = "#d3d3d3",width = 520,height = 565)
main_frame.pack(pady = 100)


#login_label = tk.Label(main_frame,text = "LOGIN",font = "Italic 15 bold",bg = "#d3d3d3")
#login_label.place(x = 10 , y = 50)



#image olustur
ni = ImageTk.PhotoImage(Image.open("365774-middle2.png"))
new_l = tk.Label(main_frame,image = ni,bg = "#d3d3d3")
new_l.place(x = 172 , y = 5)

#email ve entry kutusu
email_label = tk.Label(main_frame,text = "E-mail:",font = "Italic 8 bold",bg = "#d3d3d3",fg = "#666666")
email_label.place(x = 130,y = 185)

a = tk.Scrollbar(main_frame,orient = "horizontal")
entry_box = tk.Entry(main_frame, bd = 6, width = 35, relief ="flat", xscrollcommand = a.set, font ="Italic 10 bold", fg ="#333333")
entry_box.focus()
a.config(command=entry_box.xview)
entry_box.place(x = 130, y = 210)
a.place(x = 130,y = 240,width = 259)



#password ve entry kutusu
Password = tk.Label(main_frame,text = "Password:",font = "Italic 8 bold",bg = "#d3d3d3",fg = "#666666")
Password.place(x = 130,y = 270)

entry_box_2 = tk.Entry(main_frame, bd = 6, width = 30, relief ="flat", font ="Italic 10 bold", fg ="#333333", show="*")
entry_box_2.place(x = 130, y = 295)

#visibility button for password and its function
image_new_1 = ImageTk.PhotoImage(Image.open("visible.png"))
image_new_2 = ImageTk.PhotoImage(Image.open("invisible.png"))

nv = tk.IntVar()
nv.set(1)
def new_command():
    global entry_box_2
    global nv
    global vb
    global image_new_1
    global image_new_2
    if nv.get() == 1:
        vb.place_forget()
        vb = tk.Button(main_frame, command=new_command, image=image_new_1,bg = "#d3d3d3",relief = "flat")
        vb.place(x=355, y=295)
        nv.set(0)
        entry_box_2["show"] = ""
    elif nv.get() == 0:
        vb.place_forget()
        vb = tk.Button(main_frame, command=new_command, image=image_new_2,bg = "#d3d3d3",relief = "flat")
        vb.place(x=355, y=295)
        nv.set(1)
        entry_box_2["show"] = "*"


vb = tk.Button(main_frame, command = new_command, image = image_new_2, bg ="#d3d3d3", relief ="flat")
vb.place(x = 355, y = 295)



import sqlite3
cv = sqlite3.connect("new_database2x.db")
cv_cursor = cv.cursor()
cv_cursor.execute("CREATE TABLE IF NOT EXISTS mail_table (Name TEXT,Surname TEXT,Mail TEXT,Password TEXT)")
cv.commit()

ntv = tk.StringVar()
ntv.set("")
warning_label = tk.Label(main_frame,textvariable = ntv,bg = "#d3d3d3", fg = "#ff0f0f")
warning_label.place(x = 130, y = 325)


def login_if():
    a = cv_cursor.execute("SELECT Mail,Password FROM mail_table")
    cakma_liste = a.fetchall()
    new_dict = dict()
    for tuples in cakma_liste:
        new_dict[tuples[0]] = tuples[1]
    global entry_box
    global entry_box_2
    eb = entry_box.get()
    eb2 = entry_box_2.get()
    if len(eb) == 0 or len(eb2) == 0:
        ntv.set("Empty box or boxes")
        return
    flag = False
    for member in new_dict:
        if eb == member:
            flag = True
            break
    if not flag:
        ntv.set("Invalid password or eomail")
        return

    if new_dict[eb] != eb2:
        ntv.set("Invalid password or eomail")
        return
    warning_label["fg"] = "#32CD32"
    ntv.set("Login is successful ")
    entry_box.delete(0,len(eb))
    entry_box_2.delete(0,len(eb2))
    b = cv_cursor.execute(f"SELECT Name,Surname FROM mail_table WHERE Mail == '{eb}' and Password == '{eb2}' ")
    ntuple = b.fetchall()[0]
    pencere.destroy()
    new_window = tk.Tk()
    new_window.title("eomail page")
    new_window.iconbitmap("lockicon3.ico")
    new_window.geometry("700x750+500+10")
    lab1 = tk.Label(new_window,text = f"Welcome {ntuple[0]} {ntuple[1]} to eomail system",anchor = "w")
    lab1.place(x = 0,y = 0)
    new_window.mainloop()


#Login button
Signin_button = tk.Button(main_frame,command = login_if,relief = "flat",font = "Italic 10 bold",fg = "#333333",bg = "#458b74",text = "SIGN IN",activebackground = "#666666")
Signin_button.place(x = 135, y = 385,width = 120,height = 48)

Signup_button = tk.Button(main_frame,command = S2Signup_page.new_func,relief = "flat",font = "Italic 10 bold",fg = "#333333",bg = "#458b74",text = "SIGN UP",activebackground = "#666666")
Signup_button.place(x = 275, y = 385,width = 120,height = 48)

pencere.mainloop()