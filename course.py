available_courses = ["Python Programming", "Data Science", "Web Development", "Machine Learning", "Cybersecurity"]
enrolled_courses = []
def show_available_courses():
    print("\nAvailable Courses:")
    for i, course in enumerate(available_courses, start=1):
        print(f"{i}. {course}")
def enroll_in_course():
    show_available_courses()
    try:
        choice = int(input("Enter the number of the course you want to enroll in: "))
        if 1 <= choice <= len(available_courses):
            selected_course = available_courses[choice - 1]
            if selected_course not in enrolled_courses:
                enrolled_courses.append(selected_course)
                print(f"You have successfully enrolled in '{selected_course}'.")
            else:
                print("You are already enrolled in this course.")
        else:
            print("Invalid choice. Please select a valid course number.")
    except ValueError:
        print("Please enter a valid number.")
def show_enrolled_courses():
    if enrolled_courses:
        print("\nYou are enrolled in the following courses:")
        for course in enrolled_courses:
            print(f"- {course}")
    else:
        print("\nYou are not enrolled in any courses yet.")
def main():
    while True:
        print("\n--- Course Enrollment System ---")
        print("1. Show Available Courses")
        print("2. Enroll in a Course")
        print("3. View Enrolled Courses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_available_courses()
        elif choice == "2":
            enroll_in_course()
        elif choice == "3":
            show_enrolled_courses()
        elif choice == "4":
            print("Thank you for using the Course Enrollment System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
if __name__ == "__main__":
    main()