from icalendar import Calendar, Event
from datetime import datetime
import sys

# Todo 
#   Add more error handling for newer additions

class MyCalendar:
    cal       = Calendar()
    startTime = True
    EVENT_RECURRANCE  = ["daily","weekly","monthly","yearly"]
    
    def readFile(self):
        try:
            with open(sys.argv[1],'r',encoding='utf-8',errors='ignore') as file:
                lines = file.readlines()
        except OSError:
            print("Something went wrong reading the file!")
            sys.exit()
        except IndexError:
            print("Don't forget to add an input file as an argument!")
            sys.exit()
        
        EVENT_STARTTIME   = ''
        EVENT_ENDTIME     = ''
        EVENT_DESCRIPTION = ''
        EVENT_END         = '*'
        EVENT_NAME        = ''
        titleSearch       = False
        descriptionSearch = False
        event = Event()
        
        for i,line in enumerate(lines):

            if(i == 0): # Grabs the very first line of the file (assumes the first line will be an event title)
                # Adds title to event
                event.add('summary',line)
                EVENT_NAME = line
                # Indicates that a title was found and that a description is the next priority
                descriptionSearch = True
                titleSearch       = False
            elif(titleSearch):
                event.add('summary',line) # Adds title to event
                # Indicates that a title was found and that a description is the next priority
                descriptionSearch = True
                titleSearch       = False
            elif(descriptionSearch and EVENT_END not in line):
                # Will add each line of the description to a variable up until the event seperator (*) for later use
                EVENT_DESCRIPTION += line
            elif(EVENT_END in line):
                # Event seperator has been found
                descriptionSearch = False   # No longer parsing description
                titleSearch       = True    # Indicates that the next target is an event title
                # Add description to the event
                event.add('description', EVENT_DESCRIPTION)
                EVENT_DESCRIPTION = '' # Clear description temp variable

                # Prompt for event timings
                EVENT_STARTTIME = datetime.strptime(self.enterTime(EVENT_NAME),'%y/%m/%d %H:%M:%S')
                EVENT_ENDTIME   = datetime.strptime(self.enterTime(EVENT_NAME),'%y/%m/%d %H:%M:%S')
                    # Add time to event
                event.add('dtstart', EVENT_STARTTIME)
                event.add('dtend', EVENT_ENDTIME )
                # Prompt for recurrance
                print("Would you like to make " + EVENT_NAME + " a reoccuring event? (y/n)")
                val = input()
                if self.confirmInput(val):
                    event.add('rrule', {'freq': self.selectRecurrance(EVENT_NAME)})  
                else:
                    pass
                # Push event to calendar
                self.cal.add_component(event)
                event = Event() # Fixes issue of having one large event instead of seperate indivdual events
    
    
    def enterTime(self,eventName):
        if(self.startTime):
            self.startTime = False
            print("Enter event start datetime in the format YY/MM/DD HH:MM:SS for " + eventName)
        else:
            self.startTime = True
            print("Enter event end datetime in the format YY/MM/DD HH:MM:SS for " + eventName)
        val = input()
        print("You entered the datetime " + val + " is this correct? (y/n)")
        prompt = input()
        # IF returns false rerun the function
        promptResult = self.confirmInput(prompt)

        if(promptResult):
            return val
        else:
            return self.enterTime(eventName) # Fixes issue with recursively returning values

    def confirmInput(self,input):
        if(input == 'y' or input == 'Y'):
            return True
        elif(input == 'n' or input == 'N'):
            return False
        else:
            print(input + " isn't a valid input.")
            return False

    def selectRecurrance(self,eventName):
        # Prompt user for recurrance
        print("How often would you like for the event " + eventName.strip("/n") + " to be repeated? (daily,weekly,monthly,yearly)")
        
        # Save val
        recurrance = input()

        # Return val if given correct input
        if(recurrance in self.EVENT_RECURRANCE):
            return recurrance
        else:
            print("'" + recurrance + "' isn't an option for event recurrance, please enter an option from the given list.")
            self.selectRecurrance(eventName)

    def createFile(self):
        try:
            with open(sys.argv[2],'wb') as calFile:
                calFile.write(self.cal.to_ical())
                calFile.close()
        except IndexError:
            print("Don't forget to add an output file as the last argument!")
            sys.exit()

mc = MyCalendar()
mc.readFile()   
mc.createFile()