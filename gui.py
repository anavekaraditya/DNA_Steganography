from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter.font import Font

#from numpy import WRAP, pad
import main

class Home:
    def __init__(self, root):
        self.root = root
        self.gui_function()

    def gui_function(self):
        self.design_gui()

    def encrypt(self):
        root.wm_state('iconic')
        top_level = Toplevel()
        top_level.geometry("250x230")
        def open_file():
            global filepath
            filepath = filedialog.askopenfile(initialdir="/C", title="Select", filetypes=(("png files", "*.*"),
                        ("all files", ".")))

        def set_dir():
            global outpath
            outpath = filedialog.askdirectory()    
        
        def get_encrypt():
            msg = message_entry.get()
            key = key_entry.get()
            in_img = filepath.name
            out_img = outpath
            print(msg)
            print(key)
            print(filepath.name)
            print(outpath)
            main.encrpt_crypteg(msg,key,in_img,out_img) 
            text2.set("Successfully encrypted and stored @ {}".format(outpath))   

        message_lbl = Label(top_level, text="Message",font=('Monsterant 10 bold'),padx=10,pady=10)
        message_lbl.grid(row=0,column=1 ,columnspan=2)
        message_entry = Entry(top_level)
        message_entry.grid(row=0,column=4, columnspan=4,padx=10,pady=10)

        key_lbl = Label(top_level, text="Key",font=('Monsterant 10 bold'),padx=10,pady=10)
        key_lbl.grid(row=1, column=1, columnspan=2)
        key_entry = Entry(top_level)
        key_entry.grid(row=1, column=4, columnspan=2,padx=10,pady=10)

        input_path = Label(top_level, text="Input Path",font=('Monsterant 10 bold'),padx=10,pady=10)
        input_path.grid(row=2, column=1,columnspan=2)
        browse_input = Button(top_level, text="Browse", command=open_file,font=('Monsterant 10 bold'))
        browse_input.grid(row=2, column=2,columnspan=4)

        output_path = Label(top_level, text="Output Path",font=('Monsterant 10 bold'),padx=10,pady=10)
        output_path.grid(row=3, column=1,columnspan=2)
        browse_output = Button(top_level, text="Browse", command=set_dir,font=('Monsterant 10 bold'))
        browse_output.grid(row=3, column=2,columnspan=4)
        btn4 = Button(top_level, text="Submit", command=get_encrypt,font=('Monsterant 10 bold'))
        btn4.grid(row=4, column=1,columnspan=6, padx=10, pady=10)
        text2 = tkinter.StringVar()
        text2.set(" ")
        status = Label(top_level,textvariable=text2,font=('Monsterant 10 bold'))
        status.grid(row=5,columnspan=6)

    def decrypt(self):
        root.wm_state('iconic')
        top_level = Toplevel()
        top_level.geometry("250x200")

        def open_file():
            global filepath
            filepath = filedialog.askopenfile(initialdir="/C", title="Select", filetypes=(("png files", "*.*"),
                        ("all files", ".")))

        def get_decrypt():
            global a
            key = key_entry.get()
            in_img = filepath.name
            print(key)
            print(filepath.name)
            msg = main.decrpt_crypteg(key,in_img)
            print(msg)
            text.set("Decrypted Message: {}".format(msg)) 

        key_lbl = Label(top_level, text="Key",font=('Monsterant 10 bold'),padx=30,pady=20)
        key_lbl.grid(row=1, column=0)
        key_entry = Entry(top_level)
        key_entry.grid(row=1, column=1)

        input_path = Label(top_level, text="Input Path",font=('Monsterant 10 bold'))
        input_path.grid(row=2, column=0,padx=10,pady=10)
        browse_input = Button(top_level, text="Browse", command=open_file,font=('Monsterant 10 bold'))
        browse_input.grid(row=2, column=1)
        btn5 = Button(top_level, text="Submit", command=get_decrypt,font=('Monsterant 10 bold'))
        btn5.grid(row=3, column=1, padx=10, pady=10)
        text = tkinter.StringVar()
        text.set("Decrypted Message: ")
        msg_output = Label(top_level,textvariable=text,font=('Monsterant 10 bold'))
        msg_output.grid(row=4,columnspan=4)

    def design_gui(self):
        lbl1 = Label(root, text="Welcome to CRYPTEG",font=('Axis 20 bold'),padx=30,pady=30)
        lbl1.grid(row=0, columnspan=10)
        lbl2 = Label(root, text="This is a Crypto-Stegno Tool to encrypt and decrypt your messages.",font=('Monsterant 14 bold'),padx=30,pady=30)
        lbl2.grid(row=1, columnspan=10)
        btn1 = Button(root, text="Encrypt", command=self.encrypt,font=('Monsterant 10 bold'))
        btn1.grid(row=3, columnspan=10, padx=10, pady=10,ipadx=10,ipady=10)
        btn1 = Button(root, text="Decrypt", command=self.decrypt,font=('Monsterant 10 bold'))
        btn1.grid(row=4, columnspan=10, padx=10, pady=10,ipadx=10,ipady=10)

if __name__ == '__main__':
    root = Tk()
    root.title("CRYPTEG")
    root.geometry("685x350")
    root.eval('tk::PlaceWindow . center')
    app = Home(root)
    root.mainloop()