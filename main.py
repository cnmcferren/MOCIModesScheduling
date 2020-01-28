import sys

"""

Used to return file containing mode scheduling.

Precedent order:
    1. Data downlink mode
    2. Imaging/Data Processing modes
    3. Cruise mode

Flags:
    --stk: Run STK sim to calculate access file given a target list
    --file: Skip STK sim and run using provided access file

"""

if __name__=='__main__':
    #Executed if new STK simulation needs to be run
    if "--stk" in sys.argv:
        import stkengine
        targListName = sys.argv[sys.argv.index("--stk") + 1]
        stkengine.CalculateAccess(targListName)
        
    #Executed if access file is already provided
    elif "--file" in sys.argv:
        
    else:
        print("Error: please enter valid flags.")