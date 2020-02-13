import sys
import toolbox
import scheduler

"""

Used to return file containing mode scheduling.

Precedent order:
    1. Data downlink mode
    2. Imaging/Data Processing modes
    3. Cruise mode

"""
def SortAccess(accessFilename, outputFilename):
    accessFile = open(accessFilename,'r')
    line = True
    access = []
    while line:
        line = accessFile.readline()
        if line != '':
            access.append(line.split(','))

    sortedAccess = toolbox.Toolbox.SortAllAccess(access)
    outputFile = open(outputFilename,'w')
    for line in sortedAccess:
        for i in range (len(line)):
            if i != len(line) -1:
                line[i] += ","
            outputFile.write(line[i])
        
    accessFile.close()
    outputFile.close()

if __name__=='__main__':
    #uncomment when used with stk
    import stkengine
    targListName = "TargetList.csv"
    stkengine.CalculateAccess(targListName)

    
    SortAccess("Access.csv","SortedAccess.csv")
    access = scheduler.OpenAccess("SortedAccess.csv")
    actions = scheduler.Schedule(access)
    for item in actions:
        print(item)
    