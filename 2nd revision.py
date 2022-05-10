import os
import math
from PIL import Image
import shutil  # ?
import tkinter
from tkinter import filedialog

THRESHOLD = 8
INPUT_DIRECTORY =tkinter.filedialog.askdirectory(title='where da memes boiii')
OUTPUT_DIRECTORY =tkinter.filedialog.askdirectory(title= 'where do you want em?')

NOT_JPGS = tkinter.filedialog.askdirectory(title= 'if you are a fool, this is where your not jpegs are')
UNABLETOCROP_DIR = tkinter.filedialog.askdirectory(title="we can't crop those")
fullpath = INPUT_DIRECTORY + '/' + filename

# Get color difference


def color_difference(pixel1, pixel2):
    difference = math.sqrt(
        abs(pixel2[0] - pixel1[0]) ** 2 + abs(pixel2[1] - pixel1[1]) ** 2 + abs(pixel2[2] - pixel1[2]) ** 2)
    return difference


# Assumes image has watermark and attempts to crop
def crop():
        for file in os.listdir(INPUT_DIRECTORY):  # For each file in directory)
            print('[error]:'+filename +”failed”+str(IOError))
    shutil.move(fullpath, UNABLETOCROP_DIR)
    # movefile(filename,UNABLETOCROP_DIR)

    Else:
    filename = os.fsdecode(file)  # Get filename
    if filename.endswith(".jpg"):
    # img = Image.open(INPUT_DIRECTORY + "/" + filename)
        With
    Image.open(INPUT_DIRECTORY + "/" + filename) as img
    pix = img.load()
    width, length = img.size
    curr_y = length - 1
    Else: \
        shutil.move(fullpath, NOT_JPGS)
    # movefile(filename, NOT_JPGS)

    # While color difference is less than threshold, move up and decrease Y height
    while color_difference(pix[0, curr_y], pix[0, length - 1]) < THRESHOLD:
        curr_y = curr_y - 1
    watermark_size = length - curr_y

    # For possible bad crops since the average watermark size is 21 pixels or less
    cropped = img.crop((0, 0, width, length - watermark_size))


if watermark_size > 21:
    print("[Skipped]:", filename, watermark_size)

    # img.show()
    # cropped.show()
shutil.move()
else:  # Save image
cropped.save(UNABLETOCROP_DIR + filename, format='JPEG', subsampling=0, quality=100)


# Just check image for iFunny watermark
# seems incomplete
def has_watermark():
    pass


def menu():
    print("Cropping images...")
    crop()
    print("Done")


if __name__ == "__main__":
    menu()

# this is to make a binary file for the file to copy it without shutil but I need to navigate them to  the directory of the
# Def movefile(filename, DESTINATION,  )
bindata = open(filename, r + b)

In
DESTINATION
open(filename, "w")
f.write(bindata)
f.close0
f.close
os.remove(fullpath, )
