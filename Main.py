# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:02:32 2020

@author: HASSAN
"""

from tkinter import *
import os
from PIL import *
import random
import glob
import qrcode
from tkinter import filedialog
import pyodbc
#from datetime import date
#today = date.today()
#d4 = today.strftime("%b-%d-%Y")

def generate_png():
    
    from PIL import Image, ImageDraw, ImageFont
    #ID FRONT
    image = Image.open("Card Background/IDBackground.png","r")
    #image = Image.ANTIALIAS
    logo = Image.open("Card Background/LOGO.png","r")
    logo.resize((260, 144), Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    profile_pic = pic
    
    (x, y) = (50, 560)
    display =("INSTITUTE OF MANAGEMENT SCIENCES, PESHAWAR")
    colors = 'rgb(0, 51, 153)'
    font = ImageFont.truetype("Roboto-Bold.ttf", size=35)
    draw.text((x, y), display, fill=colors, font=font)
    
    (x, y) = (660, 60)
    display =("STUDENT")
    colors = 'rgb(0, 0, 0)'
    font = ImageFont.truetype("Roboto-Bold.ttf", size=38)
    draw.text((x, y), display, fill=colors, font=font)
    
    display = logo
    image.paste(display,(40, 40),mask=display)
    
    display = profile_pic
    image.paste(display,(620, 150))
    
    (x, y) = (50, 200)
    display = (name.get())
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=42)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (50, 250)
    display = cnic.get()
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=28)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (50, 290)
    display = program.get()
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=28)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (50, 330)
    display = "2019-2023"
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=28)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (50, 370)
    display = "GROUP-A"
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=28)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (50, 480)
    display = "DIRECTOR"
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('Roboto-Bold.ttf', size=24)
    draw.text((x, y), display, fill=color, font=font)
    
    
    image.save("Printed Cards/"+str(rollnumber.get())+'.png')
    
    #ID BACK
    
    image = Image.open("Card Background/IDBackground.png","r")
    draw = ImageDraw.Draw(image)
    
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=1,
    )
    qr.add_data(str(name.get())+str(cnic.get()))
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")
    display = img
    image.paste(display,(50, 50))
    
    (x, y) = (300, 50)
    display = ("Roll Number :     "+rollnumber.get())
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=24)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (300, 90)
    display = ("Father Name:     "+fatherName.get())
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=24)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (300, 130)
    display = ("Contact:             "+contact.get())
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (300, 170)
    display = ("Expiry Date:       September, 2023")
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (300, 210)
    add = adress.get()
    display = ("Permanent Adress:\n"+add)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (400, 400)
    display = ("If found return to")
    color = 'rgb(255, 0, 0)' # red color 
    font = ImageFont.truetype('Roboto-Bold.ttf', size=25)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (225, 430)
    display = ("INSTITUTE OF MANAGEMENT SCIENCES")
    color = 'rgb(0, 51, 153)' # navy color 
    font = ImageFont.truetype('Roboto-Bold.ttf', size=29)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (185, 470)
    display = ("        I-A,Sector E-5, Phase VII, Hayatabad, Peshawar-Pakistan\n Tel: +92 91 9217451-2, 5861024-5, Fax: +92 91 9217407, 5861026")
    color = 'rgb(0, 0, 0)' # navy color 
    font = ImageFont.truetype('arial.ttf', size=20)
    draw.text((x, y), display, fill=color, font=font)
    
    (x, y) = (365, 520)
    display = ("email: info@imsciences.edu.pk")
    color = 'rgb(0, 0, 0)' # navy color 
    font = ImageFont.truetype('arial.ttf', size=18)
    draw.text((x, y), display, fill=color, font=font)

    image.save("Printed Cards/"+str(rollnumber.get())+'back.png')
    
def roll_check():
    
    rollnum=str(rollnumber.get())
    
    global txt_files
    txt_files = glob.glob("Printed Cards/*.png")
    rnum=str("Printed Cards\\"+rollnum+".png")
    if rnum in txt_files:
        alreadyexistdata()
    else:
        register_user()

def alreadyexistdata():
    
    global screen1
    screen1=Toplevel(screen)
    screen1.geometry("300x100")
    screen1.title("RollNum Already Exist")
    
    Label(screen1, text = "Roll Number Already Exist").pack()
    Button(screen1, text = "Okay", width = 10, height = 1, command = screen1.destroy).pack()

 
def register_user():
    
    name_info = name.get()
    fatherName_info = fatherName.get()
    cnic_info = cnic.get()
    rollnumber_info = rollnumber.get()
    program_info = program.get()
    contact_info = contact.get()
    adress_info = adress.get()
    
    
    file=open("All Data.txt", "a")
    file.write(name_info+",")
    file.write(fatherName_info+",")
    file.write(cnic_info+",")
    file.write(rollnumber_info+",")
    file.write(program_info+",")
    file.write(contact_info+",")
    file.write(adress_info+"\n")
    file.close()
    generate_png()
    
    name_entry.delete(0, END)
    fatherName_entry.delete(0, END)
    cnic_entry.delete(0,END)
    roll_number_entry.delete(0, END)
    program_entry.delete(0, END)
    contact_entry.delete(0, END)
    adress_entry.delete(0, END)
    
    Label(screen, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
    
    

def open_img():
    # Select the Imagename from a folder
    x = openfilename()
    
    global pic
    
    # opens the image
    pic = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    pic = pic.resize((250, 300), Image.ANTIALIAS)
    #return pic

def openfilename():

	# open file dialog box to select image
	# The dialogue box has a title "Open"
	filename = filedialog.askopenfilename(title ='Open')
	return filename
    
 
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x600")
    screen.title("ID Generator")
    
    Label(screen, text = "Please enter details below").pack()
    Label(screen, text = "").pack()
    
    global name
    global name_entry
    name = StringVar()
    
    global fatherName
    global fatherName_entry
    fatherName = StringVar()
    
    global cnic
    global cnic_entry
    cnic = StringVar()
    
    global rollnumber
    global roll_number_entry
    rollnumber = StringVar()
    
    global program
    global program_entry
    program = StringVar()
    
    global contact
    global contact_entry
    contact = StringVar()
    
    global adress
    global adress_entry
    adress = StringVar()
    
    
    Label(screen, text = "Name").pack()
    name_entry = Entry(screen, textvariable = name)
    name_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "Father Name").pack()
    fatherName_entry = Entry(screen, textvariable = fatherName)
    fatherName_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "CNIC NO").pack()
    cnic_entry = Entry(screen, textvariable = cnic)
    cnic_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "Roll Number").pack()
    roll_number_entry = Entry(screen, textvariable = rollnumber)
    roll_number_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "Program").pack()
    program_entry = Entry(screen, textvariable = program)
    program_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "Contact Number").pack()
    contact_entry = Entry(screen, textvariable = contact)
    contact_entry.pack()
    Label(screen, text = "").pack()
    
    Label(screen, text = "Adress").pack()
    adress_entry = Entry(screen, width=40 ,textvariable = adress)
    adress_entry.pack()
    Label(screen, text = "").pack()
    
    Button(screen, text ='Import image', command = open_img).pack()
    Label(screen, text = "").pack()
    Button(screen, text = "Generate", width = 10, height = 1, command = roll_check).pack()
    
    screen.mainloop()
    
main_screen()