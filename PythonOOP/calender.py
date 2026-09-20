from calendar import Calendar
import datetime

class Calender:
    
    def __init__(self) -> None:
        self.evets = []

    def add_event(self, event):
        self.events.append(event)

    @staticmethod
    def is_weekend(date):
        return date.weekday() > 4
    
    @classmethod
    def from_json(cls, filename):
        c = cls()

        return c

class WokCalender(Calender):
    pass

def main():
    c = Calender()
    c.add_event('party')
    today = datetime.date.today()
    print(c.is_weekend(today))
    print(Calendar.is_weekend(today))

    wc = WokCalender.from_json('filename')