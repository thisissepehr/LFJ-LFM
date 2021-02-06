from manager import *

user = Manager()

user.addMachine()
user.addMachine()
user.addMachine()

user.addTask(1, [0, 1, 2])
user.addTask(1, [0, 1])
user.addTask(1, [2])
user.addTask(1, [0, 1, 2])
user.addTask(1, [1])

user.printTasks()
user.printMachines()

user.passTime(13)
user.report()
