# 🎓 Student Management System (Python)

## 📌 Project Description

This project is a simple **Student Management System** developed using Python. It is a menu-driven program that allows users to manage student records using basic programming concepts like loops, functions, and lists.

The system can perform operations such as adding, displaying, searching, and deleting student data.

---

## 🚀 Features

* Add new student records
* Display all student details
* Search student by roll number
* Delete student record
* Simple and user-friendly menu system

---

## 🛠️ Technologies Used

* Python (Basic Concepts)
* Data Structures: List
* Functions and Loops

---

## 📂 How the Program Works

### 1. Data Storage

All student records are stored in a list called `students`.

Each student is stored as a list:

```
[name, roll_number, marks]
```

Example:

```
["Rahul", "101", "85"]
```

---

### 2. Functions Used

#### ➤ add_student()

This function is used to add a new student.

* Takes input from the user (name, roll number, marks)
* Stores the data in a list
* Appends it to the main `students` list

---

#### ➤ display_students()

This function displays all student records.

* Checks if the list is empty
* If not, it prints all student details in a formatted way

---

#### ➤ search_student()

This function searches for a student using roll number.

* Takes roll number as input
* Uses a loop to find the matching record
* Displays student details if found

---

#### ➤ delete_student()

This function deletes a student record.

* Takes roll number as input
* Searches for the student
* Removes the record from the list if found

---

### 3. Main Menu Logic

The program uses a `while True` loop to continuously show the menu.

Options:

1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit

* Based on user input, the respective function is called
* The loop runs until the user chooses Exit

---

## 💡 Concepts Used

* Functions
* Lists (Data Structure)
* Loops (for loop, while loop)
* Conditional Statements (if-else)
* User Input Handling

---

## 🎯 Purpose of the Project

The main goal of this project is to understand and apply basic Python concepts in a real-world problem like managing student records.

---

## 📈 Future Improvements

* Store data in a file (so records are saved permanently)
* Add update student feature
* Convert into GUI using Tkinter
* Use database (MySQL)

---

## ✅ Conclusion

This project is a beginner-friendly implementation of a Student Management System. It helps in building a strong foundation in Python programming and understanding how real-world systems work in a simple way.
