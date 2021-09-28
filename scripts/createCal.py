import icalendar

class Event:
    # Will be used to encapsulate event data from the parser class
    def __init__(self,name,description,startTime,endTime):
        self.name        = name
        self.description = description
        self.startTime   = startTime
        self.endTime     = endTime

class Calendar:

    def test(self):
        print("foo")