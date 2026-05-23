from habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits_list = []

    def add_habit(self, name, periodicity):
        new_habit = Habit(name, periodicity)
        self.habits_list.append(new_habit)

        print(f"{name} has been added to you habit list.")

    def check_off(self, habit_name):
        for habit in self.habits_list:
            if habit.name == habit_name:
                habit.mark_completed()
                print(f"good jop you have completed {habit_name} for today.")  

                return
        print(f"erorr we could not find your {habit_name}.")     