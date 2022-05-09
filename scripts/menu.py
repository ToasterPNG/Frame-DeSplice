import librarys

from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter, os, cv2, shutil, base64
from PIL import Image, ImageTk

"""
opencv-python==4.5.1.48
Pillow==8.2.0
"""

w = tkinter.Tk()

w.geometry('300x250')
w.resizable(0, 0)
w.wm_iconbitmap('../assets/logo.ico')
w.title('Frame DeSplice')
w.resizable(False, False)

pushd = os.getcwd()
filename = 'DeSpliced.mp4'
input_dir = 'C:/tmp'
output_dir = 'C:/output'
image_type = 'png'
errors = ''
fps = 2

cur_frame = 'none'

deafult_template = 0

list_of_templates = ['']

canvas = Canvas(
    w,
    width = 160, 
    height = 140
)

def find_templates():
    global list_of_templates, deafult_template

    os.chdir('..')
    os.chdir('templates')

    for x in os.listdir():
        if x.endswith(".fds"):

            deafult_template += 1

            list_of_templates.append(x.replace('.fds', ''))

    os.chdir('..')
    os.chdir('scripts')

find_templates()

def set_template(*args):
    global variable

    file = variable.get() + '.fds'

    os.chdir('..')
    os.chdir('templates')

    with open(file, 'rb') as temp:
        template = temp.read()

    template = base64.b64decode(template)

    os.chdir('..')
    os.chdir('scripts')

    exec(template)

def save_templates():

    try:

        folder = filedialog.askdirectory()
        
        Input_Text_Box.delete(1.0, 'end')
        Input_Text_Box.insert('end', folder)

        output_dir = Output_Text_Box.get(1.0, "end-1c")
        input_dir = Input_Text_Box.get(1.0, "end-1c")

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def browseFiles(arg):
    global Input_Text_Box, Output_Text_Box, output_dir, input_dir, errors, Console_Text_Box

    try:

        if arg == 0:
            folder = filedialog.askdirectory()
            
            Input_Text_Box.delete(1.0, 'end')
            Input_Text_Box.insert('end', folder)
        else:
            folder = filedialog.askdirectory()
            
            Output_Text_Box.delete(1.0, 'end')
            Output_Text_Box.insert('end', folder)

        output_dir = Output_Text_Box.get(1.0, "end-1c")
        input_dir = Input_Text_Box.get(1.0, "end-1c")

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def update_progressbar(val):
    global progress, errors

    try:

        progress['value'] += val
        w.update_idletasks()

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def set_progressbar(val):
    global progress, errors

    try:

        progress['value'] = val
        w.update_idletasks()

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def delete_file(fn='DeSpliced.mp4'):
    global errors, pushd

    try:

        input_dir_full = os.path.join(input_dir.replace('/', '\\'), fn)

        delete_command = 'del /f "' + input_dir_full + '"'
        # del /f "C:\tmp\DeSpliced.mp4"
        os.system(delete_command); update_progressbar(10)
        os.chdir(pushd)

        set_progressbar(0)
    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def render_video(fps, file_name='DeSpliced.mp4', image_type='png'): # i add presets maybe some time :'(
    global progress, errors, pushd

    try:
        set_progressbar(0)

        output_dir = Output_Text_Box.get(1.0, "end-1c")
        input_dir = Input_Text_Box.get(1.0, "end-1c")

        os.chdir(input_dir)

        images = [img for img in os.listdir(input_dir) if img.endswith("." + image_type)]; update_progressbar(10)
        frame = cv2.imread(os.path.join(input_dir, images[0])); update_progressbar(20)

        height, width, layers = frame.shape

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v'); update_progressbar(20)

        video = cv2.VideoWriter(file_name, fourcc, fps, (width,height)); update_progressbar(10)

        
        for image in images:
            print(image)
            video.write(cv2.imread(os.path.join(input_dir, image)))

        # update_frame(os.path.join(input_dir, image))

        video.release()

        update_progressbar(30)
        

        input_dir_full = os.path.join(input_dir.replace('/', '\\'), file_name)

        shutil.copy(input_dir_full, output_dir)


        delete_file(fn=file_name)

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

def update_frame(path):
    global canvas, frame_insert

    res = Image.open(path)
 
    resize_image = res.resize((160, 140))
    frame_insert = ImageTk.PhotoImage(resize_image)

    canvas.create_image(
        10,
        25, 
        anchor=NW, 
        image=frame_insert
    )

import desplice

# STYLE

style = ttk.Style(w)
style.theme_use('winnative')

# WIDGETS :)

Button_Input_folder = tkinter.Button(w, text ="Input Folder", relief=GROOVE, command=lambda: browseFiles(0))
Button_Output_folder = tkinter.Button(w, text ="Output Folder", relief=GROOVE, command=lambda: browseFiles(1))


Button_Render = tkinter.Button(w, text ="Render", relief=GROOVE, command=lambda: render_video(int(Fps_Text_Box.get(1.0, "end-1c")), file_name=FileName_Text_Box.get(1.0, "end-1c"), image_type=FileEnd_Text_Box.get(1.0, "end-1c")))
Button_SaveTemplate = tkinter.Button(w, text ="Save Settings", relief=GROOVE, command=lambda: save_templates())

heading = tkinter.Label(w, text='Frame DeSplice', font=("Helvetica", 12))
label_fn = tkinter.Label(w, text='File Name: ', font=("Helvetica", 9))
label_ft = tkinter.Label(w, text='File Type: ', font=("Helvetica", 9))
label_fps = tkinter.Label(w, text='FPS: ', font=("Helvetica", 9))
label_cn = tkinter.Label(w, text='Console Errors: ', font=("Helvetica", 9))

label_cur_frame = tkinter.Label(w, text='Frame: ' + cur_frame, font=("Helvetica", 10))

link1 = Label(w, text="Builds", fg="blue", cursor="hand2", font=('Helvetica 10 underline'))
link1.place(x=10,y=220)
link1.bind("<Button-1>", lambda e: os.system("start https://github.com/ToasterPNG/Frame DeSplice/releases"))

Input_Text_Box = Text(w, height=1.4, width=22)
Output_Text_Box = Text(w, height=1.4, width=22)
Fps_Text_Box = Text(w, height=0, width=6)
FileName_Text_Box = Text(w, height=0, width=9)
FileEnd_Text_Box = Text(w, height=0, width=9)
Console_Text_Box = Text(w, height=4, width=12)

progress = Progressbar(w, orient = HORIZONTAL,length = 100, mode = 'determinate')

# PACK STUFF

heading.pack(ipadx=10, ipady=10)
label_fps.place(x=10, y=124)
label_fn.place(x=10, y=149)
label_ft.place(x=10, y=176)
label_cn.place(x=180, y=152)
# label_cur_frame.place(x=310, y=70)

Button_Input_folder.place(x=10, y=50)
Button_Output_folder.place(x=10, y=80)
Button_Render.place(x=120, y=120)
# Button_SaveTemplate.place(x=10, y=214)

Input_Text_Box.place(x=90, y=53)
Input_Text_Box.insert('end', input_dir)

Output_Text_Box.place(x=100, y=83)
Output_Text_Box.insert('end', output_dir)

Fps_Text_Box.place(x=50, y=124)
Fps_Text_Box.insert('end', fps)

FileName_Text_Box.place(x=80, y=150)
FileName_Text_Box.insert('end', filename)

FileEnd_Text_Box.place(x=80, y=176)
FileEnd_Text_Box.insert('end', image_type)

Console_Text_Box.place(x=180, y=176)
Console_Text_Box.insert('end', errors)
Console_Text_Box.configure(state='disabled')

Console_Text_Box.tag_add("here", "1.0", "1.4")
Console_Text_Box.tag_config("here", background="black", foreground="red")

variable = StringVar(w)
print(list_of_templates)
variable.set(list_of_templates[2])
# tremplates = OptionMenu(w, variable, *list_of_templates, command=set_template)
tremplates = ttk.OptionMenu(w, variable, *list_of_templates, command=set_template)

tremplates.config(width=7)
set_template()

tremplates.place(x=80, y=211)

"""
os.chdir('..')
res = Image.open("assets\\split_1.png")
os.chdir('scripts')

resize_image = res.resize((160, 140))
frame_insert = ImageTk.PhotoImage(resize_image)

canvas.create_image(
    10,
    25, 
    anchor=NW, 
    image=frame_insert
)
canvas.place(x=300, y=80)
"""

progress.place(x=180, y=125)

#CheckBox_Setting_1 = Checkbutton(w, text='Funny Setting',variable=tkinter.IntVar(), onvalue=1, offvalue=0)
#CheckBox_Setting_1.place(x=10, y=120)


w.mainloop()