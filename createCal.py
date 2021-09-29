from icalendar import Calendar, Event
from datetime import datetime
import sys,tempfile,os

class MyCalendar:
    cal  = Calendar()
    
    def readFile(self):
        try:
            with open(sys.argv[1],'r',encoding='utf-8',errors='ignore') as file:
                lines = file.readlines()
        except OSError:
            print("Something went wrong reading the file!")
            sys.exit()
        
        EVENT_DESCRIPTION = ''
        EVENT_END         = '*'
        titleSearch       = False
        descriptionSearch = False
        event = Event()
        
        for i,line in enumerate(lines):

            if(i == 0): # Grabs the very first line of the file (assumes the first line will be an event title)
                # Adds title to event
                event.add('summary',line)
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
                # Push event to calendar
                self.cal.add_component(event)
    
    def createFile(self):
        with open(sys.argv[2],'wb') as calFile:
            calFile.write(self.cal.to_ical())
            calFile.close()

mc = MyCalendar()
mc.readFile()   
mc.createFile()