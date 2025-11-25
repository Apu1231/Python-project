TodoList = []
print("Welcome to To-Do-List")

while True:
    print("\nWelcome to our website")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark All tasks done")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        task = input("Add a Task: ")
        description = input("Add a Description: ")

        newTask = {
            "task": task,
            "description": description
        }

        TodoList.append(newTask)
        print("\nTask Added successfully 🎉✅")

    elif choice == 2:
        if len(TodoList) == 0:
            print("No Task Added. Add a task first.")
        else:
            print("\nHere is Your Task List 👇")
            count = 1
            for t in TodoList:
                print(f"{count}. {t['task']} - {t['description']}")
                count += 1

    elif choice == 3:
        print("Your All Tasks Are Marked Done ✅")
        TodoList.clear()

    elif choice == 4:
        print("Thank You For Using Our website")
        break

    else:
        print("❌ Choose a Valid Option")
