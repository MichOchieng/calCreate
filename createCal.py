from icalendar import Calendar, Event
from datetime import datetime
import sys,tempfile,os

class MyCalendar:
    c  = Calendar()
    eList = []

    EVENT_START       = 'CFUR'
    EVENT_END         = '*'
    EVENT_DESCRIPTION = ''

    # Switch statement alternative
    #   1 = Title/Summary
    #   2 = Description
    #   3 = dtstart
    #   4 = dtend

    def readFile(self):
        try:
            with open(sys.argv[1],'r',encoding='utf-8',errors='ignore') as file:
                lines = file.readlines()
        except OSError:
            print("Something went wrong reading the file!")
            sys.exit()
        
        EVENT_DESCRIPTION = ''

        e  = Event()
        for line in lines:
            if(self.EVENT_START in line.splitlines()[0] and '\n' not in line.splitlines()[0] and 'Playlist' in line.splitlines()[0]): # Bandaid fix for grabbing the correct titles
                e.add('summary',line)
            elif(self.EVENT_END not in line):
                EVENT_DESCRIPTION += line # Adds desc text to event desc up until seperator
            elif(self.EVENT_END in line):
                e.add('description', self.EVENT_DESCRIPTION)
                self.c.add_component(e)
        directory = tempfile.mkdtemp()
        with open(sys.argv[2],'wb') as file2:
                file2.write(self.c.to_ical())
                file2.close()

mc = MyCalendar()
mc.readFile()   