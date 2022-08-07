###### NOTES / SAMPLE CODE TO REFERENCE ######
# Creates a calender with an event + outputs an ics file
# This is through the ics package/library
from ics import Calendar, Event

c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
print(c.events)
# {<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>}
with open('event.ics', 'w') as f:
    f.writelines(c.serialize_iter())