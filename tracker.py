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
                habit.mark_completed()
                print(f"Good jop you have completed {habit_name} for today.")  
                
                return
        print(f"Erorr we could not find your {habit_name}.") 

    def show_all_habits(self):
        """Display all habits currently store""" 


        print("\nYour current habits:")
        for index, habit in enumerate(self.habits_list, 1):
            print(f"{index}- {habit.name}")
        print()