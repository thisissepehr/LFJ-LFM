# This class is used in the manager file

class Machine:
    def __init__(self, id):
        self.__Mid = id
        self.__jobAssignedId = -1
        self.__validJobs = []
        self.timeLeft = 0
        self.__isBusy = False
        self.__tasksDone = []

    def getTimeLeft(self):
        return self.timeLeft

    def getID(self):
        return self.__Mid

    def isBusy(self):
        return self.__isBusy

    def goToWork(self, JID, time):
        self.__jobAssignedId = JID
        self.timeLeft = time
        self.__isBusy = True

    def Free(self):
        self.__isBusy = False
        self.timeLeft = 0
        jID = self.__jobAssignedId
        self.__tasksDone.append(jID)
        self.__jobAssignedId = -1
        return jID

    def getTasksDone(self):
        return self.__tasksDone

    def decTime(self):
        self.timeLeft -= 1

    def addValidJob(self, Jid):
        if (Jid not in self.__validJobs):
            self.__validJobs.append(Jid)

    def getValidJobs(self):
        return self.__validJobs
