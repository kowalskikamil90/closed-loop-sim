class PIDcontroller():

    def __init__(self):
        self.__P = None
        self.__I = None
        self.__D = None

    def setP(self, proportional):
        self.__P = proportional

    def setI(self, integrative):
        self.__I = integrative

    def setD(self, derivative):
        self.__D = derivative

    def getP(self):
        return self.__P

    def getI(self):
        return self.__I

    def getD(self):
        return self.__D

class OscObject():

    def __init__(self):
        self.omega0 = None
        self.dampingRatio = None

    def getOmega0(self):
        return self.omega0

    def getDampingRatio(self):
        return self.dampingRatio

    def setOmega0(self, w0):
        self.omega0 = w0

    def setDampingRatio(self, damping):
        self.dampingRatio = damping

class ControlSystem():

    def __init__(self, controlObject, controllerObject, viewReference, pidEntries, objEntries):
        self.__object = controlObject
        self.__controller = controllerObject
        self.__viewRef = viewReference
        self.__PIDentries = pidEntries
        self.__OBJentries = objEntries

    def generateResponse(self):
        print("GENERATE RESPONSE") #temporary, to check the callback execution
        # TODO: this is where the response will be calculated based
        # TODO: on known equation
        result = []
        self.__viewRef.updatePlot(result)

    def getController(self):
        return self.__controller

    def getObject(self):
        return self.__object

    def setController(self, controllerObject):
        self.__controller = controllerObject

    def setObject(self, controlObject):
        self.__object = controlObject