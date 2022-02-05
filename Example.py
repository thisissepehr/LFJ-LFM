from Manager import *

user = Manager()

# Insert number of machine
machine_num = 3

for i in range(machine_num):
    user.addMachine()

# Insert Job i   user.addTask(time, [list of Machine can proccess job i])
# Note: The number of machines and jobs is one less. Be careful when entering it.
user.addTask(5, [0, 2])
user.addTask(3, [1, 2])
user.addTask(7, [0, 1, 2])
user.addTask(6, [0, 1, 2])
user.addTask(3, [2])



user.printTasks()
print("\n")
user.printMachines()

user.passTime(6000)

print("\n")
print("Result is:")
user.report()
