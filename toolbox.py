
import datetime

        
class Toolbox:
    
    @staticmethod
    def CompareTime(time1,time2):       
        """
        Compares if time1 is greater than time2. If it is, it returns true. If
        it is not, it returns false.
        
        Parameters:
            time1 (datetime): Object to test.
            time2 (datetime): Object to compare to time1.
            
            Returns:
                True if time1 is greater than time2. Otherwise, it returns false.
        
        """

        time1Delta = (time1 - datetime.datetime(1970,1,1)).total_seconds()
        time2Delta = (time2 - datetime.datetime(1970,1,1)).total_seconds()
        
        if time1Delta > time2Delta:
            return True
        else:
            return False
    
    @staticmethod    
    def ConvertTime(time1):              
        """
    
        Converts time from STK format to datetime objects.
    
        Parameters:
            time1 (str): The time string from STK.
        
        Returns:
            timeObj1 (datetime): The datetime objects.
        
        """

        monthDict = {"Jan": 1,
                     "Feb": 2,
                     "Mar": 3,
                     "Apr": 4,
                     "May": 5,
                     "Jun": 6,
                     "Jul": 7,
                     "Aug": 8,
                     "Sep": 9,
                     "Oct": 10,
                     "Nov": 11,
                     "Dec": 12}
        
        revMonthDict = {1 : "Jan",
                     2 : "Feb",
                     3 : "Mar",
                     4 : "Apr",
                     5 : "May",
                     6 : "Jun",
                     7 : "Jul",
                     8 : "Aug",
                     9 : "Sep",
                     10 : "Oct",
                     11 : "Nov",
                     12 : "Dec"}
        
        if type(time1) == str:
        
            time1 = str(time1)
            time1 = time1\
                .replace('(','')\
                .replace(')','')\
                .replace("'",'')\
                .replace(',','')
            if time1[0] == 'u':
                time1 = time1[1:]
        
            splitTime1 = time1.split(' ')
            day1 = splitTime1[0]
            month1 = monthDict[splitTime1[1]]
            year1 = splitTime1[2]
        
            clockTime1 = splitTime1[3]
        
            splitClockTime1 = clockTime1.split(':')
            hours1 = splitClockTime1[0]
            minutes1 = splitClockTime1[1]
            seconds1 = splitClockTime1[2].split('.')[0]
            microseconds1 = splitClockTime1[2].split('.')[1]
        
            timeObj1 = datetime.datetime(
                int(year1),
                int(month1),
                int(day1),
                hour=int(hours1),
                minute=int(minutes1),
                second=int(seconds1),
                microsecond=int(microseconds1) * 1000)
        
            return timeObj1
        
        else:
            year = str(time1.year)
            month = revMonthDict[time1.month]
            day = str(time1.day)
            hour = str(time1.hour)
            minute = str(time1.minute)
            second = str(time1.second)
            millisecond = str(int(float(time1.microsecond) / 1000.0))
            
            outputTime = "%s %s %s %s:%s:%s.%s" % (day,month,year,hour,minute,second,millisecond)
            
            return outputTime

    @staticmethod
    def AddAccessArrays(*args):        
        """
    
        For adding access array to a singluar array.
        
        Parameters:
            *args (list): Lists containing the the name and access array in the 
            following format:
                [name, accessArray]
                
        Returns:
            addedArray (list): The array containing all the added access times.
        
        """
        
        addedArray = []
        if len(args) == 1:
            for accessArray in args[1]:
                for line in accessArray[1]:
                    outputLine = [line[0],line[1],accessArray[0]]
                    addedArray.append(outputLine)
                
            return addedArray
        else:    
            for accessArray in args:
                for line in accessArray[1]:
                    outputLine = [line[0],line[1],accessArray[0]]
                    addedArray.append(outputLine)
                
            return addedArray

    @staticmethod
    def SortAllAccess(allAccessArray):
        """
        
        Sorts an array containg access times into chronological order based
        on the start time of the pass.
        
        Parameters:
            allAccessArray (list): List of all access.
        
        Returns:
            outputArray: The sorted access array.
            
        """
        
        outputArray = allAccessArray
        for i in range(len(outputArray)):
            for j in range(0,len(outputArray)-1):
                time1 = outputArray[j] #Full pass array
                time2 = outputArray[j+1] #Full pass array
                time1D = Toolbox.ConvertTime(time1[0]) #Datetime objects of first contact
                time2D = Toolbox.ConvertTime(time2[0]) #Datetime objects of first contact
                
                if Toolbox.CompareTime(time1D,time2D):
                    outputArray[j] = time2
                    outputArray[j+1] = time1
                    
        return outputArray
    
    @staticmethod
    def AccessToCSV(accessArray,outputFilename):
        """
        
        Writes access to a CSV file.
        
        Parameters:
            accessArray (list): List of all access times.
            outputFilename (str): Name of the csv file to be written.
            
        """
        
        outputFile = open(outputFilename,'w')
        for i in range(len(accessArray)):
            for n in range(len(accessArray[i])):
                if n == len(accessArray[i])-1:
                    delimiter = '\n'
                else:
                    delimiter = ','
                outputFile.write(str(accessArray[i][n]) + delimiter)
                
        outputFile.close()