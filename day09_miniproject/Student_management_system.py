students = []

def add_student():
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    
    for s in students: 
        if s["roll"] == roll:
            print("Roll number already exists!")
            return
        
    marks = {}
    subjects = ["math", "science", "english"]
    
    for sub in subjects:
        marks[sub] = int(input(f"Enter marks for {sub}: "))
        
    student = {
        "name": name,
        "roll": roll,   
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!")
    
def view_students():
    if not students: 
        print("No students found.")
        return
    
    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"])
        print(f"Name: {s['name']} | Roll: {s['roll']} | Avg: {avg:.2f}")

def search_student():
    roll = int(input("Enter roll number to search: "))
    
    for s in students: 
        if s["roll"] == roll:
            print("Student found:")
            print(s)
            return
        
    print("Student not found.")
    
def find_topper():
    if not students:
        print("No students available.")
        return
    
    topper = None
    highest = 0
    
    for s in students: 
        avg = sum(s["marks"].values()) / len(s["marks"])
        
        if avg > highest:
            highest = avg
            topper = s
            
    print(f"Topper: {topper['name']} with avg {highest:.2f}")
    
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        find_topper()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")