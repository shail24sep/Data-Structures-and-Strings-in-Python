# Data-Structures-and-Strings-in-Python

**Task 1: Create a Dictionary of Student Marks**

Explanation:

**Dictionary Creation:**

student = {'Abhishek': 80, 'Shashank': 70, 'Rahul': 85, 'Alice': 85}
A dictionary named student is defined.

It stores student names as keys and their marks as values.

**User Input:**
myinput = input("Enter the student name's: ")
The user is asked to input a student's name.
The result is stored in the variable myinput.

**Check and Output:**
if myinput in student:
    print(f"{myinput}'s marks:", student[myinput])
else:
    print("student not found.")

The code checks whether the inputted name exists in the dictionary.

If it does exist, it prints the student's marks using an f-string (formatted string).

If it does not exist, it displays "student not found."

**Expected Output:**

Enter the student name's: Alice
Alice's marks: 85

If student doesnot exist in the disctionary

Enter the student name's: John
student not found.


**Task 2: Demonstrate List Slicing**

**List Definition:**

MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A list named MyList is created containing the numbers 1 through 10.

**Print Original List:**
print("Original list:", MyList)
Displays the entire list.

**List Slicing:**
x = MyList[0:5]
Extracts a sublist of the first 5 elements (index 0 to 4) from MyList.
This sublist is [1, 2, 3, 4, 5] and is stored in variable x.

**Print Extracted Elements:**
print("Extracted first five elements:", x)
Displays the sliced sublist.

**Reverse the Extracted Elements:**
print("Reversed extracted elements:", x[::-1])
x[::-1] is a Python slice syntax to reverse the list.
It prints [5, 4, 3, 2, 1].

**expected output:**

Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]


