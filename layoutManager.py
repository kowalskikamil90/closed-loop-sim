import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import sys

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
        self.__plotFrame = None
        self.__plot = None
        self.__plotCanvas = None

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

        self.__simButton = tk.Button(controlFrame,
                                text="SIMULATE",
                                fg="black",
                                bg="#63D84C",
                                width=24,
                                height=8)
        self.__simButton.place(x=layoutManager.leftMargin + 500,
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
        self.__OBJentries[labs[0]].insert(0, string=str(3.0))
        self.__OBJentries[labs[1]].insert(0, string=str(0.25))

    def createSchemeFrame(self):
        # This frame is used for holding
        # scheme widgets
        schemeFrame = tk.Frame(self.__master,
                               borderwidth=2,
                               width=layoutManager.frameWidth,
                               height=layoutManager.schemeFrameH,
                               relief="solid",
                               bg="#AE4D1D")
        schemeFrame.place(x=layoutManager.leftMargin,
                          y=layoutManager.schemeFrameYCord)

        canvas_width = layoutManager.frameWidth - 20
        canvas_height = layoutManager.schemeFrameH - 20

        paintingArea = tk.Canvas(schemeFrame,
                                 width=canvas_width,
                                 height=canvas_height,
                                 bg="#C49B86")

        self.paintTheScheme(paintingArea, canvas_width, canvas_height)

    def paintTheScheme(self, canvas, w, h):

        canvas.place(x=5,
                     y=5)

        # Paint feedback line and connections
        canvas.create_line(80,
                           80,
                           w - 80,
                           80,
                           fill="black",
                           width=3)
        canvas.create_line(w - 80,
                           80,
                           w - 80,
                           h - 80,
                           fill="black",
                           width=3)
        canvas.create_line(w - 80,
                           80,
                           w - 80,
                           h - 80,
                           fill="black",
                           width=3)
        canvas.create_line(w - 80,
                           h - 80,
                           80,
                           h - 80,
                           fill="black",
                           width=3)
        canvas.create_line(80,
                           h - 80,
                           80,
                           h - 170,
                           fill="black",
                           width=3)
        canvas.create_line(80,
                           h - 170,
                           180,
                           h - 170,
                           fill="black",
                           width=3)

        # Paint summator
        canvas.create_rectangle(170,
                                h - 210,
                                170 + 50,
                                h - 160,
                                fill="red")
        canvas.create_line(180,
                           h - 200,
                           190,
                           h - 200,
                           fill="black",
                           width=3)
        canvas.create_line(185,
                           h - 195,
                           185,
                           h - 205,
                           fill="black",
                           width=3)
        canvas.create_line(180,
                           h - 170,
                           190,
                           h - 170,
                           fill="black",
                           width=3)

        # Paint the PID Controller
        canvas.create_rectangle(330,
                                h - 225,
                                330 + 50,
                                h - 175,
                                fill="yellow")
        canvas.create_text(355,
                           h-200,
                           text="PID")

        # Paint the Object which is te subject of control system
        canvas.create_rectangle(500,
                                h - 225,
                                500 + 50,
                                h - 175,
                                fill="orange")
        canvas.create_text(525,
                           h-200,
                           text="OBJECT")

    def createPlotFrame(self):
        # This frame is used for holding
        # plot widgets
        self.__plotFrame = tk.Frame(self.__master,
                                    borderwidth=3,
                                    width=layoutManager.frameWidth,
                                    height=layoutManager.plotFrameH,
                                    relief="groove")
        self.__plotFrame.place(x=layoutManager.leftMargin,
                               y=layoutManager.plotFrameYCord)

        # Embeeding plot from matplotlib into tk canvas widget
        figure = Figure(figsize=(7.9, 2.9), dpi=100)
        self.__plot = figure.add_subplot(111)
        self.__plotCanvas = FigureCanvasTkAgg(figure , master=self.__master)
        self.__plotCanvas.draw()
        self.__plotCanvas._tkcanvas.place(x=layoutManager.leftMargin + 5,
                                          y=layoutManager.plotFrameYCord + 5)


    def updatePlot(self, result):

        self.__plot.plot(result[0], result[1])
        self.__plotCanvas.draw()


    def master(self):
        return self.__master

    def simButton(self):
        return self.__simButton

    def PIDentries(self):
        return self.__PIDentries

    def OBJentries(self):
        return self.__OBJentries

    def plotFrameReference(self):
        return self.__plotFrame
