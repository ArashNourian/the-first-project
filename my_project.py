#  ==========================================   Creat a Data Base   ==================================================>

import sqlite3
my_ware=sqlite3.connect('my_ware.db')
my_ware.execute("""
CREATE TABLE IF NOT EXISTS commodity(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    value INTEGER,
    buy REAL,
    sell REAL
)
""")

#  =============================================   Creat Items   =====================================================>

import customtkinter as ctk
from CTkListbox import CTkListbox
from PIL import Image, ImageTk, ImageSequence
win = ctk.CTk()
win.title("WAREHOUSE")
win.minsize(500,800)
win.maxsize(800,1100)

l0 = ctk.CTkLabel(win, text = 'My Ware', font = ('Helvetica',22), width = 30, anchor = "s")
l0.grid(row = 1, column = 0)

l1 = ctk.CTkLabel(win, text = "Name of commodity : ", font = ('Arial',16), width = 200, anchor = "w")
l1.grid(row=3, column=0, sticky="ew", padx=10)

t1 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t1.grid(row=3, column=0, sticky="ns", padx=1)

l2 = ctk.CTkLabel(win, text = "Type of commodity : ", font = ('Arial',16), width = 200, anchor = "w")
l2.grid(row=4, column=0, sticky="ew", padx=10)

t2 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t2.grid(row=4, column=0, sticky="ns", padx=1)

l3 = ctk.CTkLabel(win, text = "Entered amount : ", font = ('Arial',16), width = 200, anchor = "w")
l3.grid(row=5, column=0, sticky="ew", padx=10)

t3 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t3.grid(row=5, column=0, sticky="ns", padx=1)

l4 = ctk.CTkLabel(win, text = "Buy's price : ", font = ('Arial',16), width = 200, anchor = "w")
l4.grid(row=6, column=0, sticky="ew", padx=10)

t4 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t4.grid(row=6, column=0, sticky="ns", padx=1)

l5 = ctk.CTkLabel(win, text = "Sell's price : ", font = ('Arial',16), width = 200, anchor = "w")
l5.grid(row=7, column=0, sticky="ew", padx=10)

t5 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t5.grid(row=7, column=0, sticky="ns", padx=1)

# l7 = ctk.CTkLabel(win, text = "Sell's price : ", font = ('Arial',16), width = 200, anchor = "w")
# l7.grid(row=8, column=0, sticky="ew", padx=10)

# t7 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
# t7.grid(row=8, column=0, sticky="ns", padx=1)

b1 = ctk.CTkButton(win,text="Add into the storage", width = 20,font = ('Arial',16), command = lambda: add_data())
b1.grid(row = 9, column = 0, sticky = "ns", padx = 1)

update_id_label = ctk.CTkLabel(win, text = "ID to update : ", font = ('Arial',16), width = 200, anchor = "w" )
update_id_label.grid(row = 11, column = 0, sticky = "ew", padx = 10)

update_id_text = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
update_id_text.grid(row=11, column=0, sticky="ns", padx=1)

update_id_button = ctk.CTkButton(win,text="Leaving from the warehouse", width = 20,font = ('Arial',16), command = lambda: update_data())
update_id_button.grid(row = 14, column = 0, sticky = "ns", padx = 1)

l7 = ctk.CTkLabel(win, text = "Exported amount : ", font = ('Arial',16), width = 200, anchor = "w")
l7.grid(row=13, column=0, sticky="ew", padx=10)

t7 = ctk.CTkTextbox(win, height = 1, width = 200 , fg_color = 'light blue', text_color = 'black')
t7.grid(row=13, column=0, sticky="ns", padx=1)

my_str = ctk.StringVar()
l6 = ctk.CTkLabel(win, textvariable = my_str,font = ('Arial',16), width = 10)
l6.grid(row=15, column=0, sticky="w", padx=10)
my_str.set("Output : ")

#  ================================================  Add Functions  ==========================================================>

def add_data():
    flag_validation = True
    name_of_commodity = t1.get("1.0", "end")
    Type_of_commodity = t2.get("1.0", "end")
    value_of_commodity = t3.get("1.0", "end")
    buys_price = t4.get("1.0", "end")
    sells_price = t5.get("1.0", "end")
    if (len(name_of_commodity) < 2 or len(Type_of_commodity) < 2 or len(value_of_commodity) < 2 or len(buys_price) == 0 or len(sells_price) == 0):
        flag_validation = False

    try:
        val1 = float(value_of_commodity)
        val2 = float(buys_price)
        val3 = float(sells_price)

    except:
        flag_validation = False

    if (flag_validation):
        my_str.set("Adding data... ")
        try:
            my_data = (None, name_of_commodity.strip(), Type_of_commodity.strip(), float(val1),float(val2),float(val3))
            my_query = "INSERT INTO commodity values (?,?,?,?,?,?)"
            my_ware.execute(my_query, my_data)
            my_ware.commit()
            x = my_ware.execute(''' select last_insert_rowid()''')
            id = x.fetchone()
            l6.grid()
            l6.configure(fg_color = 'green')
            l6.configure(text_color = 'white')
            my_str.set("ID :"+ str(id[0]))
            l6.after(3000, lambda: l6.grid_remove())
            t1.delete('1.0', "end")
            t2.delete('1.0', "end")
            t3.delete('1.0', "end")
            t4.delete('1.0', "end")
            t5.delete('1.0', "end")

        except sqlite3.Error as my_error:
            l6.grid()
            l6.configure(fg_color ='red')
            l6.configure(text_color = 'white')
            print(my_error)
            my_str.set(my_error)

    else:
        l6.grid()
        l6.configure(fg_color = 'black')
        l6.configure(text_color = 'gold')
        my_str.set("Please check inputs :")
        l6.after(3000, lambda: l6.grid_remove())

#  ================================================  Leave Functions  ==========================================================>

def fill_fields(event):
    selected_item = search_results_listbox.get(search_results_listbox.curselection())
    selected_id = selected_item.split(",")[0].split(":")[1].strip()
    record = my_ware.execute("SELECT * FROM commodity WHERE id=?", (selected_id)).fetchone()
    update_id_text.delete("1.0", "end")
    update_id_text.insert("end", record[0])
    t1.delete("1.0", "end")
    t1.insert("end", record[1])
    t3.delete("1.0", "end")
    t3.insert("end", record[3])

def update_data():
    update_id = update_id_text.get("1.0", "end").strip()
    name_of_commodity = t1.get("1.0", "end").strip()
    value_of_commodity = t7.get("1.0", "end")
    if update_id and name_of_commodity and value_of_commodity:
        try:
            my_query = "UPDATE commodity SET name = ? , value = ? WHERE id=?"
            my_ware.execute(my_query, (name_of_commodity, value_of_commodity, update_id))
            my_ware.commit()
            my_str.set(f"ID : {update_id} updated")
            l6.grid()
            l6.configure(fg_color = 'green')
            l6.configure(text_color = 'white')
            l6.after(3000, lambda: l6.grid_remove())

        except sqlite3.Error as my_error:
            l6.grid()
            l6.configure(fg_color ='red')
            l6.configure(text_color = 'white')
            print(my_error)
            my_str.set(my_error)

    else:
        l6.grid()
        l6.configure(fg_color = 'black')
        l6.configure(text_color = 'gold')
        my_str.set("Please check inputs :")
        l6.after(3000, lambda: l6.grid_remove())  

#  ================================================  Search   =========================================================>

search_name_label = ctk.CTkLabel(win, text = "Search by name :", width = 10, anchor = 'w', font = ('Arial',16))
search_name_label.grid(row=16, column=0, sticky="ew", padx=10)

search_name_text = ctk.CTkTextbox(win, height = 1, width = 200, fg_color = 'light blue', text_color = 'black')
search_name_text.grid(row=16, column=0, sticky="ns", padx=1)

search_type_label = ctk.CTkLabel(win, text = "Search by type :", width = 10, anchor = 'w',font = ('Arial',16))
search_type_label.grid(row = 17, column = 0, sticky = 'ew', padx = 10)

search_type_text = ctk.CTkTextbox(win, height = 1, width = 200, fg_color = 'light blue', text_color = 'black')
search_type_text.grid(row = 17, column = 0, sticky = 'ns', padx = 1)

search_button = ctk.CTkButton(win, text = "Search", width = 10,font = ('Arial',16), command = lambda: search_data())
search_button.grid(row = 18, column = 0, sticky = 'ns', padx = 1)

search_results_listbox = CTkListbox(win, height = 150, width = 550, fg_color = 'light blue', text_color = 'black',font = ('Arial',16))
search_results_listbox.grid(row = 19, column = 0, sticky = 'ns', padx = 1)

#  ============================================  Function of Search  =====================================================>

def search_data():
    search_name = search_name_text.get("1.0", "end").strip()
    search_type = search_type_text.get("1.0", "end").strip()
    query = "SELECT * FROM commodity WHERE name LIKE ? AND type LIKE ?"
    search_results = my_ware.execute(query, (f'%{search_name}%', f'{search_type}%')).fetchall()
    search_results_listbox.delete(0, "end")
    for row in search_results:
        search_results_listbox.insert("end", f"ID : {row[0]}, Name : {row[1]}, Type : {row[2]}")
    search_results_listbox.bind('<Double-1>', fill_fields)


#  ================================================  Add Image   =========================================================>

ctk.set_appearance_mode("dark")
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = ctk.CTk()
app.geometry("200x200")
gif = Image.open(resource_path("storage-ezgif.com-crop.gif"))
frames = []

for frame in ImageSequence.Iterator(gif):
    frames.append(ImageTk.PhotoImage(frame.copy()))

label = ctk.CTkLabel(win, text="")
label.grid(row=0, column=0)

def animate(index):
    label.configure(image=frames[index])
    index += 1

    if index == len(frames):
        index = 0

    app.after(80, animate, index)

animate(0)
win.mainloop()
my_ware.close()