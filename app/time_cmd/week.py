from .scheme import Scheme


class Week:
    """
    week()
    week Schemes within days
    """
    def __init__(self):
        self.week = {"monday": [],
                     "tuesday": [],
                     "wednesday": [],
                     "thursday": [],
                     "friday": [],
                     "saturday": [],
                     "sunday": []
                     }

    def addmonday(self, s: Scheme):
        self.week["monday"].append(s)

    def addtuesday(self, s: Scheme):
        self.week["tuesday"].append(s)

    def addwednesday(self, s: Scheme):
        self.week["wednesday"].append(s)

    def addthursday(self, s: Scheme):
        self.week["thursday"].append(s)

    def addfriday(self, s: Scheme):
        self.week["friday"].append(s)

    def addsaturday(self, s: Scheme):
        self.week["saturday"].append(s)

    def addsunday(self, s: Scheme):
        self.week["sunday"].append(s)

    def popmonday(self, s: Scheme):
        self.week["monday"].pop(s)

    def poptuesday(self, s: Scheme):
        self.week["tuesday"].pop(s)

    def popwednesday(self, s: Scheme):
        self.week["wednesday"].pop(s)

    def popthursday(self, s: Scheme):
        self.week["thursday"].pop(s)

    def popfriday(self, s: Scheme):
        self.week["friday"].pop(s)

    def popsaturday(self, s: Scheme):
        self.week["saturday"].pop(s)

    def popsunday(self, s: Scheme):
        self.week["sunday"].pop(s)

    def __str__(self) -> str:
        return str(self.week)

    def __iter__(self):
        for day in self.week:
            yield day
