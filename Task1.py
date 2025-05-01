student={'Abhishek':80,'Shashank':70,'Rahul':85,'Alice':85}
myinput=input("Enter the student name's: ")
if myinput in student:
    print(f"{myinput}'s marks:",student[myinput])
else:
    print("student not found.")
