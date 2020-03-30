
# this script takes in input on course information to give a GPA value
# my university does grades on GPA (as opposed to percentages) so this script is written for that


# class Course holds information about the name, grade, and number of credits per course
class Course:

    # to create a class object
    def __init__(self, name, grade, credits):
        self.name = name
        self.grade = grade
        self.credits = credits

    # returns a value useful in calculating the overall GPA 
    def gpa_credits(self):
        return self.grade * self.credits

# a list of all the courses to be entered
courses = []


# output welcome text
print "\nWelcome to Grade Calculator"


# prompt to start the program
runner = raw_input("Are there any courses to enter (y/n)? ")

# loop to ask until all courses inputted; course names and GPAs are added to the courses dict
while runner == "y":
    try:
        name = raw_input("Enter the course name: ")
        grade = input("Enter the grade for {}: ".format(name))
        credits = input("Enter the number of credits for {}: ".format(name))
        courses.append(Course(name, grade, credits))
    except:
        print "Something went wrong. Grade and Credit inputs need numbers. Please try again."
    runner = raw_input("\nAre there more courses to enter (y/n)? ")


# give an overall GPA based on the courses list
print "\n\nHere's what I've calculated:\n"
if courses == []:
    print "No GPA to report"
else:
    overall_gpa = 0.0
    total_credits = 0
    for course in courses:
        print "{}\t: {}\t: {}".format(course.name, course.grade, course.credits)
        overall_gpa = overall_gpa + course.gpa_credits()
        total_credits = total_credits + course.credits

    overall_gpa = overall_gpa / total_credits
    print "\nOverall GPA: {}".format(overall_gpa)
print ""