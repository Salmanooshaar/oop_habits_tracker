from tracker import HabitTracker

def cli():
    """The main funcion contain the main ClI"""
    engine = HabitTracker()
    engine.load_habits()
    
    print("Welcome to your Habit Tracker App") 
    
    while True:
        print("""--menu:--
1-Add a habit
2-All habit
3-Analyze
4-Exit""")
        choice = input("Enter a correct number from the menu: ")
        if choice == '1':
           habit_name = input("Enter a new habit name: ")
           habit_period = input("Enter the periodicity: ")
           engine.add_habit(habit_name, habit_period)

        elif choice == '2':
                    
            if not engine.habits_list:
                print("You do not have a habit to track.")   
                continue
        
            engine.show_all_habits()
            selection = input("Select a habit by entering the number or type 'back' to return.: ")
            if selection.lower() == 'back':
                continue
            
            try:
                selection = int(selection)
                if 1 <= selection <= len(engine.habits_list):
                    selected_habit = engine.habits_list[selection - 1]
                    #puting the sub menu here
                    manage_habit_menu(engine, selected_habit.name)
                else:
                    print("invaild number")
            except ValueError:
                print("Please enter a vaild value.")

        elif choice == '3':
            print("")

        elif choice == '4':
            print("Thank you.")
            engine.save_habits()
            break
        
        else:
            print("Invaild number. Enter from 1 to 4 only!!")

def manage_habit_menu(engain, habit_name):
    """Sub menu for interacting with single habit"""
    
    while True:
        print(f"""--managing: {habit_name}--
1-Mark done
2-Show last time you did {habit_name}
3-Show highest streak of {habit_name}
4-Delete {habit_name}
5-Return to the main menu""")
        sub_choice = input("Enter a correct number from the menu: ")
        
        if sub_choice == "1":
            engain.check_off(habit_name)
        elif sub_choice == "2":
            print("")
        elif sub_choice == "3":
            print("")
        elif sub_choice == "4":
            print("")
        elif sub_choice == "5":
            break
        else:
            print("Invaild number. Enter from 1 to 5 only!!")
if __name__ == "__main__":
    cli()