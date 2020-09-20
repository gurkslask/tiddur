import datetime


class exception():
    """
    exception(name: str, starttime: datetime, stoptime: datetime,
    value: bool)

    exceptions used when schemes should be overriden

    Methods:
    check if starttime and stoptime is now, if true return value
    """
    def __init__(self,
                 name: str,
                 starttime: datetime.datetime,
                 stoptime: datetime.datetime,
                 value: bool):
        self.name = name
        self.starttime = starttime
        self.stoptime = stoptime
        self.value = value

    def check(self) -> bool:
        if datetime.datetime.now() > self.starttime and\
                datetime.datetime.now() < self.stoptime:
            return self.value
