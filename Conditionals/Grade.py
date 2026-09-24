marks = int(input("Enter your marks: "))

# Using 'and' keyword
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 50 and marks < 60:
    print("Grade: E")
else:
    print("Grade: F")

# without Using "and" keyword
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")

# Without Using "and" keyword other way
if marks > 100 or marks < 0:
    print("Invalid marks")
elif 90 <= marks < 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
elif 60 <= marks < 70:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: E")
else:
    print("Grade: F")