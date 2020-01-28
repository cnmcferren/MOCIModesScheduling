
def ParseFile(filename):
    f = open(filename,'r')
    
    lines = f.readlines()
    f.close()
    
    elements = []
    for i in range(len(lines)):
        
        line = lines[i].split(',')
        
        name = line[0]
        
        coord0 = (line[8],line[9])
        coord1 = (line[8],line[11])
        coord2 = (line[10],line[11])
        coord3 = (line[10],line[9])
        
        elements.append([name,coord0,coord1,coord2,coord3])
 
    return elements       
    