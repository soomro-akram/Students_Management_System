
from pathlib import Path

file_path = Path("record.txt")

print("\n\t\t\t\tStudent Management System\n")

def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student age: "))
        grade = input("Enter Student Grade: ")

        with open(file_path,"a") as fs:
            fs.write(f"{student_id}\t {name.upper()} \t {age}\t  {grade.upper()}\n ")

        print("Student added Successfully!")
    except Exception as err:
        print(f"An error occured as {err}")

def view_student():
    try:
        with open(file_path,"r") as fs:
            data =fs.read()
            print(data)
    except Exception as err:
        print(f"An error occured as {err}")

def search_student():
    try:
        student_id = input("Enter Student ID to search: ")

        with open(file_path, "r") as fs:
            records = fs.readlines()

        found = False

        for record in records:
            data = record.strip().split(",")

            if data[0] == student_id:
                print("\nStudent Found!")
                print(f"ID    : {data[0]}")
                print(f"Name  : {data[1]}")
                print(f"Age   : {data[2]}")
                print(f"Grade : {data[3]}")
                found = True
                break

        if not found:
            print("Student not found.")

    except Exception as err:
        print(f"An error occurred: {err}")


def update_student():
    try:
        student_id = int(input("Enter Student ID: "))    

        with open(file_path,"r") as fs:
            data = fs.readline()

            update = False

            with open(file_path,"w") as fs:
                for record in data:
                    Data = record.strip().split(",")

                    if Data[0].strip() == student_id:
                        print("\nStudent Found!")

                        name = input("Enter New Name: ")
                        age = int(input("Enter New Age: "))
                        grade = input("Enter New Grade: ")

                        fs.write(f"{student_id}\t{name.upper()}\t{age}\t{grade.upper()}\n")
                        updated = True

                    else:
                        fs.write(record)

                if update:
                    print("Student Updated Successfully! ")

                else:
                    print("Student ID Not Found! ")

    except Exception as err:
        print(f"An Error occured as {err}")      


def delete_student():
    try:
        student_id = input("Enter Student ID to delete: ")

        with open(file_path, "r") as fs:
            records = fs.readlines()

        deleted = False

        with open(file_path, "w") as fs:
            for record in records:
                data = record.strip().split(",")

                if data[0].strip() == student_id:
                    deleted = True
                    continue

                fs.write(record)

        if deleted:
            print("Student Deleted Successfully!")
        else:
            print("Student ID not found.")

    except Exception as err:
        print(f"An error occurred: {err}")



print("Press 1 for Add a Student :")
print("Press 2 for View Students :")
print("Press 3 for Search a Student :")
print("Press 4 for Update a Student :")
print("Press 5 for Delete a Student :")


user = int(input("\nSelect a Choice :-"))


if user ==1:
    add_student()

elif user ==2:
    view_student()

elif user ==3:
    search_student()

elif user ==4:
    update_student()

elif user ==5:
    delete_student()


else:
    print("Invalid Choice")