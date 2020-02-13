import scheduler
import parse


if __name__=='__main__':
    answer = input("Are you running a new STK simulation (y/n)? ")
    if (answer == "y"):
        import stkengine
        answer = input("How long do you want to run the simulation for (ex. '+24hrs')? ")
        targListName = "TargetList.csv"
        stkengine.CalculateAccess(targListName,answer)
        filename = "Access.csv"
        
    else:
        filename = input("What is the name of the access file? ")
    
    parse.SortAccess(filename,"SortedAccess.csv")
    access = scheduler.OpenAccess("SortedAccess.csv")
    actions = scheduler.Schedule(access)
    for item in actions:
        print(item)
    