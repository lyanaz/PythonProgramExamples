#!/usr/bin/python
#A Small example of how to convert time in seconds to Days Hours & Minutes, Seconds

TimeInSeconds = 60000

Days, Remainder = divmod(TimeInSeconds,24*60*60)
Hours, Remainder = divmod(Remainder, 60*60)
Minutes, Remainder = divmod (Remainder, 60)
Seconds = Remainder
print (int(Days)," Days ",int(Hours)," Hours ", int(Minutes)," Minutes ", round(Seconds)," Seconds ")
