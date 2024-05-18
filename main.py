import mysql.connector as con
import os

db = con.connect(
    host="<host>",
    user="<username>",
    password="<passwd>",
    database="<database>"
)
db_cursor = db.cursor()

def newStd():
    name = input("Enter Name: ")
    cl = input("Enter Class: ")
    rollNum = int(input("Enter Roll Number: "))
    phone = input("Enter Mobile Number: ")
    address = input("Enter Student Address: ")
    data = (name, cl, rollNum, phone, address)
    sql = 'insert into student values(%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db.commit()
    print("Data saved Sucessfully!")
    return

def rmStd():
    cl = input("Enter Studentc class:")
    rollNum = int(input("Enter Roll Number: "))
    data = (cl,rollNum)
    sql = 'delete from student where class=%s and roll=%s'
    db_cursor.execute(sql, data)
    db.commit()
    print("Update Sucess!")
    return

def allStudents():
    db_cursor.execute("SELECT * FROM student")
    students = db_cursor.fetchall()
    for student in students:
        print("=============================================")
        print(f"Name: {student[0]}")
        print(f"Class: {student[1]}")
        print(f"Roll Number: {student[2]}")
        print(f"Phone Number: {student[3]}")
        print(f"Address: {student[4]}")
    print("=============================================")
    return

def classStudents():
    cl = input("Enter class: ")
    data = (cl,)
    db_cursor.execute("SELECT * FROM student where class=%s", data)
    students = db_cursor.fetchall()
    for student in students:
        print("=============================================")
        print(f"Name: {student[0]}")
        print(f"Class: {student[1]}")
        print(f"Roll Number: {student[2]}")
        print(f"Phone Number: {student[3]}")
        print(f"Address: {student[4]}")
    print("=============================================")
    return

def classAttd():
    cl = input("Enter Class: ")
    clTeacher = input("Enter Teacher: ")
    strength = int(input("Enter Class Strength: "))
    date = input("Date (yyyy-mm-dd): ")
    absent = int(input("Number of absent students: "))
    data = (cl, clTeacher, strength, date, absent)
    sql = 'INSERT INTO classAttenadce (class, clteacher, totalst, date, absentees) VALUES (%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db.commit()
    print("Attendance updated successfully!")
    return

def showClassAttd():
    sql = 'select * from  classAttenadce'
    db_cursor.execute(sql)
    attd = db_cursor.fetchall()
    for i in attd:
        print("=============================================")
        print("Class: ", i[0])
        print("Teacher: ", i[1])
        print("Class Strength: ", i[2])
        print("Date: ", i[3])
        print("Absent Students: ", i[4])
    print("=============================================")
    return

def newTeacher():
    teacherID = int(input("Enter Teacher ID: "))
    name = input("Enter Name: ")
    sal = int(input("Enter Salary: "))
    address = input("Enter Address: ")
    phone = input("Enter Mobile Number: ")
    data = (teacherID, name, sal, address, phone)
    sql = 'insert into teacher values(%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db.commit()
    print("Data saved Sucessfully!")
    return

def rmTeacher():
    name = input("Enter Name: ")
    teacherID = int(input("Enter Teacher ID: "))
    data = (name, teacherID)
    sql = 'delete from teacher where name=%s and tcode=%s'
    db_cursor.execute(sql, data)
    db.commit()
    print("Update Sucess!")
    return

def upSalary():
    teacherID = int(input("Enter Teacher ID: "))
    sal = int(input("Enter Salary: "))
    data = (sal, teacherID)
    sql = 'update teacher set salary=%s where tcode=%s'
    db_cursor.execute(sql, data)
    db.commit()
    print("Update Sucess!")
    return

def allTeacher():
    db_cursor.execute("SELECT * FROM teacher")
    teachers = db_cursor.fetchall()
    for teacher in teachers:
        print("=============================================")
        print(f"Teacher ID: {teacher[0]}")
        print(f"Name: {teacher[1]}")
        print(f"Salary: {teacher[2]}")
        print(f"Address: {teacher[3]}")
        print(f"Phone Number: {teacher[4]}")
    print("=============================================")
    return

def teacherAttd():
    name = input("Enter Name: ")
    date = input("Date (yyyy-mm-dd): ")
    absent = input("Attendance: ")
    data = (name, date, absent)
    sql = 'INSERT into teacherAttendance values(%s,%s,%s)'
    db_cursor.execute(sql, data)
    db.commit()
    print("Attendance updated Sucessfully!")
    return

def showTeacherAttd():
    sql = 'select * from  teacherAttendance'
    db_cursor.execute(sql)
    attd = db_cursor.fetchall()
    for i in attd:
        print("=============================================")
        print("Name: ", i[0])
        print("Date: ", i[1])
        print("Attendance: ", i[2])
    print("=============================================")
    return

def updateFees():
    cl = input("Enter Class: ")
    monthly = int(input("Enter Monthly Fees: "))
    bus = int(input("Enter Bus Fees: "))
    school = int(input("Enter School Fees: "))
    tech = int(input("Enter Tech Fees: "))
    discount = int(input("Enter discount % (Enter 0 if None): "))
    total = ((monthly+bus+school+tech)-((monthly+bus+school+tech)*(discount/100)))
    print(f"Total Fees will be: {total}")
    data = (cl,monthly,bus,school,tech, total)
    sql = 'update feestructure set class=%s, monthly=%s, busfee=%s, scfee=%s, techfee=%s, total=%s'
    db_cursor.execute(sql, data)
    db.commit()
    return

def dispFees():
    sql = 'select * from feestructure'
    db_cursor.execute(sql)
    fees = db_cursor.fetchall()
    for i in fees:
        print("=============================================")
        print(f"Class: {i[0]}")
        print(f"Monthly Fees: {i[1]}")
        print(f"Bus Fees: {i[2]}")
        print(f"School Fees: {i[3]}")
        print(f"Tech Fees: {i[4]}")
        print(f"Total Fees: {i[5]}")
    print("=============================================")
    return

def addBook():
    bookID = int(input("Enter Book ID: "))
    author = input("Enter Author: ")
    publish = input("Enter Publisher: ")
    genre = input("Enter Genre: ")
    data = (bookID, author, publish, genre)
    sql = 'insert into library values( %s, %s, %s, %s)'
    db_cursor.execute(sql,data)
    db.commit()
    return

def fetchBooks():
    sql =  'select * from library'
    db_cursor.execute(sql)
    books = db_cursor.fetchall()
    for book in  books:
        print("=============================================")
        print(f"Book ID: {book[0]}")
        print(f"Book Author: {book[1]}")
        print(f"Book Publisher: {book[2]}")
        print(f"Book Genre: {book[3]}")
    print("=============================================")
    return

def rmBook():
    bookID = int(input("Enter Book ID: "))
    data = (bookID,)
    sql = 'delete from library where bid=%s'
    db_cursor.execute(sql,data)
    db.commit()
    return

def clearTerm():
    os.system('clear')

def main():
    while True:
        try:
            clearTerm()
            ch = 'y'
            while ch in ['y', 'Y']:
                print("<------- School Management ------->")
                print("1. Student")
                print("2. Teacher")
                print("3. Class Attendance") 
                print("4. Teacher Attendance")
                print("5. Fees Structure")
                print("6. Library")
                print("7. Exit")
                option = int(input("Entry Option: "))
                if option == 1:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Add Student")
                        print("2. Remove Student")
                        print("3. Display class Students")
                        print("4. Display all students")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            newStd()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            rmStd()
                        elif task == 3:
                            clearTerm()
                            print("<------- School Management ------->")
                            classStudents()
                        elif task == 4:
                            clearTerm()
                            print("<------- School Management ------->")
                            allStudents()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()
                elif option == 2:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Add Teacher")
                        print("2. Remove Teacher")
                        print("3. Display all Teachers")
                        print("4. Update Salary")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            newTeacher()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            rmTeacher()
                        elif task == 3: 
                            clearTerm()
                            print("<------- School Management ------->")
                            allTeacher()
                        elif task == 4:
                            clearTerm()
                            print("<------- School Management ------->")
                            upSalary()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()

                elif option == 3:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Enter Class Attendance")
                        print("2. Display Class Attendance")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            classAttd()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            showClassAttd()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()
                elif option == 4:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Enter Teacher Attendance")
                        print("2. Display Teacher Attendance")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            teacherAttd()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            showTeacherAttd ()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()
                elif option == 5:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Update  Fees")
                        print("2. Display Fees details")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            updateFees()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            dispFees ()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()
                elif option == 6:
                    op = 'y'
                    while op in ['y', 'Y']:
                        clearTerm()
                        print("<------- School Management ------->")
                        print("1. Add Book")
                        print("2. Remove Book")
                        print("3. Display All Books")
                        task = int(input("Enter Option: "))
                        if task == 1:
                            clearTerm()
                            print("<------- School Management ------->")
                            addBook()
                        elif task == 2:
                            clearTerm()
                            print("<------- School Management ------->")
                            rmBook ()
                        elif task == 3:
                            clearTerm()
                            print("<------- School Management ------->")
                            fetchBooks ()
                        else:
                            print("<------- School Management ------->")
                            print("Please enter a valid option!!")
                        op = input("Continue (y/n): ")
                        clearTerm()
                elif option == 7:
                    exit()
                else:
                    clearTerm()
        except KeyboardInterrupt:
            print("KeyboardInterrupt!!")
            exit()
        except Exception as e:
            print(f"Error Occured: {e}")

if __name__ == "__main__":
    main()