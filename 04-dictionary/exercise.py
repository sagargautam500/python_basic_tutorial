# Let‘s Practice
# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

words={
    "table":["a piece of furniture ,list of facts & figures"],
    "cat":"a small animal"
}

# You are given a list of subjects for students. Assume one classroom is required for 1subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,“java”, “python”, “java”, “C++”, “C”
subjects = ["python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"]

unique_subjects = set(subjects)

print("Number of classrooms needed:", len(unique_subjects))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start withan empty 
# dictionary & add one by one. Use subject name as key & marks as value
marks = {}

sub1 = input("Enter subject name: ")
marks[sub1] = int(input("Enter marks: "))

sub2 = input("Enter subject name: ")
marks[sub2] = int(input("Enter marks: "))

sub3 = input("Enter subject name: ")
marks[sub3] = int(input("Enter marks: "))

print("Marks Dictionary:", marks)

# math=float(input("enter marsks of math "))
# science=float(input("enter marsks of science "))
# english=float(input("enter marsks of english "))

# subjects={"math":"","science":"","english":""}
# subjects["math"]=math
# subjects["science"]=science
# subjects["english"]=english
# print(subjects)
