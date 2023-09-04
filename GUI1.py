from tkinter import *

root = Tk()
root.title("QMU Data Converter")

ogdirectory = Entry(root, width = 50)
ogdirectory.grid(row=4,column=0)


lines = Entry(root, width = 50)
lines.grid(row=8,column=0)



MyLabel1 = Label(root, text="Greevesis epic code")
MyLabel1.grid(row=1,column=0)

MyLabel3 = Label(root, text="Enter original file directory: ")
MyLabel3.grid(row=3,column=0)

MyLabel4 = Label(root, text="Enter number of lines in the file: ")
MyLabel4.grid(row=7,column=0)

MyLabel4 = Label(root, text="Enter new file directory: ")
MyLabel4.grid(row=5,column=0)

newdirectory = Entry(root, width = 50)
newdirectory.grid(row=6,column=0)

def start():
    original = open( ogdirectory.get(),"r")
    new = open(newdirectory.get(), 'w')
    linenum= lines.get()
    linenum = int(linenum)
    for i in range(0,linenum):
        line = str(original.readline())
        splitline = line.split()
        size = int(splitline[0])
        if size < 40000:
            line = str(line)
            new.write(line)

            

MyButton = Button(root, text="Start", fg = "red",padx=50,pady=30, command=start)
MyButton.grid(row=2,column=0)

root.mainloop()