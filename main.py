from layoutManager import *

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

    # Enter into infinite event loop
    layoutMan.master().mainloop()