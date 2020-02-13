import toolbox
import scheduler

"""

Sorts the access provided from STK and saves it to a separate file.

Parameters:
    accessFilename(str): Name of access file to be parsed
    outputFilename(str): Name of the file to store the sorted access

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
    