import json
import os

students = []

# ------------------ FILE HANDLING ------------------

def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except:
        students = []

def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

# ------------------ UI HELPERS ------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def print_header(title):
    print("\n" + "="*40)
    print(f"{title.center(40)}")
    print("="*40)

def safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("❌ Enter a valid number!")

# ------------------ FEATURES ------------------

def add_student():
    print_header("ADD STUDENT")

    name = input("Enter name: ")
    roll = safe_int("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:
            print("❌ Roll number already exists!")
            return

    marks = {}
    subjects = ["math", "science", "english"]

    for sub in subjects:
        marks[sub] = safe_int(f"{sub.capitalize()} marks: ")

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    save_data()
    print("✅ Student added!")

def view_students():
    print_header("STUDENT LIST")

    if not students:
        print("No students found.")
        return

    print(f"{'Name':<10} {'Roll':<6} {'Avg':<6}")
    print("-"*25)

    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"])
        print(f"{s['name']:<10} {s['roll']:<6} {avg:.2f}")

def search_student():
    print_header("SEARCH STUDENT")

    roll = safe_int("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:
            print(f"\nName: {s['name']}")
            print(f"Roll: {s['roll']}")
            print("Marks:")
            for sub, m in s["marks"].items():
                print(f"  {sub}: {m}")
            return

    print("❌ Student not found.")

def find_topper():
    print_header("TOPPER")

    if not students:
        print("No data available.")
        return

    topper = max(students, key=lambda s: sum(s["marks"].values()) / len(s["marks"]))
    avg = sum(topper["marks"].values()) / len(topper["marks"])

    print(f"🏆 {topper['name']} (Roll {topper['roll']})")
    print(f"Average: {avg:.2f}")

def update_student():
    print_header("UPDATE MARKS")

    roll = safe_int("Enter roll: ")

    for s in students:
        if s["roll"] == roll:
            subject = input("Enter subject: ").lower()

            if subject in s["marks"]:
                s["marks"][subject] = safe_int("New marks: ")
                save_data()
                print("✅ Updated!")
            else:
                print("❌ Subject not found.")
            return

    print("❌ Student not found.")

def delete_student():
    print_header("DELETE STUDENT")

    roll = safe_int("Enter roll: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data()
            print("🗑️ Deleted!")
            return

    print("❌ Student not found.")

# ------------------ MAIN LOOP ------------------

load_data()

while True:
    clear_screen()
    print_header("STUDENT MANAGEMENT SYSTEM")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        find_topper()
    elif choice == "5":
        update_student()
    elif choice == "6":
        delete_student()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice!")

    pause()