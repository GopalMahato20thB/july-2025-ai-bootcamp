from datetime import date

def main():
    print("1. Add Task\n2. View Task\n3. Exit")
    while True:
        choice = input("Enter Your Choice: ").strip()
        if choice == "1":
            task = input("Enter Task to add: ").strip()
            today = date.today().strftime('%d-%m-%y')
            with open("tasks.txt", "a", encoding="utf-8") as a:
                a.write(f"{today}::{task}\n")
            print("Task added!")
        elif choice == "2":
            try:
                with open("tasks.txt", "r", encoding="utf-8") as r:
                    contents = r.readlines()
                    if not contents:
                        print("No tasks found.")
                    else:
                        print("Tasks:")
                        for line in contents:
                            print(line.strip())
            except FileNotFoundError:
                print("No tasks found.")
        elif choice == "3":
            print("Bye Bye!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()

