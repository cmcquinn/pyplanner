from ics import Calendar

class Task:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        event = args[1]
        self.name = event.name
        self.uid = event.uid
        self.date = event.end
        self.done = false
        self.desc = event.description
        self.note = ''