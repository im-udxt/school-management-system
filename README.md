

# School Management System

## Overview

This project is a Python-based command-line application designed to manage various aspects of a school system. It provides functionalities for managing students, teachers, class attendance, teacher attendance, fees structure, and library books. The application interacts with a MySQL database to store and retrieve data.

## Features

- **Student Management**
  - Add new students
  - Remove students
  - Display students by class
  - Display all students

- **Teacher Management**
  - Add new teachers
  - Remove teachers
  - Display all teachers
  - Update teacher salary

- **Class Attendance Management**
  - Record class attendance
  - Display class attendance

- **Teacher Attendance Management**
  - Record teacher attendance
  - Display teacher attendance

- **Fees Structure Management**
  - Update fees structure
  - Display fees structure

- **Library Management**
  - Add new books
  - Remove books
  - Display all books

## Prerequisites

- Python 3.12.2
- MySQL server
- MySQL Connector for Python

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/school-management-system.git
    cd school-management-system
    ```

2. **Install required Python packages:**

    ```sh
    pip install mysql-connector-python
    ```

3. **Set up the MySQL database:**

    Create a MySQL database and the necessary tables. Below are the table descriptions:

    **Class Attendance Table (`classAttenadce`):**
    
    ```sql
    +-----------+--------------+------+-----+---------+-------+
    | Field     | Type         | Null | Key | Default | Extra |
    +-----------+--------------+------+-----+---------+-------+
    | class     | varchar(30)  | YES  |     | NULL    |       |
    | clteacher | varchar(40)  | YES  |     | NULL    |       |
    | totalst   | varchar(30)  | YES  |     | NULL    |       |
    | date      | varchar(30)  | YES  |     | NULL    |       |
    | absentees | varchar(300) | YES  |     | NULL    |       |
    +-----------+--------------+------+-----+---------+-------+
    ```

    **Fees Structure Table (`feestructure`):**

    ```sql
    +---------+-------------+------+-----+---------+-------+
    | Field   | Type        | Null | Key | Default | Extra |
    +---------+-------------+------+-----+---------+-------+
    | class   | varchar(30) | YES  |     | NULL    |       |
    | monthly | varchar(30) | YES  |     | NULL    |       |
    | busfee  | varchar(30) | YES  |     | NULL    |       |
    | scfee   | varchar(30) | YES  |     | NULL    |       |
    | techfee | varchar(30) | YES  |     | NULL    |       |
    | total   | varchar(30) | YES  |     | NULL    |       |
    +---------+-------------+------+-----+---------+-------+
    ```

    **Library Table (`library`):**

    ```sql
    +-----------+-------------+------+-----+---------+-------+
    | Field     | Type        | Null | Key | Default | Extra |
    +-----------+-------------+------+-----+---------+-------+
    | bid       | varchar(30) | YES  |     | NULL    |       |
    | author    | varchar(30) | YES  |     | NULL    |       |
    | publisher | varchar(30) | YES  |     | NULL    |       |
    | genre     | varchar(30) | YES  |     | NULL    |       |
    +-----------+-------------+------+-----+---------+-------+
    ```

    **Student Table (`student`):**

    ```sql
    +---------+--------------+------+-----+---------+-------+
    | Field   | Type         | Null | Key | Default | Extra |
    +---------+--------------+------+-----+---------+-------+
    | name    | varchar(30)  | YES  |     | NULL    |       |
    | class   | varchar(30)  | YES  |     | NULL    |       |
    | roll    | varchar(30)  | YES  |     | NULL    |       |
    | phone   | varchar(30)  | YES  |     | NULL    |       |
    | address | varchar(255) | YES  |     | NULL    |       |
    +---------+--------------+------+-----+---------+-------+
    ```

    **Teacher Table (`teacher`):**

    ```sql
    +---------+--------------+------+-----+---------+-------+
    | Field   | Type         | Null | Key | Default | Extra |
    +---------+--------------+------+-----+---------+-------+
    | tcode   | varchar(30)  | NO   | PRI | NULL    |       |
    | name    | varchar(30)  | YES  |     | NULL    |       |
    | salary  | varchar(30)  | YES  |     | NULL    |       |
    | address | varchar(255) | YES  |     | NULL    |       |
    | phone   | varchar(30)  | YES  |     | NULL    |       |
    +---------+--------------+------+-----+---------+-------+
    ```

    **Teacher Attendance Table (`teacherAttendance`):**

    ```sql
    +------------+-------------+------+-----+---------+-------+
    | Field      | Type        | Null | Key | Default | Extra |
    +------------+-------------+------+-----+---------+-------+
    | name       | varchar(30) | YES  |     | NULL    |       |
    | date       | varchar(30) | YES  |     | NULL    |       |
    | attendance | varchar(30) | YES  |     | NULL    |       |
    +------------+-------------+------+-----+---------+-------+
    ```

4. **Update database connection details:**

    Edit the following lines in the Python script to match your MySQL database configuration:

    ```python
    db = con.connect(
        host="<host>",
        user="<username>",
        password="<passwd>",
        database="<database>"
    )
    ```

## Usage

Run the main script to start the application:

```sh
python main.py
```

The application provides a menu-based interface to navigate through different functionalities. Follow the on-screen prompts to perform various operations.

## Functions

- `newStd()`: Adds a new student to the database.
- `rmStd()`: Removes a student from the database.
- `allStudents()`: Displays all students.
- `classStudents()`: Displays students by class.
- `classAttd()`: Records class attendance.
- `showClassAttd()`: Displays class attendance.
- `newTeacher()`: Adds a new teacher to the database.
- `rmTeacher()`: Removes a teacher from


## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For any issues or queries, please contact [uditgarg.dev@gmail.com].
