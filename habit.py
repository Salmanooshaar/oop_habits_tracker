import datetime 

class Habit:
    """It make all relevant data into single object"""
    def __init__(self, name, periodicity):
        self.name = name
        self. periodicity = periodicity
        
        # zero completion at first
        self.completion = []
        
        current_time = datetime.datetime.now()
        # Using isoformat() to amke it easy to store with json
        self.created_at = current_time.isoformat()
        