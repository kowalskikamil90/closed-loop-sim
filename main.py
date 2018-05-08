from layoutManager import *
from controlSystem import *

if __name__ == "__main__":

    # Create laytout manager
    layoutMan = layoutManager()

    # Create main window, root for all widgets
    layoutMan.createWindow()

    # Create control frame for buttons and user entries
    layoutMan.createControlFrame()

    # Create scheme frame for system diagram
    layoutMan.createSchemeFrame()

    # Create plot frame for plot displaying
    layoutMan.createPlotFrame()

    # Initialize the Control system and it's required submodules
    PID = PIDcontroller()
    oscObj = OscObject()
    cntrlSys = ControlSystem(oscObj,
                             PID,
                             layoutMan,
                             layoutMan.PIDentries(),
                             layoutMan.OBJentries())

    # Set callback for button click
    layoutMan.simButton().config(command=cntrlSys.generateResponse)

    # Enter into infinite event loop
    layoutMan.master().mainloop()