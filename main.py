import tkinter as tk

if __name__ == "__main__":
    # Create master widget, the window.
    # This is a root widget, for all
    # other widgets.
    master = tk.Tk()

    # This frame is used for holding
    # control widgets
    controlFrame = tk.Frame(master,
                            borderwidth=3,
                            relief="groove")
    controlFrame.pack(fill=tk.X)

    simButton = tk.Button(controlFrame,
                          text="SIMULATE",
                          fg="black",
                          bg="green",
                          width=14,
                          height=4,
                          command=quit
                          )
    simButton.pack()

    # This frame is used for holding
    # scheme widgets
    schemeFrame = tk.Frame(master,
                           borderwidth=3,
                           relief="groove")
    schemeFrame.pack(fill=tk.X)

    canvas_width = 800
    canvas_height = 400
    paintingArea = tk.Canvas(schemeFrame,
               width=canvas_width,
               height=canvas_height)
    paintingArea.pack()

    # This frame is used for holding
    # plot widgets
    plotFrame = tk.Frame(master,
                         borderwidth=3,
                         relief="groove")
    plotFrame.pack(fill=tk.X)

    label = tk.Label(plotFrame, text="PLOTTING AREA")
    label.pack()

    # Enter into infinite event loop
    master.mainloop()