# Import Tkinter GUIs & web browser access

from tkinter import *
import webbrowser


# create an overall function for GUI interface to interact with
def climatetool(event):
    rentry = txt.get()  # retrieve the response from the user from input window
    while rentry:  # beginning the loop so that interface can process user response
        if rentry in ["local","Local"]:  # Processing the user input as if/else statement
            root.destroy()

            def twoloop(event):  # subfunction for user choosing local
                rentry2 = txt2.get()# retrieve the response from the user from input window
                if rentry2 in ["climate change resiliency", "Climate Change Resiliency"]:
                    root2.destroy()
                    def thrloop(event):
                        rentry3 = txt3.get()

                    root3 = Tk()  # enable tkinter for the main function to use
                    root3.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                    root3.title("Decision Support Tool")  # Create overarching header for the interface
                    thelabel3 = Label(root2,
                                      text="Decision Support Tool- Climate")  # add subset header for the interface
                    thelabel3.pack()  # put GUI onto interface for usage
                    frame3 = Frame(root2, width=500, height=500)  # frame user interface
                    frame3.pack()  # put GUI onto interface for usage
                    bottomframe3 = Frame(root2)  # frame user interface
                    bottomframe3.pack(side=BOTTOM)  # put GUI onto interface for usage
                    lbl3 = Label(frame2, text="Which Jurisdiction is your location in? [PA, Other] ")
                    lbl3.pack()  # put GUI onto interface for usage
                    txt3 = Entry(root2, width=10)
                    txt3.pack()  # put GUI onto interface for usage
                    rbutton3 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
                    rbutton3.bind("<Button-1>", thrloop)
                    rbutton3.pack()  # put GUI onto interface for usage
                    root3.mainloop()  # allow program to remain on user PC

            root2 = Tk()  # enable tkinter for the main function to use
            root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            root2.title("Decision Support Tool")  # Create overarching header for the interface
            thelabel2 = Label(root2,text="Decision Support Tool- Climate")  # add subset header for the interface
            thelabel2.pack()  # put GUI onto interface for usage
            frame2 = Frame(root2, width=500, height=500)  # frame user interface
            frame2.pack()  # put GUI onto interface for usage
            bottomframe2 = Frame(root2)  # frame user interface
            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
            lbl2 = Label(frame2,
                         text="What topic are you interested in? [climate change resiliency, "
                              "climate change and ecosystems] ")
            lbl2.pack()  # put GUI onto interface for usage
            txt2 = Entry(root2, width=10)
            txt2.pack()  # put GUI onto interface for usage
            rbutton2 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
            rbutton2.bind("<Button-1>", twoloop)
            rbutton2.pack()  # put GUI onto interface for usage
            root2.mainloop()  # allow program to remain on user PC


root = Tk()  # enable tkinter for the main function to use
root.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
root.title("Decision Support Tool")  # Create overarching header for the interface
thelabel = Label(root, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
thelabel.pack()  # put GUI onto interface for usage
frame = Frame(root, width=500, height=500)  # frame user interface
frame.pack()  # put GUI onto interface for usage
bottomframe = Frame(root)  # frame user interface
bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage

lbl = Label(frame, text="What is the scope of your project? [Local, Regional, National, Global] ")
lbl.grid(column=0, row=0)
lbl.pack()  # put GUI onto interface for usage
txt = Entry(root, width=10)
txt.pack()  # put GUI onto interface for usage

rbutton = Button(frame, text='Run Fish Loop', fg='black', bg='yellow')
rbutton.bind("<Button-1>", climatetool)
rbutton.pack()  # put GUI onto interface for usage

root.mainloop()  # allow program to remain on user PC