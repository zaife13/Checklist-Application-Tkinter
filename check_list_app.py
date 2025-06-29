# Simple Check-List 📋 application made with tkinter 🪶
import tkinter
from tkinter import END
from tkinter.constants import ANCHOR

# 1- Define fonts and colors for application 🫟
application_font  = ('Times New Roman', 18)
primary_color     = '#6c1cbc'
button_color      = '#e2cff4'

# 2- Define root window and its configuration 🖥️
root = tkinter.Tk()
root.title('Check List')
root.geometry('450x450+400+100')
root.config(bg=primary_color)

# 3- Define functions here
def quit_app():
    root.destroy()

def add_task():
    """Add user task to the listbox"""
    list_box.insert(END, input_task_entry.get())

def remove_task():
    """Remove user task from end"""
    list_box.delete(ANCHOR)

def clear_list():
    """Clear the list completely"""
    list_box.delete(0, END)


def save_list():
    """Save the list to the file system"""
    with open('checklist.txt', 'w') as f:
        #listbox.get() returns a tuple
        list_box_tuple = list_box.get(0, END)
        for item in list_box_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(f"{item} {"\n"}")

def reopen_list_on_startup():
    try:
        with open('checklist.txt', 'r') as f:
            for line in f:
                list_box.insert(END, line)
    except:
        print("FILE NOT FOUND")
        return

# GUI layout goes here
# 4- Create Application Frames
input_frame = tkinter.Frame(root, bg=primary_color)
output_frame = tkinter.Frame(root, bg=primary_color)
buttons_frame = tkinter.Frame(root, bg="yellow")

# 5- 5.1: Create input_frame widgets here
input_task_entry = tkinter.Entry(input_frame,
                                 font=application_font,
                                 bg="white",
                                 fg="black",
                                 insertbackground="black",
                                 width=34)

input_task_entry.insert(0,"Enter your task")

add_task_button = tkinter.Button(input_frame,
                                 bg=button_color,
                                 text="Add Task",
                                 font=application_font,
                                 highlightbackground=primary_color,
                                 command=add_task)

# 5.2: Create output_frame widgets here
scroll_bar = tkinter.Scrollbar(output_frame)
list_box = tkinter.Listbox(output_frame,
                           bg="white",
                           fg="black",
                           font=application_font,
                           borderwidth=3,
                           height=15,
                           width=45,
                           yscrollcommand=scroll_bar.set)

scroll_bar.config(command=list_box.yview)

# 5.3: Create buttons_frame widgets (all lower buttons of application)
remove_button = tkinter.Button(buttons_frame,
                                    text="Remove Item",
                                    font=application_font,
                                    highlightbackground=primary_color,
                                    command=remove_task)

clear_button = tkinter.Button(buttons_frame,
                                   text="Clear List",
                                   font=application_font,
                                   highlightbackground=primary_color,
                                   command=clear_list)

save_button = tkinter.Button(buttons_frame,
                            text="Save List",
                            font=application_font,
                            highlightbackground=primary_color,
                            command=save_list)

quit_button = tkinter.Button(buttons_frame,
                             text="Quit",
                             font=application_font,
                             highlightbackground=primary_color,
                             command=quit_app)

# 6- ⚙️ pack the frames into the layout manager
input_frame.pack()
output_frame.pack()
buttons_frame.pack(pady=(10,0))

# 7- pack the widgets into the frames
# 7.1: pack input_frame widgets using grid manager
input_task_entry.grid(row=0, column=0, pady=10)
add_task_button.grid(row=0, column=1)

# 7.2: pack output_frame widgets using grid manager
list_box.grid(row=0, column=0)
scroll_bar.grid(row=0, column=1, sticky="NS")

# 7.3: pack buttons_frame widgets using grid manager
remove_button.grid(row=0, column=0)
clear_button.grid(row=0, column=1)
save_button.grid(row=0, column=2)
quit_button.grid(row=0, column=3)

# on startup, this function will run and will retrieve checklist tasks
# from file-manager
reopen_list_on_startup()

# 🔄 run the main-loop of root window
root.mainloop()