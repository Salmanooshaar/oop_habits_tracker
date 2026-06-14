import datetime 

class Habit:
    """It make all relevant data into single object"""
    def __init__(self, name, periodicity):
        self.name = name
        self. periodicity = periodicity
        
        # zero completion at first
        self.completions = []
        
        current_time = datetime.datetime.now()
        # Using isoformat() to make it easy to store with json
        self.created_at = current_time.isoformat()

    def mark_completed(self):
        """It mark the completed habit at current time"""
        completion_time = datetime.datetime.now()
        self.completions.append(completion_time)