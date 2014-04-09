import sys
import copy
import random

#you can edit this task list to contain the actual tasks you have. Just keep the format.
#("name of task",num of minutes task takes)
tasks=[("math hwk",120),("project proposal",5),("make lunch",45),("os",120)]
taskNames = ""

for task in tasks:
	if len(taskNames)==0:
		taskNames+=task[0]
	else:
		taskNames += ", " + task[0]

#this is in case you want to add tasks after the program has started.
#It's clunky and inconvenient, so I recommend just editing the list directly above.
print "Currently you have the following tasks: " + taskNames
var = raw_input("Would you like to add more tasks? y/n: ")
while (var == "y"):
	task = raw_input("Type in task name: ")
	time = int(raw_input("Type in time in minutes: "))
	tasks += (task,time)
	var=raw_input("Would you like to add more tasks? y/n: ")

time = 60*int(raw_input("How much time in hours do you have to work right now? Round to the nearest hour:  "))
t=time/60
tasksCopy = copy.deepcopy(tasks)
toDo=""
num = 0
while time > 0 and num<2*len(tasks) and len(tasksCopy)>0:
	if len(tasksCopy)==1:
		i=0
	else:
		i = random.randint(0,len(tasksCopy)-1)
	if tasksCopy[i][1] < time:
		toDo += str(tasksCopy[i]) + " "
		time -= tasksCopy[i][1]
		del tasksCopy[i]
		num = 0
	else:
		num+=1
print
print "For the next " + str(t) + " hours, work on: "
print toDo
