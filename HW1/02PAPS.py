'''
Gantt Chart Setting
'''
# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt
from math import gcd

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# Setting Y-axis limits
gnt.set_ylim(0, 55)

# Setting X-axis limits
gnt.set_xlim(0, 60)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('time since start')
gnt.set_ylabel('process')

# Setting ticks on y-axis
gnt.set_yticks([5, 13, 18, 23, 28, 33, 38, 43, 48])
# Labelling tickes of y-axis
gnt.set_yticklabels(['ALL', 'τ1', 'τ2', 'τ3', 'τ4', 'τ5', 'AP1', 'AP2', 'AP3'])

# Setting graph attribute
gnt.grid(True)

'''
Polling Server AperiodicProcess Scheduling
'''
print('Polling Server APS Average Delay Calculating Program Start! \n')
# Hyper Parameter Input (Periodic Task)
print('Please input Periodic task1')
t1ComputeTime, t1Period = map(int, input(
    'Periodic task1 computation time, period : ').split())
t1RemainTask = 0

print('Please input Periodic task2')
t2ComputeTime, t2Period = map(int, input(
    'Periodic task2 computation time, period : ').split())
t2RemainTask = 0

print('Please input Periodic task3')
t3ComputeTime, t3Period = map(int, input(
    'Periodic task3 computation time, period : ').split())
t3RemainTask = 0

print('Please input Periodic task4')
t4ComputeTime, t4Period = map(int, input(
    'Periodic task4 computation time, period : ').split())
t4RemainTask = 0

print('Please input Periodic task5')
t5ComputeTime, t5Period = map(int, input(
    'Periodic task5 computation time, period : ').split())
t5RemainTask = 0

# Hyper Parameter Input (Aperiodic Task)
print('\nPlease input Aperiodic task1')
AP1ComputeTime, AP1ArrivalTime = map(int, input(
    'Aperiodic task1 computation time, arrival time : ').split())
AP1RemainTask = 0

print('Please input Aperiodic task2')
AP2ComputeTime, AP2ArrivalTime = map(int, input(
    'Aperiodic task2 computation time, arrival time : ').split())
AP2RemainTask = 0

print('Please input Aperiodic task3')
AP3ComputeTime, AP3ArrivalTime = map(int, input(
    'Aperiodic task3 computation time, arrival time : ').split())
AP3RemainTask = 0

print('Please input Polling server task')
PollingCapacity, PollingPeriod = map(int, input(
    'Polling capacity, period : ').split())

# Hyper Period Calculating
PeriodList = [t1Period, t2Period, t3Period, t4Period, t5Period]
lcm = t1Period
for i in PeriodList[1:]:
    lcm = int(lcm*i / gcd(lcm, i))

HyperPeriod = lcm

taskList = [0 for i in range(HyperPeriod)]
print("\nPeriodic task's Hyper Period :", HyperPeriod)

# Proccess Execution
for i in range(0, HyperPeriod):

    # Aperiodic Task Arrival
    if (i == AP1ArrivalTime):
        AP1RemainTask += AP1ComputeTime

    if (i == AP2ArrivalTime):
        AP2RemainTask += AP2ComputeTime

    if (i == AP3ArrivalTime):
        AP3RemainTask += AP3ComputeTime

    # Periodic Task Arrival
    if (i % t1Period == 0):
        t1RemainTask += t1ComputeTime

    if (i % t2Period == 0):
        t2RemainTask += t2ComputeTime

    if (i % t3Period == 0):
        t3RemainTask += t3ComputeTime

    if (i % t4Period == 0):
        t4RemainTask += t4ComputeTime

    if (i % t5Period == 0):
        t5RemainTask += t5ComputeTime

    # Aperiodic Task Execution
    if (i % PollingPeriod == 0):
        for j in range(0, PollingCapacity):
            if (AP1RemainTask == 0 and AP2RemainTask == 0 and AP3RemainTask == 0):
                break
            if (AP1RemainTask > 0):
                if(taskList[i] == 0):
                    taskList[i] = 'ap1'
                    gnt.broken_barh([(i, 1)], (4, 2), facecolors=('crimson'))
                    gnt.broken_barh([(i, 1)], (37, 2), facecolors=('crimson'))
                    AP1RemainTask -= 1

            if (AP2RemainTask > 0):
                if(taskList[i] == 0):
                    taskList[i] = 'ap2'
                    gnt.broken_barh([(i, 1)], (4, 2), facecolors=('pink'))
                    gnt.broken_barh([(i, 1)], (42, 2), facecolors=('pink'))
                    AP2RemainTask -= 1

            if (AP3RemainTask > 0):
                if(taskList[i] == 0):
                    taskList[i] = 'ap3'
                    gnt.broken_barh([(i, 1)], (4, 2), facecolors=('orange'))
                    gnt.broken_barh([(i, 1)], (47, 2), facecolors=('orange'))
                    AP3RemainTask -= 1
            i += 1

    # Periodic Task Execution
    if (t1RemainTask > 0):
        if(taskList[i] == 0):
            taskList[i] = 't1'
            gnt.broken_barh([(i, 1)], (4, 2), facecolors=('gold'))
            gnt.broken_barh([(i, 1)], (12, 2), facecolors=('gold'))
            t1RemainTask -= 1

    if (t2RemainTask > 0):
        if(taskList[i] == 0):
            taskList[i] = 't2'
            gnt.broken_barh([(i, 1)], (4, 2), facecolors=('green'))
            gnt.broken_barh([(i, 1)], (17, 2), facecolors=('green'))
            t2RemainTask -= 1

    if (t3RemainTask > 0):
        if(taskList[i] == 0):
            taskList[i] = 't3'
            gnt.broken_barh([(i, 1)], (4, 2), facecolors=('lightgreen'))
            gnt.broken_barh([(i, 1)], (22, 2), facecolors=('lightgreen'))
            t3RemainTask -= 1

    if (t4RemainTask > 0):
        if(taskList[i] == 0):
            taskList[i] = 't4'
            gnt.broken_barh([(i, 1)], (4, 2), facecolors=('lightblue'))
            gnt.broken_barh([(i, 1)], (27, 2), facecolors=('lightblue'))
            t4RemainTask -= 1

    if (t5RemainTask > 0):
        if(taskList[i] == 0):
            taskList[i] = 't5'
            gnt.broken_barh([(i, 1)], (4, 2), facecolors=('blue'))
            gnt.broken_barh([(i, 1)], (32, 2), facecolors=('blue'))
            t5RemainTask -= 1

# Average Delay Time Calculating
AP1CompleteTime = 0
AP2CompleteTime = 0
AP3CompleteTime = 0
for i in range(0, HyperPeriod):
    if (taskList[i] == 'ap1'):
        AP1CompleteTime = i
    if (taskList[i] == 'ap2'):
        AP2CompleteTime = i
    if (taskList[i] == 'ap3'):
        AP3CompleteTime = i
AP1DelayTime = AP1CompleteTime - AP1ArrivalTime
AP2DelayTime = AP2CompleteTime - AP2ArrivalTime
AP3DelayTime = AP3CompleteTime - AP3ArrivalTime

APSaverageDelayTime = (AP1DelayTime + AP2DelayTime + AP3DelayTime) / 3

print("\n----Polling Server APS Result----")

print("AP1 Complete Time : ", AP1CompleteTime)
print("AP2 Complete Time : ", AP2CompleteTime)
print("AP3 Complete Time : ", AP3CompleteTime)

print("\nAP1 Delay Time : ", AP1DelayTime)
print("AP2 Delay Time : ", AP2DelayTime)
print("AP3 Delay Time : ", AP3DelayTime)

print("\nAperiodic Proccess Scheduling Average Delay Time : ", APSaverageDelayTime)

'''
Result Saving to img(png)
'''
plt.savefig("PollingServerAPS.png")
