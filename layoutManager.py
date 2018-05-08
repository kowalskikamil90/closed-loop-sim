import tkinter as tk

class layoutManager():
    # Height of all frame widgets
    controlFrameH = 200
    schemeFrameH = 300
    plotFrameH = 300

    # Spacing between frames and margins
    leftMargin = 20
    rightMargin = 20
    verticalSpacing = 10

    # Width for all frames
    frameWidth = 800

    # Vertical coordinates of frames
    controlFrameYCord = 0 + verticalSpacing
    schemeFrameYCord = controlFrameYCord + controlFrameH + verticalSpacing
    plotFrameYCord = schemeFrameYCord + schemeFrameH + verticalSpacing

    # Size of entire window
    winWidth = leftMargin + frameWidth + rightMargin
    winHeight = plotFrameYCord + plotFrameH + verticalSpacing

    def __init__(self):
        self.__master = None
        self.__simButton = None
        self.__PIDentries = {}
        self.__OBJentries = {}

    def createWindow(self):
        # Create master widget, the window.
        # This is a root widget, for all
        # other widgets.
        self.__master = tk.Tk()
        self.__master.title('Closed loop simulator with PID controller')
        # Size needs to be passed as a string e.g. "500x500"
        sizeString = str(layoutManager.winWidth) + "x" + str(layoutManager.winHeight)
        self.__master.geometry(sizeString)
        # Don't allow resizing of a window
        self.__master.resizable(0, 0)

    def createControlFrame(self):

        # This frame is used for holding
        # control widgets
        controlFrame = tk.Frame(self.__master,
                                borderwidth=3,
                                width=layoutManager.frameWidth,
                                height=layoutManager.controlFrameH,
                                relief="groove")
        controlFrame.place(x=layoutManager.leftMargin,
                           y=layoutManager.controlFrameYCord)

        simButton = tk.Button(controlFrame,
                              text="SIMULATE",
                              fg="black",
                              bg="#63D84C",
                              width=24,
                              height=8,
                              command=quit)
        simButton.place(x=layoutManager.leftMargin + 500,
                        y=layoutManager.controlFrameYCord + 20)

        # PID parameters panel
        pidLab = tk.Label(controlFrame,
                          text="PID parameters:",
                          font=("Arial", 13))
        pidLab.place(x=layoutManager.leftMargin + 20,
                     y=layoutManager.controlFrameYCord + 20)

        labs = ["Proportional:", "Integrative:", "Derivative:"]
        bias = 0;
        entryLength = 80

        for lab in labs:
            label = tk.Label(controlFrame,
                             text=lab,
                             font=("Arial", 10))
            label.place(x=layoutManager.leftMargin + 20,
                        y=layoutManager.controlFrameYCord + 45 + bias)
            entry = tk.Entry(controlFrame, justify='center')
            entry.place(x=layoutManager.leftMargin + 100,
                        y=layoutManager.controlFrameYCord + 45 + bias,
                        width=entryLength)
            bias += 25
            self.__PIDentries[lab] = entry

        # Set default values
        self.__PIDentries[labs[0]].insert(0, string=str(1.0))
        self.__PIDentries[labs[1]].insert(0, string=str(0.5))
        self.__PIDentries[labs[2]].insert(0, string=str(0.2))

        # Oscillatory object parameters panel
        objLab = tk.Label(controlFrame,
                          text="Oscillatory object parameters:",
                          font=("Arial", 13))
        objLab.place(x=layoutManager.leftMargin + 250,
                     y=layoutManager.controlFrameYCord + 20)

        labs = ["Angular frequency(Wo):", "Damping ratio(dzeta):"]
        bias = 0;

        for lab in labs:
            label = tk.Label(controlFrame,
                             text=lab,
                             font=("Arial", 10))
            label.place(x=layoutManager.leftMargin + 250,
                        y=layoutManager.controlFrameYCord + 45 + bias)
            entry = tk.Entry(controlFrame, justify='center')
            entry.place(x=layoutManager.leftMargin + 390,
                        y=layoutManager.controlFrameYCord + 45 + bias,
                        width=entryLength)
            bias += 25
            self.__OBJentries[lab] = entry

        # Set default values
        self.__OBJentries[labs[0]].insert(0, string=str(1.0))
        self.__OBJentries[labs[1]].insert(0, string=str(0.5))

    def createSchemeFrame(self):
        # This frame is used for holding
        # scheme widgets
        schemeFrame = tk.Frame(self.__master,
                               borderwidth=3,
                               width=layoutManager.frameWidth,
                               height=layoutManager.schemeFrameH,
                               relief="solid",
                               bg="#63D84C")
        schemeFrame.place(x=layoutManager.leftMargin,
                          y=layoutManager.schemeFrameYCord)

        canvas_width = layoutManager.frameWidth - 20
        canvas_height = layoutManager.schemeFrameH - 20
        paintingArea = tk.Canvas(schemeFrame,
                                 width=canvas_width,
                                 height=canvas_height,
                                 bg="#476042")
        paintingArea.place(x=5,
                           y=5)

    def createPlotFrame(self):
        # This frame is used for holding
        # plot widgets
        plotFrame = tk.Frame(self.__master,
                             borderwidth=3,
                             width=layoutManager.frameWidth,
                             height=layoutManager.plotFrameH,
                             relief="groove")
        plotFrame.place(x=layoutManager.leftMargin,
                        y=layoutManager.plotFrameYCord)

    def master(self):
        return self.__master

    def PIDentries(self):
        return self.__PIDentries

    def OBJentries(self):
        return self.__OBJentries
