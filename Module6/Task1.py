try:
    students_marks = {"Alice" : "52", "Rahul" : "72", "Kritika" : "83", "Khushboo" : "67", "Akash" : "56"}
    userInput = input("Enter the student name: ")
    res = students_marks[userInput]
    print( userInput ,"marks: ", res)
except KeyError:
    print("Error: Student not found")