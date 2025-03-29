import logging
from crud import add_task, get_task, update_task, mark_task_completed, delete_task

# ✅ Configure Logging (Logs errors to a file)
logging.basicConfig(
    filename="todo_app.log", # save logs to a file
    level=logging.DEBUG, # Log all messages (DEBUG, INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

# valid input
def get_valid_int(prompt):
    """Function to safely get an integer input from the user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    try:
        while True:
            print("\n📌 TODO App Menu:")
            print("1️⃣ Add Task")
            print("2️⃣ View Tasks")
            print("3️⃣ Edit Task")
            print("4️⃣ Mark Task as Completed")
            print("5️⃣ Delete Task")
            print("0️⃣ Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                title = input("Enter your TASK: ").strip()

                if title:
                    add_task(title)
                else:
                    print("⚠️ Task title cannot be empty.")

            elif choice == 2:
                get_task()

            elif choice == 3:
                task_id = get_valid_int("Enter the ID of the task you want to edit: ")
                new_title = input("Edit your TASK: ").strip()

                if new_title:
                    update_task(task_id, new_title)
                else:
                    print("⚠️ Task title cannot be empty.")

            elif choice == 4:
                task_id = get_valid_int("Enter the ID of the task you want to mark as completed: ")
                mark_task_completed(task_id)

            elif choice == 5:
                task_id = get_valid_int("Enter the ID of the task you want to delete: ")
                delete_task(task_id)

            elif choice == 0:
                print("👋 Exiting TODO App. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("❌ An unexpected error occurred. Check 'error.log' for details.")

if __name__ == "__main__":
    main()