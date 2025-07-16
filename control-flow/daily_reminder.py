task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
time_sensitive_message = ""

# Check if the task is time-bound and set the appropriate message
if time_bound == "yes":
    time_sensitive_message = " that requires immediate attention today!"

match priority:
    case "high":
        # Combine the task, priority, and time-sensitive message
        print(f"Reminder: '{task}' is a high priority task{time_sensitive_message}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{time_sensitive_message}")
    case "low":
        # For low priority, if not time-bound, add the specific suggestion.
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            # If low priority but time-bound, use the standard time_sensitive_message
            print(f"Reminder: '{task}' is a low priority task{time_sensitive_message}")
    case _:
        # Handle unexpected priority input
        print("Invalid priority level entered. Please choose high, medium, or low.")