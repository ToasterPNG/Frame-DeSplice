# Frame-DeSplice v1.1
Frame DeSplice will take a sequence of images and then turn it into a video with ffmpeg.

## Settings

FPS, FileName, FileType, Input and Output Folder
These settings can be saved in .fds files, to save your
Current settings click the "Save Settings" button

## Templates

The template button which is the current template
Sellected will open up a window that allows you to choose

A template, to save a template click the "Save Settings" button.
The default name in the templates folder will be template.fds
Which you cannot rename yet through the program.

## Progress Bar

When you click the "Render" button a progress bar will start
And will notify you when it finishes by going back to 0%

## Error Log

There is an error log in the a uneditable TextBox labled
"Console Errors", this output/errors will be written in a 
File named "ErrorLog.log"

Note that the errors wont be in an error log or the TextBox
If the program crashes.

## Installing

Dependencies include python, OpenCV Package and Pillow
The packages (OpenCV Package and Pillow) are installed throught the
Installer when you first run it.

If the installer doesnt work run these pip commands:

pip install opencv-python==4.5.1.48
pip install Pillow==8.2.0
  
 

![window](https://user-images.githubusercontent.com/79758393/175777297-feecc0d7-3ff2-4a66-a8d8-cfaef2d50866.jpg)
