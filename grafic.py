from customtkinter import *
import function

root = CTk()

root.title('TAKING _Data Managment System')
root.geometry('800x400')
root.resizable(width= False, height= False)

project_title = CTkEntry(root, placeholder_text= 'Project', width= 70)
project_title.place(x= 10, y= 10)
project_date = CTkEntry(root, placeholder_text= 'yyyy/mm/dd', width= 70)
project_date.place(x= 90, y= 10)
project_from = CTkEntry(root, placeholder_text= 'From', width= 70)
project_from.place(x= 170, y= 10)

consol = CTkTextbox(root, width= 520, height= 330, border_color= 'white', border_width= 1, font= ('Arial', 20))
consol.place(x= 10, y= 50)

shape_name = CTkEntry(root, placeholder_text= 'Name', width= 75)
shape_name.place(x= 700, y= 10)
shape_enter = CTkEntry(root, placeholder_text= 'HH:MM:SS', width= 75)
shape_enter.place(x= 620, y= 10)
shape_date = CTkEntry(root, placeholder_text= 'mm/dd', width= 75)
shape_date.place(x= 540, y= 10)
add_btn = CTkButton(root, text= 'Add', text_color= 'white', width= 235, fg_color= 'green', command= function.add_new)
add_btn.place(x= 540, y= 45)

remove_row = CTkEntry(root, placeholder_text= ': row', width= 80)
remove_row.place(x= 540, y= 300)
remove_btn = CTkButton(root, text= 'Remove', text_color= 'white', fg_color= 'red', width=150, command= function.remove)
remove_btn.place(x= 625, y= 300)

export_btn = CTkButton(root, text= 'Export now!', width= 100, height=30, fg_color= 'yellow', text_color= 'black', command= function.export)
export_btn.place(x= 610, y= 350)

root.mainloop()