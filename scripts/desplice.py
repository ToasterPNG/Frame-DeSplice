import librarys, cv2, os, shutil, tkinter


def render_video(fps, file_name='DeSpliced.mp4', image_type='png'): # i add presets maybe some time :'(
    pass
"""
    global progress, errors

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
            update_frame(os.path.join(input_dir, image))
            video.write(cv2.imread(os.path.join(input_dir, image)))

        video.release()

        update_progressbar(20)
        

        input_dir_full = os.path.join(input_dir.replace('/', '\\'), file_name)

        shutil.copy(input_dir_full, output_dir)

        delete_file(fn=file_name)

    except Exception as e:

        Console_Text_Box = Text(w, height=4, width=12)

        errors = e

        Console_Text_Box.insert('end', e)
        Console_Text_Box.configure(state='disabled')
        Console_Text_Box.place(x=180, y=176)

"""

def read_desplicing_data():

    with open('desplicing.dat') as f:
        file_data = f.readlines()

    return file_data[0]