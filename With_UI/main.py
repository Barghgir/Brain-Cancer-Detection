# Import the required Libraries
import tkinter as tk
from tkinter import ttk, filedialog
import os

from functions import *
from PIL import ImageTk, Image


win = tk.Tk()
win.config(padx=20, pady=20)


def callback(panel_img, path=address):
    image = ImageTk.PhotoImage(Image.open(path))
    panel_img.configure(image=image)
    panel_img.image = image


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.jpg')])
    if file:
        filepath = os.path.abspath(file.name)
        print(filepath)
        img_path = resize(img_path=filepath)

        gray_path = BGR2GRAY(img_path=img_path)
        callback(panel1, path=gray_path)

        thr_bn_path = THRESH_BINARY(img_path=img_path)
        callback(panel2, path=thr_bn_path)

        thr_bn_inv_path = THRESH_BINARY_INV(img_path=img_path)
        callback(panel3, path=thr_bn_inv_path)

        morph_path = MORPH_CLOSE(img_path=thr_bn_path)
        callback(panel4, path=morph_path)

        closed_path = erode_and_dilate_func(img_path=morph_path)
        callback(panel5, path=closed_path)

        env_image_path = show_environment_of_tumor(img_path=img_path)
        callback(panel7, path=env_image_path)

        tumor_path = show_tumor(img_path=img_path)
        callback(panel8, path=tumor_path)


# Add a Label widget
label = tk.Label(win, text="Click the Button to browse the Files", font='Georgia 13')
label.grid(row=0, column=0, columnspan=3)

# Create a Button
browse_button = ttk.Button(win, text="Browse", command=open_file)
browse_button.grid(row=0, column=3)

# Create other labels for each picture
label_fig1 = tk.Label(win, text="Original picture in GRAY environment", font='Georgia 8')
label_fig1.grid(row=2, column=0)

label_fig2 = tk.Label(win, text="Binary Threshold image", font='Georgia 8')
label_fig2.grid(row=2, column=1)

label_fig3 = tk.Label(win, text="Reverse Binary Threshold image", font='Georgia 8')
label_fig3.grid(row=2, column=2)

label_fig4 = tk.Label(win, text="Threshold with 'CLOSE Morphology'", font='Georgia 8')
label_fig4.grid(row=2, column=3)

label_fig5 = tk.Label(win, text="Erosion and Dilation of image", font='Georgia 8')
label_fig5.grid(row=4, column=0)

label_fig6 = tk.Label(win, text="Islamic Azad University", font='Georgia 12')
label_fig6.grid(row=4, column=1)

label_fig7 = tk.Label(win, text="Delimitation of tumor", font='Georgia 8')
label_fig7.grid(row=4, column=2)

label_fig8 = tk.Label(win, text="Tumor Recognition", font='Georgia 8')
label_fig8.grid(row=4, column=3)


# Create empty image and add it
# empty_image = PhotoImage(file="empty_image0.png")   This makes errors
empty_image = ImageTk.PhotoImage(Image.open("empty_image0.png"))
azad_image = ImageTk.PhotoImage(Image.open("azad_logo.png"))

panel1 = tk.Label(win, image=empty_image)
panel1.grid(row=1, column=0)

panel2 = tk.Label(win, image=empty_image)
panel2.grid(row=1, column=1)

panel3 = tk.Label(win, image=empty_image)
panel3.grid(row=1, column=2)

panel4 = tk.Label(win, image=empty_image)
panel4.grid(row=1, column=3)

panel5 = tk.Label(win, image=empty_image)
panel5.grid(row=3, column=0)

panel6 = tk.Label(win, image=azad_image)
panel6.grid(row=3, column=1)

panel7 = tk.Label(win, image=empty_image)
panel7.grid(row=3, column=2)

panel8 = tk.Label(win, image=empty_image)
panel8.grid(row=3, column=3)


win.mainloop()
