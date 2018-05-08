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
        simButton.place(x=layoutManager.leftMargin + 200,
                        y=layoutManager.controlFrameYCord + 20)

        pidLab = tk.Label(controlFrame,
                          text="PID parameters:")
        pidLab.place(x=layoutManager.leftMargin + 20,
                     y=layoutManager.controlFrameYCord + 20)

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


