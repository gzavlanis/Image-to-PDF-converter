from PIL import Image
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from os import startfile

Image.MAX_IMAGE_PIXELS = None

def save_file(f):
    f= filedialog.asksaveasfilename(initialfile= 'Untitled.pdf', defaultextension=".pdf", filetypes=[("PDF Documents","*.pdf")])

def converter():
    file= filedialog.askopenfilename(filetypes= [("Image files", ".jpg .jpeg")])
    img1= Image.open(file)
    pdf1= img1.convert('RGB')
    save_file(pdf1)

def multiple_converter():
    image_list= []
    while True:
        files= filedialog.askopenfilenames(filetypes= [("Image files", ".jpg .jpeg")])
        for f in files:
            img= Image.open(f)
            pdf= img.convert('RGB')
            image_list.append(pdf)
        if files== '':
            break
    path= filedialog.asksaveasfilename(initialfile= 'Untitled.pdf', defaultextension=".pdf", filetypes=[("PDF Document","*.pdf")])
    image_list[0].save(path, 'PDF', save_all= True, append_images= image_list[1:])

def convert_to_image():
    pdf= filedialog.askopenfilename(filetypes= [("PDF files", ".pdf")])
    pages= convert_from_path(pdf, poppler_path= r'C:/Users/User/Downloads/Release-22.04.0-0/poppler-22.04.0/Library/bin')
    for i in range(len(pages)):
        path= filedialog.asksaveasfilename(initialfile= 'Untitled.jpg', defaultextension=".jpg", filetypes=[("Image file","*.jpg")])
        pages[i].save(path, 'JPEG')

def open_instructions():
    messagebox.showinfo(title= 'Instructions', message= 'Button 1 "Single image to PDF" Converts a single image to pdf file\n\n Button 2 "Multiple images to PDF" Converts multiple images and combine them to a single pdf file\n\n Button 3 "PDF to multiple images" Converts a pdf to multiple image files (jpg format)\n\n Button 4 "Quit" Terminates the application')
   
ctk.set_appearance_mode('Light')

parent= ctk.CTk()
parent.title('Image to PDF converter')
parent.geometry('400x300')
parent.resizable(False, False)

label1= tk.Label(master= parent, text= 'Image to pdf converter version 1', font= ('Arial', 20))
label1.grid(row= 0, pady= 1, padx= 15)

label2= tk.Label(master= parent, text= 'Select function', font= ('Arial', 14))
label2.grid(row= 2, pady= 1, padx= 15)

button1= ctk.CTkButton(master= parent, text= 'Single image to PDF', fg_color= '#000137', hover_color= "#404040", corner_radius= 20, text_font= '30', text_color= 'white', command= converter)
button1.place(relx= 0.5, rely= 0.3, anchor= tk.CENTER)

button2= ctk.CTkButton(master= parent, text= 'Multiple images to PDF', fg_color= '#02055a', hover_color= "#404040", corner_radius= 20, text_font= '30', text_color= 'white', command= multiple_converter)
button2.place(relx= 0.5, rely= 0.45, anchor= tk.CENTER)

button3= ctk.CTkButton(master= parent, text= 'PDF to multiple images', fg_color= '#02198b', hover_color= "#404040", corner_radius= 20, text_font= '30', text_color= 'white', command= convert_to_image)
button3.place(relx= 0.5, rely= 0.6, anchor= tk.CENTER)

button5= ctk.CTkButton(master= parent, text= 'Show instructions', fg_color= '#5099f4', hover_color= "#404040", corner_radius= 20, text_font= '30', text_color= 'white', command= open_instructions)
button5.place(relx= 0.5, rely= 0.75, anchor= tk.CENTER)

button4= ctk.CTkButton(master= parent, text= 'Quit', fg_color= '#800000', hover_color= "#404040", corner_radius= 20, text_font= '30', text_color= 'white', command= parent.destroy)
button4.place(relx= 0.5, rely= 0.9, anchor= tk.CENTER)

parent.mainloop()