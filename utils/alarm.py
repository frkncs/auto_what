import datetime


class Alarm:

    def setAlarm(self, hour, minute):
        while (True):
            if (hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute):
                break
