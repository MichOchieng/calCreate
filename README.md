
# iCalendar Generator
This is a program that will generate .ical files by parsing from an input text file with a specific format (specified below). 

## Functions
- readFile()
    - This function will try to take the first command line argument as the incoming file name to parse. If succesful, calendar events will be created from the data in the parse file.
- enterTime()
    - This function is used to allow users to enter calendar event datetimes.
- confirmInput()
    - This function is uesd to confirm user input in the enterTime function.
- selectRecurrance()
    - This function allows users to specify how often they want events to occur.
- createFile()
    - This function is what takes the calendar object and creates the resulting .ical file.
## Input File format
The formatting of input files is very integral to how the readFile function will interpret/create events. Below is an example of how the input file should be formatted.
    
    <EVENT_NAME>
    <EVENT_SUMMARY>
    ***************
    <EVENT_NAME>
    <EVENT_SUMMARY>
    ***************
    <EVENT_NAME>
    <EVENT_SUMMARY>
    ***************
    .
    .
    .   
    
The readFile function will always use the first line of the file and the first line after a series of astrixes as the event name. Everything following the event name will be used as the event summary (more information on how this is done can be found in the comments of the readFile function).
## How to use
This program is ran from a command line interface, below is an example of the arguments used to run the program.
    
    my@comp: python3 calCreate.py <input file name>.txt <output ical file name>

**Example File (parseFile.txt)**

    CFUR's Jazz Jukebox
    The original rebel music. Improvised... WHAT!? Fusion... WHAT!? Classic too… WHAT!? Jazz keeps on pushing the envelope. Even when other genres cease the Jazz hands keep going. A tasty brew of tunes for you to chill too. Cozy up to with your CFUR.
    *****************************************************************


**Example input**
    
    my@comp: python3 createCal.py parseFile.txt myCal
    Enter event start datetime in the format YY/MM/DD HH:MM:SS for CFUR's Jazz Jukebox
    21/11/03 12:00:00
    You entered the datetime 21/11/03 12:00:00 is this correct? (y/n)
    y
    Enter event end datetime in the format YY/MM/DD HH:MM:SS for CFUR's Jazz Jukebox
    21/11/03 13:00:00
    You entered the datetime 21/11/03 13:00:00 is this correct? (y/n)
    y
    Would you like to make CFUR's Jazz Jukebox a reoccuring event? (y/n)
    y
    How often would you like for the event CFUR's Jazz Jukebox to be repeated? (daily,weekly,monthly,yearly)
    daily

**Example Output (myCal.ical)**

    BEGIN:VCALENDAR
    BEGIN:VEVENT
    SUMMARY:CFUR's Jazz Jukebox\n
    DTSTART;VALUE=DATE-TIME:20211103T120000
    DTEND;VALUE=DATE-TIME:20211103T130000
    RRULE:FREQ=DAILY
    DESCRIPTION:The original rebel music. Improvised... WHAT!? Fusion... WHAT!
    ? Classic too… WHAT!? Jazz keeps on pushing the envelope. Even when othe
    r genres cease the Jazz hands keep going. A tasty brew of tunes for you to
    chill too. Cozy up to with your CFUR.\n
    END:VEVENT
    END:VCALENDAR

