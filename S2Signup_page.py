import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

pencere_new23 = None
def close_top():
    global pencere_new23

    pencere_new23.destroy()
    pencere_new23 = None

def new_func():
    global pencere_new23
    global main_frame_new23
    global  login_label_new23
    global name_new23
    global entry_box_3_new23
    global surname_new23
    global entry_box_4_new23
    global email_label_new23
    global a_new23
    global entry_box_new23
    global image_new_1_new23
    global image_new_2_new23
    global nw_new23
    global nw2_new23
    global vb_new23
    global vb2_new23
    global Password_new23
    global entry_box_2_new23
    global Passwordconfirm_new23
    global entry_box_5_new23
    global cv_new23
    global cv_cursor_new23
    global ntv_new23
    global warning_label_new23
    global rp_button_new23
    global Signup_button_new23

    if pencere_new23 is None:
        pencere_new23 = tk.Toplevel()
        pencere_new23.configure(bg ="#458b74")
        pencere_new23.title("eomail")
        pencere_new23.iconbitmap("lockicon.ico")
        pencere_new23.geometry("700x800+450+50")
        pencere_new23.protocol("WM_DELETE_WINDOW", close_top)
    else:
        messagebox.showinfo("Existing open window","There is already an open sign up page ")
        return

    main_frame_new23 = tk.Frame(pencere_new23, bg ="#d3d3d3", width = 520, height = 565)
    main_frame_new23.pack(pady = 100)

    login_label_new23 = tk.Label(main_frame_new23, text ="CREATE ACCOUNT", font ="Italic 15 bold", bg ="#d3d3d3")
    login_label_new23.place(x = 170, y = 40)

    #welcome = tk.Label(main_frame,text = "Welcome to eomail system",font = "Italic 15",bg = "#d3d3d3",fg = "#666666")
    #welcome.place(x = 145,y = 20)

    #name and surname
    name_new23 = tk.Label(main_frame_new23, text ="Name:", font ="Italic 8 bold", bg ="#d3d3d3", fg ="#666666")
    name_new23.place(x = 50, y = 80)

    entry_box_3_new23 = tk.Entry(main_frame_new23, bd = 6, width = 35, relief ="flat", font ="Italic 10 bold", fg ="#333333")
    entry_box_3_new23.place(x = 50, y = 105)

    surname_new23 = tk.Label(main_frame_new23, text ="Surname:", font ="Italic 8 bold", bg ="#d3d3d3", fg ="#666666")
    surname_new23.place(x = 48, y = 140)

    entry_box_4_new23 = tk.Entry(main_frame_new23, bd = 6, width = 35, relief ="flat", font ="Italic 10 bold", fg ="#333333")
    entry_box_4_new23.place(x = 50, y = 165)

    #email ve entry kutusu
    email_label_new23 = tk.Label(main_frame_new23, text ="E-mail:", font ="Italic 8 bold", bg ="#d3d3d3", fg ="#666666")
    email_label_new23.place(x = 50, y = 195)

    a_new23 = tk.Scrollbar(main_frame_new23, orient ="horizontal")
    entry_box_new23 = tk.Entry(main_frame_new23, bd = 6, width = 35, relief ="flat", xscrollcommand = a_new23.set, font ="Italic 10 bold", fg ="#333333")
    entry_box_new23.focus()
    a_new23.config(command=entry_box_new23.xview)
    entry_box_new23.place(x = 50, y = 220)
    a_new23.place(x = 50, y = 250, width = 259)


    #password gizlilik ayarı
    image_new_1_new23 = ImageTk.PhotoImage(Image.open("visible.png"))
    image_new_2_new23 = ImageTk.PhotoImage(Image.open("invisible.png"))

    nv_new23 = tk.IntVar()
    nv_new23.set(1)
    def new_command():
        global entry_box_2_new23
        nonlocal nv_new23
        global vb_new23
        global image_new_1_new23
        global image_new_2_new23
        if nv_new23.get() == 1:
            vb_new23.place_forget()
            vb_new23 = tk.Button(main_frame_new23, command=new_command, image=image_new_1_new23, bg ="#d3d3d3", relief ="flat")
            vb_new23.place(x=315, y=305)
            nv_new23.set(0)
            entry_box_2_new23["show"] = ""
        elif nv_new23.get() == 0:
            vb_new23.place_forget()
            vb_new23 = tk.Button(main_frame_new23, command=new_command, image=image_new_2_new23, bg ="#d3d3d3", relief ="flat")
            vb_new23.place(x=315, y=305)
            nv_new23.set(1)
            entry_box_2_new23["show"] = "*"
    vb_new23 = tk.Button(main_frame_new23, command = new_command, image = image_new_2_new23, bg ="#d3d3d3", relief ="flat")
    vb_new23.place(x = 315, y = 305)


    nv2_new23 = tk.IntVar()
    nv2_new23.set(1)
    def new_command2():
        global entry_box_5_new23
        nonlocal nv2_new23
        global vb2_new23
        global image_new_1_new23
        global image_new_2_new23
        if nv2_new23.get() == 1:
            vb2_new23.place_forget()
            vb2_new23 = tk.Button(main_frame_new23, command=new_command2, image=image_new_1_new23, bg ="#d3d3d3", relief ="flat")
            vb2_new23.place(x=315, y=370)
            nv2_new23.set(0)
            entry_box_5_new23["show"] = ""
        elif nv2_new23.get() == 0:
            vb2_new23.place_forget()
            vb2_new23 = tk.Button(main_frame_new23, command=new_command2, image=image_new_2_new23, bg ="#d3d3d3", relief ="flat")
            vb2_new23.place(x=315, y=370)
            nv2_new23.set(1)
            entry_box_5_new23["show"] = "*"
    vb2_new23 = tk.Button(main_frame_new23, command = new_command2, image = image_new_2_new23, bg ="#d3d3d3", relief ="flat")
    vb2_new23.place(x = 315, y = 370)



    #password ve entry kutusu
    Password_new23 = tk.Label(main_frame_new23, text ="Password:", font ="Italic 8 bold", bg ="#d3d3d3", fg ="#666666")
    Password_new23.place(x = 50, y = 280)

    entry_box_2_new23 = tk.Entry(main_frame_new23, bd = 6, width = 35, relief ="flat", font ="Italic 10 bold", fg ="#333333", show ="*")
    entry_box_2_new23.place(x = 50, y = 305)

    #password confirm
    Passwordconfirm_new23 = tk.Label(main_frame_new23, text ="Password confirm:", font ="Italic 8 bold", bg ="#d3d3d3", fg ="#666666")
    Passwordconfirm_new23.place(x = 50, y = 345)

    entry_box_5_new23 = tk.Entry(main_frame_new23, bd = 6, width = 35, relief ="flat", font ="Italic 10 bold", fg ="#333333", show ="*")
    entry_box_5_new23.place(x = 50, y = 370)

    import sqlite3
    cv_new23 = sqlite3.connect("new_database2x.db")
    cv_cursor_new23 = cv_new23.cursor()
    cv_cursor_new23.execute("CREATE TABLE IF NOT EXISTS mail_table (Name TEXT,Surname TEXT,Mail TEXT,Password TEXT)")
    cv_new23.commit()


    ntv_new23 = tk.StringVar()
    ntv_new23.set("")
    warning_label_new23 = tk.Label(main_frame_new23, textvariable = ntv_new23, bg ="#d3d3d3", fg ="#ff0f0f")
    warning_label_new23.place(x = 50, y = 405)
    def signup_if():
        a_x = cv_cursor_new23.execute("SELECT Mail FROM mail_table")
        cakma_liste_x = a_x.fetchall()
        new_set_x = set()
        for tuples in cakma_liste_x:
            new_set_x.add(tuples[0])
        global entry_box_new23
        global entry_box_2_new23
        global entry_box_3_new23
        global entry_box_4_new23
        global entry_box_5_new23
        global warning_label_new23
        global ntv_new23
        eb_x = entry_box_new23.get()
        eb2_x = entry_box_2_new23.get()
        eb5_x = entry_box_5_new23.get()
        eb3_x = entry_box_3_new23.get()
        eb4_x = entry_box_4_new23.get()
        if len(eb_x) == 0 or len(eb2_x) == 0 or len(eb3_x) == 0 or len(eb4_x) == 0 or len(eb5_x) == 0 :
            ntv_new23.set("Empty box or boxes")
            return
        if eb2_x != eb5_x :
            ntv_new23.set("Passwords are not same")
            return
        if set(eb3_x).intersection(set("!,'^+%&/()=?_*+-1234567890£#$½{[]}-><|.\',\\,\n,\t,\",@€`;:,")) != set() or set(eb4_x).intersection(set("!,'^+%&/()=?_*+-1234567890£#$½{[]}-><|.\',\\,\n,\t,\",")) != set():
            ntv_new23.set("Name and Surname cannot consist numbers or signs ")
            return

        if eb_x[-11:] != "@eomail.com":
            ntv_new23.set("End of mail requires @eomail.com")
            return

        if eb_x in new_set_x:
            ntv_new23.set("eomail is used by other person please create a new one")
            return
        if len(eb2_x) < 8 or len(eb2_x) > 20:
            ntv_new23.set("Password length should be between 8 and 20")
            return
        if " " in eb2_x:
            ntv_new23.set("Password can't consist space")
            return
        cv_cursor_new23.execute(f"INSERT INTO mail_table VALUES('{eb3_x.capitalize()}','{eb4_x.capitalize()}','{eb_x}','{eb2_x}')")
        cv_new23.commit()
        warning_label_new23["fg"] = "#32CD32"
        ntv_new23.set("Information is saved")
        entry_box_new23.delete(0, len(eb_x))
        entry_box_2_new23.delete(0, len(eb2_x))
        entry_box_3_new23.delete(0, len(eb3_x))
        entry_box_4_new23.delete(0, len(eb4_x))
        entry_box_5_new23.delete(0, len(eb5_x))
        pencere_new23.destroy()
        messagebox.showinfo("Registration is successful", "Information is saved")

    def password_creator():
        global entry_box_2_new23
        global entry_box_5_new23
        characters = "AaBbCcDdEeFfGgHhIiJjKkLl1234567890lMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"
        characters_list = list(characters)
        from random import shuffle,sample,randint
        shuffle(characters_list)
        character_count = randint(8,20)
        password_list = sample(characters_list,character_count)
        password_string = "".join(password_list)

        enbn2 = entry_box_2_new23.get()
        enbn5 = entry_box_5_new23.get()
        new_set = set()
        a_y = cv_cursor_new23.execute("SELECT Password FROM mail_table")
        for member in a_y.fetchall():
            new_set.add(member[0])
        if password_string not in new_set:
            if len(enbn2) != 0:
                entry_box_2_new23.delete(0, len(enbn2))
            if len(enbn5) != 0:
                entry_box_5_new23.delete(0, len(enbn5))
            entry_box_2_new23.insert(0, f"{password_string}")
            entry_box_5_new23.insert(0, f"{password_string}")
        else:
            password_creator()



    #Signup button
    Signup_button_new23 = tk.Button(main_frame_new23, command = signup_if, relief ="flat", font ="Italic 10 bold", fg ="#333333", bg ="#458b74", text ="Create Account", activebackground ="#666666")


    #Recommend me password
    rp_button_new23 = tk.Button(main_frame_new23, relief ="flat", command = password_creator, font ="Italic 10 bold", fg ="#333333", bg ="#458b74", text ="Recommend me password", activebackground ="#666666", justify ="center")
    Signup_button_new23.place(x = 280, y = 460, width = 190, height = 48)
    rp_button_new23.place(x = 80, y = 460, width = 190, height = 48)



    pencere_new23.mainloop()