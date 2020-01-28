import parse
from stkhelper import application, scenario, satellite, areatarget

atDataList = parse.ParseFile('TargetList.csv')

app = application.Application()
scene = scenario.Scenario(app, 'Scheduling', '+24hrs')
sat = satellite.Satellite(scene, 'MOCI', 25544)

ats = []
for i in range(len(atDataList)):
    at = areatarget.AreaTarget(atDataList[i][0],
                               atDataList[i][1:4])
    ats.append(at)
    
groundStation = areatarget.AreaTarget('GroundStation',
                                      [(33.9487,-83.3754)])
groundStation.SetElevationConstraint(25)

ats.append(groundStation)

outputFile = open('Access.csv','w')
for i in range(len(ats)):
    access = sat.GetAccess(ats[i])
    for n in range(len(access)):
        string = access[0] + "," + access[1] + "," + ats[i].name + '\n'
        outputFile.write(string)
        
outputFile.close()