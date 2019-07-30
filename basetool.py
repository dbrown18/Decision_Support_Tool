# Import Tkinter GUIs & web browser access

from tkinter import *
import webbrowser


# create an overall function for GUI interface to interact with
def basetool(event):
    rentry = txt.get()  # retrieve the response from the user from input window
    while rentry:
        if rentry in ["scope", "Scope"]:
            root.destroy()  # remove the original interface from the screen
            
            def form(event):
                rentryp = txtp.get()  # retrieve the response from the user from input window
                if rentryp in ["local", " Local"]:  # Processing the user input as if/else statement

                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open('"https://www.chesapeakebay.net/"')
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage

                elif rentry in ["Jurisdiction", "jurisdiction"]:  # Processing the user input as if/else statement
                    root.destroy()  # remove the original interface from the screen

                    def nesttoolone(event):
                        rentry2 = txt2.get()  # retrieve the response from the user from input window

                        if rentry2 in ["database", "Database"]:  # Processing the user input as if/else statement
                            root2.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("https://www.chesapeakebay.net/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        elif rentry2 in ["mapping", "Mapping"]:  # Processing the user input as if/else statement
                            root2.destroy()  # remove the original interface from the screen

                            def thrloop(event):
                                rentry3 = txt3.get()  # retrieve the response from the user from input window

                                if rentry3 in ["Static Mapping", "static mapping"]:  # Processing the user input
                                    # as if/else statement
                                    root3.destroy()  # remove the original interface from the screen
                                    rootf = Tk()  # enable tkinter for the main function to use
                                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                                    bottomframef = Frame(rootf)  # frame user interface
                                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                                    Label(rootf, text="This is where the title goes: Use link- "
                                          , fg="light green",
                                          bg="dark green",
                                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                                    def openlink(event):
                                        webbrowser.open("https://www.chesapeakebay.net/")
                                        rootf.destroy()  # remove the original interface from the screen

                                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                                    buttonf.bind("<Button-1>", openlink)
                                    buttonf.pack()  # put GUI onto interface for usage
                                elif rentry3 in ["dynamic mapping", "Dynamic Mapping"]:  # Processing the user input
                                    # as if/else statement
                                    root3.destroy()  # remove the original interface from the screen
                                    rootf = Tk()  # enable tkinter for the main function to use
                                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                                    bottomframef = Frame(rootf)  # frame user interface
                                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                                    Label(rootf, text="This is where the title goes: Use link- "
                                          , fg="light green",
                                          bg="dark green",
                                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                                    def openlink(event):
                                        webbrowser.open("https://www.chesapeakebay.net/")
                                        rootf.destroy()  # remove the original interface from the screen

                                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                                    buttonf.bind("<Button-1>", openlink)
                                    buttonf.pack()  # put GUI onto interface for usage
                                elif rentry3 in ["Story Mapping", "story mapping"]:  # Processing the user input
                                    # as if/else statement
                                    root3.destroy()  # remove the original interface from the screen
                                    rootf = Tk()  # enable tkinter for the main function to use
                                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                                    bottomframef = Frame(rootf)  # frame user interface
                                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                                    Label(rootf, text="This is where the title goes: Use link- "
                                          , fg="light green",
                                          bg="dark green",
                                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                                    def openlink(event):
                                        webbrowser.open("https://www.chesapeakebay.net/")
                                        rootf.destroy()  # remove the original interface from the screen

                                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                                    buttonf.bind("<Button-1>", openlink)
                                    buttonf.pack()  # put GUI onto interface for usage
                                else:  # Processing the user input as if/else statement
                                    pass

                            root3 = Tk()  # enable tkinter for the main function to use
                            root3.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                            root3.title("Decision Support Tool")  # Create overarching header for the interface
                            thelabel2 = Label(root3,
                                              text="Decision Support Tool- Base Tool")  # add subset header for the
                            # interface
                            thelabel2.pack()  # put GUI onto interface for usage
                            frame3 = Frame(root3, width=500, height=500)  # frame user interface
                            frame3.pack()  # put GUI onto interface for usage
                            bottomframe2 = Frame(root3)  # frame user interface
                            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
                            lbl2 = Label(frame3,
                                         text="What type of Mapping Service? [Static Mapping, Dynamic Mapping, "
                                              "Story Mapping] ")
                            lbl2.pack()  # put GUI onto interface for usage
                            txt3 = Entry(root3, width=10)
                            txt3.pack()  # put GUI onto interface for usage
                            rbutton2 = Button(frame3, text='Run Base Tool', fg='black', bg='yellow')
                            rbutton2.bind("<Button-1>", thrloop)
                            rbutton2.pack()  # put GUI onto interface for usage
                            root3.mainloop()  # allow program to remain on user PC

                        elif rentry2 in ["Interactive Program", 'interactive program']:  # Processing the user input as
                            # if/else statement
                            root2.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("https://www.chesapeakebay.net/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage

                        elif rentry2 in ["Other", 'other']:  # Processing the user input as
                            # if/else statement
                            root2.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("https://www.chesapeakebay.net/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        elif rentry2 in ["Other", "other"]:  # Processing the user input as if/else statement
                            root2.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link-"
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("https://www.chesapeakebay.net/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        else:  # Processing the user input as if/else statement
                            pass

                    root2 = Tk()  # enable tkinter for the main function to use
                    root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                    root2.title("Decision Support Tool")  # Create overarching header for the interface
                    thelabel2 = Label(root2,
                                      text="Decision Support Tool- Base Tool")  # add subset header for the interface
                    thelabel2.pack()  # put GUI onto interface for usage
                    frame2 = Frame(root2, width=500, height=500)  # frame user interface
                    frame2.pack()  # put GUI onto interface for usage
                    bottomframe2 = Frame(root2)  # frame user interface
                    bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
                    lbl2 = Label(frame2, text="What format would be helpful for your purpose? [Database, Mapping, "
                                              "Interactive Program, Other ")
                    lbl2.pack()  # put GUI onto interface for usage
                    txt2 = Entry(root2, width=10)
                    txt2.pack()  # put GUI onto interface for usage
                    rbutton2 = Button(frame2, text='Run Base Loop', fg='black', bg='yellow')
                    rbutton2.bind("<Button-1>", nesttoolone)
                    rbutton2.pack()  # put GUI onto interface for usage
                    root2.mainloop()  # allow program to remain on user PC
                elif rentry in ["Regional", "regional"]:  # Processing the user input as if/else statement
                    root.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link- "
                          , fg="light blue",
                          bg="dark blue",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="gold4",
                          bg="gold",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://www.chesapeakebay.net/")
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='IndianRed2')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage

                elif rentry in ["National", "national"]:  # Processing the user input as if/else statement
                    root.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://www.chesapeakebay.net/")
                        rootf.destroy()  # remove the original interface from the screen
                        buttonf = Button(rootf, text='click here', fg="black", bg='green')
                        buttonf.bind("<Button-1>", openlink)
            rootp = Tk()  # enable tkinter for the main function to use
            rootp.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            rootp.title("Decision Support Tool")  # Create overarching header for the interface
            thelabelp = Label(rootp, text="Decision Support Tool- Base Tool")  # add subset header for the interface
            thelabelp.pack()  # put GUI onto interface for usage
            framep = Frame(rootp, width=500, height=500)  # frame user interface
            framep.pack()  # put GUI onto interface for usage
            bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage
            lblp = Label(frame, text="How would you like to start looking for tools? {by format, by scope]  ")
            lblp.grid(column=0, row=0)
            lblp.pack()  # put GUI onto interface for usage
            txtp = Entry(rootp, width=10)
            txtp.pack()  # put GUI onto interface for usage
            rbuttonp = Button(framep, text='Run Climate Tool', fg='black', bg='yellow')
            rbuttonp.bind("<Button-1>", form)
            rbuttonp.pack()  # put GUI onto interface for usage
            rootp.mainloop()  # allow program to remain on user PC

        elif rentry in ["by format", "By Format"]:
            root.destroy()

        def form(event):
            rentryp = txtp.get()  # retrieve the response from the user from input window
            while rentryp:  # beginning the loop so that interface can process user response\
                if rentryp in ["database", "Database"]:
                    rootp.destroy()  # remove the original interface from the screen

                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open('"https://www.chesapeakebay.net/"')
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                elif rentryp in ["Interface Program","inteface program"]:
                    rootp.destroy()  # remove the original interface from the screen

                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open('"https://www.chesapeakebay.net/"')
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                elif rentryp in ["other","Other"]:
                    rootp.destroy()  # remove the original interface from the screen

                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="This is where the title goes: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open('"https://www.chesapeakebay.net/"')
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                elif rentryp in ["mapping", "Mapping"]:
                    rootp.destroy()
                    def map(event):
                        claim = txtc.get()
                        if claim in ["story mapping", "Story Mapping"]:
                            rootc.destroy()  # remove the original interface from the screen

                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link-"
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open('"https://www.chesapeakebay.net/"')
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        elif claim in ["Dynamic Mapping", "dynamic mapping"]:
                            rootc.destroy()  # remove the original interface from the screen

                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="This is where the title goes: Use link-"
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open('"https://www.chesapeakebay.net/"')
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        elif claim in ["Static Mapping", "static mapping"]:
                            rootc.destroy()
                            def last(event):
                                sclaim = txtv.get()
                                def specific(event):
                                    if sclaim in ["bla"]:
                                        rootv.destroy()  # remove the original interface from the screen

                                        rootf = Tk()  # enable tkinter for the main function to use
                                        rootf.title("Decision Support Tool")  # Create overarching header
                                        # for the interface
                                        bottomframef = Frame(rootf)  # frame user interface
                                        bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                                        Label(rootf, text="This is where the title goes: Use link-"
                                              , fg="light green",
                                              bg="dark green",
                                              font="Helvetica 16 bold italic").pack()  # put GUI onto
                                        # interface for usage

                                        def openlink(event):
                                            webbrowser.open('"https://www.chesapeakebay.net/"')
                                            rootf.destroy()  # remove the original interface from the screen

                                        buttonf = Button(rootf, text='click here', fg="black", bg='red')
                                        buttonf.bind("<Button-1>", openlink)
                                        buttonf.pack()  # put GUI onto interface for usage
                            rootv = Tk()
                            rootv.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                            rootv.title("Decision Support Tool")  # Create overarching header for the interface
                            thelabelv = Label(rootv,
                                              text="Decision Support Tool- Base Tool")
                            # add subset header for the interface
                            thelabelv.pack()  # put GUI onto interface for usage
                            framev = Frame(rootv, width=500, height=500)  # frame user interface
                            framev.pack()  # put GUI onto interface for usage
                            bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage

                            lblv = Label(frame,
                                         text="What format do you prefer? "
                                              "[Database, Mapping, Interface Program, Other]  ")
                            lblv.grid(column=0, row=0)
                            lblv.pack()  # put GUI onto interface for usage
                            txtv = Entry(rootv, width=10)
                            txtv.pack()  # put GUI onto interface for usage

                            rbuttonv = Button(framev, text='Run Climate Tool', fg='black', bg='yellow')
                            rbuttonv.bind("<Button-1>", last)
                            rbuttonv.pack()  # put GUI onto interface for usage

                            rootv.mainloop()  # allow program to remain on user PC

                    rootc = Tk()  # enable tkinter for the main function to use
                    rootc.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                    rootc.title("Decision Support Tool")  # Create overarching header for the interface
                    thelabelc = Label(rootc,
                                      text="Decision Support Tool- Base Tool")  # add subset header for the interface
                    thelabelc.pack()  # put GUI onto interface for usage
                    framec = Frame(rootc, width=500, height=500)  # frame user interface
                    framec.pack()  # put GUI onto interface for usage
                    bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage

                    lblc = Label(frame,
                                 text="What format do you prefer? [Database, Mapping, Interface Program, Other]  ")
                    lblc.grid(column=0, row=0)
                    lblc.pack()  # put GUI onto interface for usage
                    txtc = Entry(rootc, width=10)
                    txtc.pack()  # put GUI onto interface for usage

                    rbuttonc = Button(framec, text='Run Climate Tool', fg='black', bg='yellow')
                    rbuttonc.bind("<Button-1>", map)
                    rbuttonc.pack()  # put GUI onto interface for usage

                    rootc.mainloop()  # allow program to remain on user PC

        rootp = Tk()  # enable tkinter for the main function to use
        rootp.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
        rootp.title("Decision Support Tool")  # Create overarching header for the interface
        thelabelp = Label(rootp, text="Decision Support Tool- Base Tool")  # add subset header for the interface
        thelabelp.pack()  # put GUI onto interface for usage
        framep = Frame(rootp, width=500, height=500)  # frame user interface
        framep.pack()  # put GUI onto interface for usage
        bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage
        lblp = Label(framep, text="What format do you prefer? [Database, Mapping, Interface Program, Other]  ")
        lblp.grid(column=0, row=0)
        lblp.pack()  # put GUI onto interface for usage
        txtp = Entry(rootp, width=10)
        txtp.pack()  # put GUI onto interface for usage
        rbuttonp = Button(framep, text='Run Climate Tool', fg='black', bg='yellow')
        rbuttonp.bind("<Button-1>", form)
        rbuttonp.pack()  # put GUI onto interface for usage

        rootp.mainloop()  # allow program to remain on user PC
    else:  # Processing the user input as if/else statement
        print("Incorrect Value")
        exit()
        root.quit()  # close program from user PC


root = Tk()  # enable tkinter for the main function to use
root.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
root.title("Decision Support Tool")  # Create overarching header for the interface
thelabel = Label(root, text="Decision Support Tool- Base Tool")  # add subset header for the interface
thelabel.pack()  # put GUI onto interface for usage
frame = Frame(root, width=500, height=500)  # frame user interface
frame.pack()  # put GUI onto interface for usage
bottomframe = Frame(root)  # frame user interface
bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage

lbl = Label(frame, text="How would you like to start looking for tools? [by format, by scope]  ")
lbl.grid(column=0, row=0)
lbl.pack()  # put GUI onto interface for usage
txt = Entry(root, width=10)
txt.pack()  # put GUI onto interface for usage

rbutton = Button(frame, text='Run Base Tool', fg='black', bg='yellow')
rbutton.bind("<Button-1>", basetool)
rbutton.pack()  # put GUI onto interface for usage

root.mainloop()  # allow program to remain on user PC
