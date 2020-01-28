import parse
from stkhelper import application, scenario, satellite, areatarget

atDataList = parse.ParseFile('TargetList.csv')

app = application.Application()
scene = scenario.Scenario(app, 'Scheduling', '+24hrs')
sat = satellite.Satellite(scene, 'MOCI', 25544)

ats = []
for i in range(len(atDataList)):
    at = areatarget.AreaTarget(scene,
                               atDataList[i][0].replace(' ','_').replace('.','').replace('(','').replace(')',''),
                               atDataList[i][1:4])
    ats.append(at)
    
groundStation = areatarget.AreaTarget(scene,'GroundStation',
                                      [(33.9487,-83.3754)])
groundStation.SetElevationConstraint(25)

ats.append(groundStation)

outputFile = open('Access.csv','w')
for i in range(len(ats)):
    access = sat.GetAccess(ats[i])
    try:
    	for n in range(len(access)):
        	string = access[n][0] + "," + access[n][1] + "," + ats[i].name + '\n'
        	outputFile.write(string)
    except Exception:
	pass
        
outputFile.close()