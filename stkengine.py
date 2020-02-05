import parse
from stkhelper import application, scenario, satellite, areatarget


"""

Runs an STK scenario to calculate the access times given a certain target
list that is provided and the Athens Ground Station

Parameters:
    filename(str): The target list to be used
    
Returns:
    0 (int): Successful execution
    1 (int): Failed execution

"""
def CalculateAccess(filename):
    try:
        atDataList = parse.ParseTargetList(filename)

        app = application.Application()
        scene = scenario.Scenario(app, 'Scheduling', '+24hrs')
        sat = satellite.Satellite(scene, 'MOCI', 25544)

        ats = []
        for i in range(len(atDataList)):
            print(atDataList[i])
            at = areatarget.AreaTarget(scene,
                               atDataList[i][0].replace(' ','_').replace('.','').replace('(','').replace(')',''),
                               atDataList[i][1:])
            ats.append(at)
    
        groundStation = areatarget.AreaTarget(scene,name='GroundStation',
					coordList=[(33.9487,-83.3754)],radius=0.001)
        groundStation.SetElevationConstraint(25)

        ats.append(groundStation)

        #TODO Sort the access times
        outputFile = open('Access.csv','w')
        for i in range(len(ats)):
            access = sat.GetAccess(ats[i])
            try:
                for n in range(len(access)):
                    string = access[n][0] + "," + access[n][1] + "," + ats[i].name + '\n'
                    outputFile.write(string)
            except Exception as e:
                    pass
        outputFile.close()
        return 0
        
    except Exception as e:
        raise SyntaxError(str(e))
        return 1
