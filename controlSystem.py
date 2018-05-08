from math import *

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
        # Fetch object parameters from the entry forms
        labs = ["Angular frequency(Wo):", "Damping ratio(dzeta):"]
        self.__object.setOmega0(float(self.__OBJentries[labs[0]].get()))
        self.__object.setDampingRatio(float(self.__OBJentries[labs[1]].get()))

        # Fetch PID parameters from the entry forms
        labs = ["Proportional:", "Integrative:", "Derivative:"]
        self.__controller.setP(float(self.__PIDentries[labs[0]].get()))
        self.__controller.setI(float(self.__PIDentries[labs[1]].get()))
        self.__controller.setD(float(self.__PIDentries[labs[2]].get()))

        resultVec = self.calculateResultList()

        self.__viewRef.updatePlot(resultVec)

    def calculateResultList(self):

        # Object parameters
        omega0 = self.__object.getOmega0()
        dzeta = self.__object.getDampingRatio()

        # PID controller parameteres
        P = self.__controller.getP()
        I = self.__controller.getI()
        D = self.__controller.getD()

        # Sampling interval and lists
        sampling = 50 #50 ms
        simulationTime = 10000 #10 seconds
        samplingList = range(0, simulationTime + sampling, sampling)
        samplingListFloat = [x * 0.001 for x in samplingList]

        # This should be equation for closed-loop control system but
        # it is only second-order oscilator object alone..
        # Couldn't find the exact equation for the closed-loop system :)
        # It basically means that the PID parameters don't matter and
        # they doesn't influence the response.

        def calculateValueForSpecificTime(t, w0, dz):
            el1 = 1.0/(sqrt(1-pow(dz, 2)))
            el2 = exp(-1.0*dz*w0*t)
            intermediateVal1 = sqrt(1.0-pow(dz, 2))*w0*t
            intermediateVal2 = acos(dz)
            el3 = sin(intermediateVal1 + intermediateVal2)
            return 1 - el1*el2*el3

        # Prepare empty list for result
        result = []

        for t in samplingListFloat:
            result.append(calculateValueForSpecificTime(t, omega0, dzeta))

        return [samplingListFloat, result]


    def getController(self):
        return self.__controller

    def getObject(self):
        return self.__object

    def setController(self, controllerObject):
        self.__controller = controllerObject

    def setObject(self, controlObject):
        self.__object = controlObject