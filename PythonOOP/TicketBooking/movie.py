from datetime import datetime

class Movie:

    # add timings later
    def __init__(self, name: str, duration: str, description: str) -> None:
        self.name = name
        self.duration = duration
        self.decription = description
        # self.timings = [time.strftime('%H:%M %B %d %Y') for time in timings]
    
    def __str__(self):
        return f"{self.name}"