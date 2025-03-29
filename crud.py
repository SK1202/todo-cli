from database import get_connection


# ✅ Create (Add a new task)
"""def add_task(title):
    conn = None  # Initialize connection
    cursor = None  # Initialize cursor

    try:
        conn = get_connection()  # Establish connection
        if conn:  # Ensure connection was successful
            cursor = conn.cursor()  # Create cursor object

            # SQL query to insert a new task
            # sql = "INSERT INTO tasks (title) VALUES (%s)"
            # val = (title,)

            # Executing SQL query
            # cursor.execute(sql, val)

            # ✅ Directly executing SQL query
            cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))

            # Committing changes to database
            conn.commit()

            print("✅ Task added successfully!")

    except Exception as e:
        print(f"❌ Error adding task: {e}")  # Handle errors

    finally:
        # ✅ Close cursor if it was created
        if cursor is not None:
            cursor.close()

        # ✅ Close connection if it was created
        if conn is not None:
            conn.close()"""

"""✅ Best Approach: Using Context Managers (with statement)"""

def add_task(title):
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            # SQL query to insert a new task and execute it
            cursor.execute(
                "INSERT INTO tasks(title) VALUES (%s)",
                (title,)
            )
            # Committing changes to database
            conn.commit()
            print("✅ Task added successfully!")
    except Exception as e:
        print(f"❌ Error adding task: {e}")  # Handle errors



# ✅ Read (Get all tasks)
def get_task():
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            # SQL query to select all tasks and execute it
            cursor.execute("SELECT id, title FROM tasks")
            tasks = cursor.fetchall() # Fetch all tasks
            if tasks:
                print("📋 Task List:")
                for task in tasks:
                    print(f"{task[0]}.{task[1]}") # Print task id and title
            else:
                print("ℹ️ No tasks found.")

    except Exception as e:
        print(f"❌ Error retrieving tasks: {e}")  # Handle errors


# ✅ Update (Edit a task title)
def update_task(task_id, new_title):
    try:
        with get_connection() as  conn, conn.cursor() as cursor:
            # SQL query to select a task by id and execute it
            cursor.execute("UPDATE tasks SET title = %s WHERE id = %s", (new_title, task_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("✅ Task updated successfully!")
            else:
                print("ℹ️ Task not found.")

    except Exception as e:
        print(f"❌ Error updating task: {e}")  # Handle errors


# ✅ Mark as completed (Mark a task as completed)
def mark_task_completed(task_id):
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            # SQL query to select a task by id and execute it
            cursor.execute("UPDATE tasks SET completed = 1 WHERE id = %s", (task_id,))
            conn.commit()

            if cursor.rowcount >0:
                print("✅ Task marked as completed!")
            else:
                print("ℹ️ Task not found.")

    except Exception as e:
        print(f"❌ Error marking task as completed: {e}")  # Handle errors



# ✅ Deleting tasks (Delete a task)
def delete_task(task_id):
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            # SQL query to select a task by id and execute it
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            conn.commit()

            if cursor.rowcount >0:
                print("✅ Task deleted successfully!")
            else:
                print("ℹ️ Task not found.")

    except Exception as e:
        print(f"❌ Error deleting task: {e}")  # Handle errors