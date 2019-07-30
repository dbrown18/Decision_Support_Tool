# Import Tkinter GUIs & web browser access

from tkinter import *
import webbrowser


# create an overall function for GUI interface to interact with
def fishloop(event):
    rentry = txt.get()  # retrieve the response from the user from input window
    while rentry:  # beginning the loop so that interface can process user response
        if rentry in ["local", "Local"]:  # Processing the user input as if/else statement
            root.destroy()  # remove the original interface from the screen

            def locloop(event):  # subfunction for user choosing local
                rentry2 = txt2.get()  # retrieve the response from the user from input window

                if rentry2 in ["PA", "pa"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="Pennsylvania Natural Heritage Program: Use this link- "
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):  # subfunction for opening the right website
                        webbrowser.open('http://www.gis.dcnr.state.pa.us/maps/index.html?acc=true')
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
                    Label(rootf, text="US Bathymetry and Fishing Maps: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open('"https://maps.ngdc.noaa.gov/viewers/fishmaps/"')
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                else:  # Processing the user input as if/else statement
                    pass

            root2 = Tk()  # enable tkinter for the main function to use
            root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            root2.title("Decision Support Tool")  # Create overarching header for the interface
            thelabel2 = Label(root2, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
            thelabel2.pack()  # put GUI onto interface for usage
            frame2 = Frame(root2, width=500, height=500)  # frame user interface
            frame2.pack()  # put GUI onto interface for usage
            bottomframe2 = Frame(root2)  # frame user interface
            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
            lbl2 = Label(frame2, text="Which Jurisdiction is your location in? [PA, Other] ")
            lbl2.pack()  # put GUI onto interface for usage
            txt2 = Entry(root2, width=10)
            txt2.pack()  # put GUI onto interface for usage
            rbutton2 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
            rbutton2.bind("<Button-1>", locloop)
            rbutton2.pack()  # put GUI onto interface for usage
            root2.mainloop()  # allow program to remain on user PC

        elif rentry in ["Jurisdiction", "jurisdiction"]:  # Processing the user input as if/else statement
            root.destroy()  # remove the original interface from the screen

            def locloop(event):
                rentry2 = txt2.get()  # retrieve the response from the user from input window

                if rentry2 in ["MD", "md", "VA", "va"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="Fresh Water Network Aquatic Barrier Prioritization: Use link- "
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://maps.freshwaternetwork.org/chesapeake/")
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                elif rentry2 in ["PA", "pa"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen

                    def thrloop(event):
                        rentry3 = txt3.get()  # retrieve the response from the user from input window

                        if rentry3 in ["Aquatic Biodiversity", "aquatic biodiversity"]:  # Processing the user input
                            # as if/else statement
                            root3.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="Pennsylvania Natural Heritage Program: Use this link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("http://www.gis.dcnr.state.pa.us/maps/index.html?acc=true")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        elif rentry3 in ["Habitat Conservation", "habitat conservation"]:  # Processing the user input
                            # as if/else statement
                            root3.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="Fresh Water Network Aquatic Barrier Prioritization: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlink(event):
                                webbrowser.open("https://maps.freshwaternetwork.org/chesapeake/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootf, text='click here', fg="black", bg='red')
                            buttonf.bind("<Button-1>", openlink)
                            buttonf.pack()  # put GUI onto interface for usage
                        else:  # Processing the user input as if/else statement
                            pass

                    root3 = Tk()  # enable tkinter for the main function to use
                    root3.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                    root3.title("Decision Support Tool")  # Create overarching header for the interface
                    thelabel2 = Label(root3, text="Decision Support Tool- Fish Habitat")  # add subset header for the
                    # interface
                    thelabel2.pack()  # put GUI onto interface for usage
                    frame3 = Frame(root3, width=500, height=500)  # frame user interface
                    frame3.pack()  # put GUI onto interface for usage
                    bottomframe2 = Frame(root3)  # frame user interface
                    bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
                    lbl2 = Label(frame3,
                                 text="What problem are you addressing?[Aquatic Biodiversity, Habitat Conservation] ")
                    lbl2.pack()  # put GUI onto interface for usage
                    txt3 = Entry(root3, width=10)
                    txt3.pack()  # put GUI onto interface for usage
                    rbutton2 = Button(frame3, text='Run Fish Loop', fg='black', bg='yellow')
                    rbutton2.bind("<Button-1>", thrloop)
                    rbutton2.pack()  # put GUI onto interface for usage
                    root3.mainloop()  # allow program to remain on user PC
                elif rentry2 in ["Other", "other"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="US Bathymetry and Fishing Maps: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://maps.ngdc.noaa.gov/viewers/fishmaps/")
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                else:  # Processing the user input as if/else statement
                    pass

            root2 = Tk()  # enable tkinter for the main function to use
            root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            root2.title("Decision Support Tool")  # Create overarching header for the interface
            thelabel2 = Label(root2, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
            thelabel2.pack()  # put GUI onto interface for usage
            frame2 = Frame(root2, width=500, height=500)  # frame user interface
            frame2.pack()  # put GUI onto interface for usage
            bottomframe2 = Frame(root2)  # frame user interface
            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
            lbl2 = Label(frame2, text="Which Jurisdiction are you looking at? [MD, PA, VA, Other] ")
            lbl2.pack()  # put GUI onto interface for usage
            txt2 = Entry(root2, width=10)
            txt2.pack()   # put GUI onto interface for usage
            rbutton2 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
            rbutton2.bind("<Button-1>", locloop)
            rbutton2.pack()  # put GUI onto interface for usage
            root2.mainloop()  # allow program to remain on user PC
        elif rentry in ["Regional", "regional"]:  # Processing the user input as if/else statement
            root.destroy()  # remove the original interface from the screen

            def locloop(event):
                rentry2 = txt2.get()  # retrieve the response from the user from input window
                if rentry2 in ["no", "No"]:  # Processing the user input as if/else statement
                    root2.destroy() # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="US Bathymetry and Fishing Maps: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage
                    Label(rootf, text="Fresh Water Network Aquatic Barrier Prioritization: Use link- "
                          , fg="light blue",
                          bg="dark blue",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage
                    Label(rootf, text="Essential Fish Habitat Conservation: Use link-"
                          , fg="gold4",
                          bg="gold",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://maps.ngdc.noaa.gov/viewers/fishmaps/")
                        webbrowser.open("https://maps.freshwaternetwork.org/chesapeake/")
                        webbrowser.open("https://www.habitat.noaa.gov/protection/efh/efhmapper/index.html")
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='IndianRed2')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage

                elif rentry2 in ["yes", "Yes"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen

                    def thrloop(event):
                        rentry3 = txt3.get()  # retrieve the response from the user from input window
                        if rentry3 in ["Striped Bass", "striped bass", "sturgeons", "Sturgeons"]:  # Processing the user
                            # input as if/else statement
                            root3.destroy()  # remove the original interface from the screen
                            rootf = Tk()  # enable tkinter for the main function to use
                            rootf.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframef = Frame(rootf)  # frame user interface
                            bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootf, text="Fresh Water Network Aquatic Barrier Prioritization: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlinkt(event):
                                webbrowser.open("https://maps.freshwaternetwork.org/chesapeake/")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonfhh = Button(rootf, text='click here', fg="black", bg='green')
                            buttonfhh.bind("<Button-1>", openlinkt)
                            buttonfhh.pack()  # put GUI onto interface for usage
                        elif rentry3 in ["Trout", "trout"]:  # Processing the user input as if/else statement
                            root3.destroy()  # remove the original interface from the screen
                            rootfhh = Tk()  # enable tkinter for the main function to use
                            rootfhh.title("Decision Support Tool")  # Create overarching header for the interface
                            bottomframefhh = Frame(rootfhh)  # frame user interface
                            bottomframefhh.pack(side=BOTTOM)  # put GUI onto interface for usage
                            Label(rootfhh, text="Brook Trout Integrated Spatial Data Tools: Use link- "
                                  , fg="light green",
                                  bg="dark green",
                                  font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                            def openlinku(event):
                                webbrowser.open("http://ecosheds.org:8080/geoserver/www/Web_Map_Viewer.html")
                                rootf.destroy()  # remove the original interface from the screen

                            buttonf = Button(rootfhh, text='click here', fg="black", bg='green')
                            buttonf.bind("<Button-1>", openlinku)
                            buttonf.pack()  # put GUI onto interface for usage
                        else:  # Processing the user input as if/else statement
                            pass

                    root3 = Tk()  # enable tkinter for the main function to use
                    root3.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
                    root3.title("Decision Support Tool")  # Create overarching header for the interface
                    thelabel2h = Label(root3, text="Decision Support Tool- Fish Habitat")  # add subset header for the
                    # interface
                    thelabel2h.pack()  # put GUI onto interface for usage
                    frame3 = Frame(root3, width=500, height=500)  # frame user interface
                    frame3.pack()  # put GUI onto interface for usage
                    bottomframe2h = Frame(root3)  # frame user interface
                    bottomframe2h.pack(side=BOTTOM)  # put GUI onto interface for usage
                    lbl2h = Label(frame3,
                                  text="What type of fish? [Striped Bass, Sturgeons, Trout] ")
                    lbl2h.pack()  # put GUI onto interface for usage
                    txt3 = Entry(root3, width=10)
                    txt3.pack()  # put GUI onto interface for usage
                    rbutton2h = Button(frame3, text='Run Fish Loop', fg='black', bg='yellow')
                    rbutton2h.bind("<Button-1>", thrloop)
                    rbutton2h.pack()  # put GUI onto interface for usage
                    root3.mainloop()  # allow program to remain on user PC

            root2 = Tk()  # enable tkinter for the main function to use
            root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            root2.title("Decision Support Tool")  # Create overarching header for the interface
            thelabel2 = Label(root2, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
            thelabel2.pack()  # put GUI onto interface for usage
            frame2 = Frame(root2, width=500, height=500)  # frame user interface
            frame2.pack()  # put GUI onto interface for usage
            bottomframe2 = Frame(root2)  # frame user interface
            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
            lbl2 = Label(frame2, text="Is there a specific fish you are looking at? [No, Yes] ")
            lbl2.pack()  # put GUI onto interface for usage
            txt2 = Entry(root2, width=10)
            txt2.pack()  # put GUI onto interface for usage
            rbutton2 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
            rbutton2.bind("<Button-1>", locloop)
            rbutton2.pack()  # put GUI onto interface for usage
            root2.mainloop()  # allow program to remain on user PC
        elif rentry in ["National", "national"]:  # Processing the user input as if/else statement
            root.destroy()  # remove the original interface from the screen

            def locloop(event):
                rentry2 = txt2.get()  # retrieve the response from the user from input window
                if rentry2 in ["Bathymetry", "bathymetry"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootf = Tk()  # enable tkinter for the main function to use
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="US Bathymetry and Fishing Maps: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://maps.ngdc.noaa.gov/viewers/fishmaps/")
                        rootf.destroy()  # remove the original interface from the screen
                        buttonf = Button(rootf, text='click here', fg="black", bg='green')
                        buttonf.bind("<Button-1>", openlink)
                        buttonf.pack()  # put GUI onto interface for usage
                elif rentry2 in ["Habitat Conservation", "habitat conservation"]:  # Processing the user input as
                    # if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootf = Tk()
                    rootf.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootf)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootf, text="Essential Fish Habitat Conservation: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlink(event):
                        webbrowser.open("https://www.habitat.noaa.gov/protection/efh/efhmapper/index.html")
                        rootf.destroy()  # remove the original interface from the screen

                    buttonf = Button(rootf, text='click here', fg="black", bg='green')
                    buttonf.bind("<Button-1>", openlink)
                    buttonf.pack()  # put GUI onto interface for usage
                elif rentry2 in ["general", "General"]:  # Processing the user input as if/else statement
                    root2.destroy()  # remove the original interface from the screen
                    rootl = Tk()
                    rootl.title("Decision Support Tool")  # Create overarching header for the interface
                    bottomframef = Frame(rootl)  # frame user interface
                    bottomframef.pack(side=BOTTOM)  # put GUI onto interface for usage
                    Label(rootl, text="USGS Ecosystems Mapping: Use link-"
                          , fg="light green",
                          bg="dark green",
                          font="Helvetica 16 bold italic").pack()  # put GUI onto interface for usage

                    def openlinkl(event):
                        webbrowser.open(
                            "https://www.usgs.gov/mission-areas/ecosystems?qt-mission_areas_l2_landing_page_ta=3#qt"
                            "-mission_areas_l2_landing_page_ta")

                    buttonf = Button(rootl, text='click here', fg="black", bg='red')
                    buttonf.bind("<Button-1>", openlinkl)
                    buttonf.pack()  # put GUI onto interface for usage
                else:  # Processing the user input as if/else statement
                    pass

            root2 = Tk()  # enable tkinter for the main function to use
            root2.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
            root2.title("Decision Support Tool")  # Create overarching header for the interface
            thelabel2 = Label(root2, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
            thelabel2.pack()  # put GUI onto interface for usage
            frame2 = Frame(root2, width=500, height=500)  # frame user interface
            frame2.pack()  # put GUI onto interface for usage
            bottomframe2 = Frame(root2)  # frame user interface
            bottomframe2.pack(side=BOTTOM)  # put GUI onto interface for usage
            lbl2 = Label(frame2, text="What problem are you addressing? [Bathymetry, Habitat Conservation, General] ")
            lbl2.pack()  # put GUI onto interface for usage
            txt2 = Entry(root2, width=10)
            txt2.pack()  # put GUI onto interface for usage
            rbutton2 = Button(frame2, text='Run Fish Loop', fg='black', bg='yellow')
            rbutton2.bind("<Button-1>", locloop)
            rbutton2.pack()  # put GUI onto interface for usage
            root2.mainloop()  # allow program to remain on user PC
        else:  # Processing the user input as if/else statement
            print("Incorrect Value")
            exit()
            root.quit()  # close program from user PC


root = Tk()  # enable tkinter for the main function to use
root.geometry('500x500+500+300')  # Assign dimensions of the interface for the user
root.title("Decision Support Tool")  # Create overarching header for the interface
thelabel = Label(root, text="Decision Support Tool- Fish Habitat")  # add subset header for the interface
thelabel.pack()  # put GUI onto interface for usage
frame = Frame(root, width=500, height=500)  # frame user interface
frame.pack()  # put GUI onto interface for usage
bottomframe = Frame(root)  # frame user interface
bottomframe.pack(side=BOTTOM)  # put GUI onto interface for usage

lbl = Label(frame, text="What is the scope of your project? [Local, Jurisdiction, Regional, National] ")
lbl.grid(column=0, row=0)
lbl.pack()  # put GUI onto interface for usage
txt = Entry(root, width=10)
txt.pack()  # put GUI onto interface for usage

rbutton = Button(frame, text='Run Fish Loop', fg='black', bg='yellow')
rbutton.bind("<Button-1>", fishloop)
rbutton.pack()  # put GUI onto interface for usage

root.mainloop()  # allow program to remain on user PC
