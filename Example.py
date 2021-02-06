class Task:
    def __init__(self, id, time, MIDs):
        self.__Tid = id
        self.__processTime = time
        self.__validMachines = MIDs
        self.__Finished = False
        self.__Assigned = False

    def getID(self):
        return self.__Tid

    def isFinished(self):
        return self.__Finished

    def setAssigned(self):
        self.__Assigned = True

    def getValidMachines(self):
        return self.__validMachines

    def Finished(self):
        self.__Finished = True

    def isAssigned(self):
        return self.__Assigned

    def getTime(self):
        return self.__processTime
