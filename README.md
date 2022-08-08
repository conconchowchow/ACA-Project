# ACA-Project - CalendarBot!
##### By Connor Chow, 2022
##### Project for Adobe Career Academy 2022
---

### Website

https://express.adobe.com/page/2ykLGqtb1k6bN/

---

### Description

CalendarBot is a slack bot that can create calendar event for you, right from slack!

All you have to do is direct-message or mention the bot in a channel (with @CalendarBot)
and it will create you an event (an .ics file) that can be added your calendar.

---

### Notes/Comments

1. Dates must be in the format YYYY-MM-DD HH:MM:SS
2. Times must be inputted based on a 24-hour time/clock
3. Timezone is based on the user sending the message!

---

### Format for messages:

- "\<title>" "\<description>" "\<start time>" "\<end time>"

Example:
- mention: @CalendarBot "My cool event" "This is a cool event" "2022-08-06 22:00:00" "2022-08-07 10:00:00"
- direct-message: "My cool event" "This is a cool event" "2022-08-06 22:00:00" "2022-08-07 10:00:00"

---

### Help

Help command examples:
- mention: @CalendarBot help
- direct-message: help

---

### Libraries

Libraries used:
- ics
- arrow
- tz

---

### MIT License
