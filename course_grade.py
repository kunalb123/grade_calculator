
# this script calculates the percentage grade for a particular course given user inputs


# output welcome message
print "\nWelcome to Course Percentage Calculator"


# a dictionary to hold information about weightage and percent earned
percents = dict()

course = raw_input("What course grade would you like to calculate? ")   # store the course name

# loop through the categories of the course 
runner = "y"
while runner == "y":
    try:
        category = raw_input("\nEnter a grade category: ")
        weight = input("Enter a weightage for {} as a decimal: ".format(category))
        earned = input("Enter percentage of {} earned: ".format(category))
        print "{}\t: {}\t: {}".format(category, weight, earned)
        percents[weight] = earned
    except:
        print "Something went wrong. The weightage must be a decimal and percentage must be <= 100"
    
    runner = raw_input("Are there more categories to add (y/n)? ")


# display results
print "\n\nHere's what I've calculated:\n"
if sum(percents.keys()) != 1:
    print "There seems to be some categories incorrectly inputted"
    print "The sum of all the weightages should be 1, but it's {}".format(sum(percents.keys()))
else:
    overall_percentage = 0
    for weight, earned in percents.items():
        overall_percentage = overall_percentage + (weight * earned)
    print "Your overall percentage in {} is {}".format(course, overall_percentage)
print ""

    
    