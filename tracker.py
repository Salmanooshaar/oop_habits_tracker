from datetime import datetime
import json
from habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits_list = []

    def add_habit(self, name, periodicity):
        """Creat a new habit and store it to habit_list"""

        new_habit = Habit(name, periodicity)
        self.habits_list.append(new_habit)

        print(f"{name} has been added to you habit list.")

    def check_off(self, habit_name):
        """mark the user's habit as completed"""

        for habit in self.habits_list:
            if habit.name == habit_name:
                #we need the exact time.
                today = datetime.now().date().isoformat()
                #this will prevent the user from complete the task that is already completed.
                for completion in habit.completions:
                    if completion.startswith(today):
                            print(f"{habit_name} is already completed for today")
                            
                            return
                full_time = datetime.now().isoformat()
                habit.completions.append(full_time)
                print(f"Good jop you have completed {habit_name} for today.")  
                
                return
        print(f"Erorr we could not find your {habit_name}.") 

    def show_all_habits(self):
        """Display all habits currently store""" 


        print("\nYour current habits:")
        for index, habit in enumerate(self.habits_list, 1):
            print(f"{index}- {habit.name}")
        print()

    def save_habits(self, filename='habits_data.json'):
        saving_data = []

        for habit in self.habits_list:
            habit_data = {
                "name" : habit.name,
                "periodicity" : habit.periodicity
            }
            saving_data.append(habit_data)

        with open(filename, 'w') as file:
            json.dump(saving_data, file, indent=4)

    def load_habits(self, filename='habits_data.json'):
        try:
            with open(filename, 'r') as file:
                saved_data = json.load(file)

                for item in saved_data:
                    rebuilt_habit = Habit(item["name"], item["periodicity"])
                    self.habits_list.append(rebuilt_habit)
        except FileNotFoundError:
            pass
