from tracker import HabitTracker

def cli():
    engian = HabitTracker()
    print("Welcome to your Habit Tracker App") 
    
    while True:
        print("""--menu:--
1-Add a habit
2-All habit
3-Analyze
4-Exit""")
        choice = input("Enter a number from the menu: ")
        if choice == '1':
           habit_name = input("Enter a new habit name: ")
           habit_period = input("Enter the periodicity: ")
           engian.add_habit(habit_name, habit_period)

        elif choice == '2':
                    
            if not engian.habits_list:
                print("You do not have a habit to track.")   
                continue
        
            engian.show_all_habits()
            selection = input("Select a habit by entering the number or type 'back' to return.: ")
            if selection.lower() == 'back':
                continue
            try:
                selection = int(selection)
                if 1 <= selection <= len(engian.habits_list):
                    selected_habit = engian.habits_list[selection - 1]
                    print("1-mark")
                    target_habit = input("Enter a number from the menu: ")
                    if target_habit == '1':
                        engian.check_off(selected_habit.name)
                else:
                    print("invaild number")
            except ValueError:
                print("Please enter a vaild value.")

        elif choice == '3':
            print("")

        elif choice == '4':
            print("Thank you.")
            break
        
        else:
            print("Invaild number. Enter 1, 2, 3, or 4 only!!")


if __name__ == "__main__":
    cli()