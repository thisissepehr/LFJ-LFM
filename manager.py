from Machine import Machine
from Job import Task


class Manager:
    def __init__(self):
        self.machines = []
        self.tasks = []
        self.completed = []
        self.lastMachineID = 0
        self.lastTaskID = 0

    def addMachine(self):
        self.machines.append(Machine(self.lastMachineID))
        self.lastMachineID += 1

    def addTask(self, time, MIDs):
        self.tasks.append(Task(self.lastTaskID, time, MIDs))
        self.lastTaskID += 1
        self.__setValidityforMachines(MIDs)

    def __setValidityforMachines(self, MIDs):

        for i in self.machines:
            for j in MIDs:
                if (i.getID() == j):
                    i.addValidJob(self.lastTaskID - 1)
                    break

    def printMachines(self):
        for i in self.machines:
            print("Machine number: ", i.getID(), ", works on Tasks:", i.getValidJobs())

    def printTasks(self):
        for i in self.tasks:
            print("Task number: ", i.getID(), ", Can be processed on:", i.getValidMachines())

    def __sortMachinesByNumberOfJobs(self, AvailableMachines):
        sortedMachines = sorted(AvailableMachines, key=lambda x: len(x.getValidJobs()), reverse=False)
        return sortedMachines

    def __sortValidJobsByNumberOfMachines(self, jids):
        l1 = []
        for i in jids:
            l1.append(self.__findJobById(i))

        sortedJobs = sorted(l1, key=lambda x: len(x.getValidMachines()), reverse=False)
        l2 = []

        for i in sortedJobs:
            l2.append(i.getID())
        return l2

    def getAvailableMachines(self):
        res = []
        for i in self.machines:
            if not i.isBusy():
                res.append(i)
        return res

    def getNotAssignedJobs(self):
        j = []
        for i in self.tasks:
            if not i.isAssigned():
                j.append(i)
        return j

    def __setTask(self, mach, job):
        if (not job.isAssigned()):
            job.setAssigned()
            mach.goToWork(job.getID(), job.getTime())
            return True
        else:
            return False

    def __findMachinebyID(self, mid):
        for i in self.machines:
            if i.getID() == mid:
                return i
        return None

    def report(self):
        for i in self.machines:
            print("machine number: ", i.getID(), "worked on jobs number: ", i.getTasksDone(), "respectively")

    def __AssignTasks(self):
        sMachine = self.__sortMachinesByNumberOfJobs(self.getAvailableMachines())
        sMachine.append(Machine(-1))  # dummy
        while (len(sMachine) - 1 != 0):
            sjobs = self.__sortValidJobsByNumberOfMachines(self.__findMachinebyID(sMachine[0].getID()).getValidJobs())
            for i in sjobs:
                success = self.__setTask(self.__findMachinebyID(sMachine[0].getID()), self.__findJobById(i))
                if success:
                    break
            sMachine.pop(0)

    def calcCPM(self):
        paths = []
        for i in self.machines:
            l1 = i.getTasksDone()
            t = 0
            for j in l1:
                job = self.__findJobById(j)
                t += job.getTime()
            paths.append(t)

        return max(paths)

    def passTime(self, time):
        for i in range(time):
            if self.__isThereBusyMachine():
                for j in self.machines:
                    if (j.isBusy() and j.getTimeLeft() == 0):
                        jID = j.Free()
                        self.__findJobById(jID).Finished()
                        self.completed.append(self.__findJobById(jID))
                    else:
                        j.decTime()

                self.__AssignTasks()
            else:
                if len(self.getNotAssignedJobs()) == 0:
                    print("Finished All Tasks. Total Time is: ", self.calcCPM())
                    break
                else:
                    self.__AssignTasks()

    def __findJobById(self, jID):
        for i in self.tasks:
            if i.getID() == jID:
                return i
        return None

    def __isThereBusyMachine(self):
        for i in self.machines:
            if i.isBusy() == True:
                return True

        return False
