import datetime


class Scheme():
    """
    scheme(name: str, starthour: int, startmin: int,
    stophour: int, stopmin:int )

    Make different time schemes, and check if time is betwen start and stop
    """
    def __init__(self, name: str, starthour: int, startmin: int,
                 stophour: int, stopmin: int):
        self.name = name
        self.starttime = datetime.time(starthour, startmin)
        self.stoptime = datetime.time(stophour, stopmin)

    def __str__(self) -> str:
        return f"{self.name} - Start: {self.starttime.strftime('%H:%M')}\
            Stop: {self.stoptime.strftime('%H:%M')}"

    def __repr__(self) -> str:
        return f"{self.name} - Start: {self.starttime.strftime('%H:%M')}\
            Stop: {self.stoptime.strftime('%H:%M')}"

    def startmin(self, startmin: int):
        self.starttime = datetime.time(self.starttime.hour, startmin)

    def starthour(self, starthour: int):
        self.starttime = datetime.time(starthour, self.starttime.minute)

    def stopmin(self, stopmin: int):
        self.stoptime = datetime.time(self.stoptime.hour, stopmin)

    def stophour(self, stophour: int):
        self.stoptime = datetime.time(stophour, self.stoptime.minute)

    def check(self):
        tnow = datetime.time(datetime.datetime.now().hour,
                             datetime.datetime.now().minute)
        return self.starttime <= tnow and self.stoptime >= tnow
