"""

Used to parse a target list for computation from MOCI's target list

Parameters:
        filename(str): Name of the target list file to be parsed.
        
Returns:
        elements(list): Returns a list containing the name and lat/lon
                        coordinate pairs in the following format:
                            [(name),(lat0,lon0),...,(lat3,lon3)]

"""
def ParseTargetList(filename):
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
    
"""

Used to parse access file

Parameters:
    filename(str): The access file to be parsed
    
Returns:
    access(list): List of access times

"""
def ParseAccess(filename):
    #TODO Add functionallity
    return 0