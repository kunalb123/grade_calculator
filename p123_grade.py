# Python script calculates physics grades

# percent breakdown of categories

print()
print('This program calculates the final course grade for PHYS 123')
print()

# check if overall percent is there and calculate gpa based on that
try: 
    overall_percent = (float)(input("Enter overall percentage if available. Otherwise, type 'n': "))
    print()
except:
    overall_percent = 0.0

# get values for each grade category
if overall_percent == 0.0:
    percents = {}
    percents['exams'] = 0.66
    percents['lecture reading discussion'] = 0.04
    percents['lecture video quiz'] = 0.04
    percents['lecture homework'] = 0.08
    percents['lab section'] = 0.1
    percents['tutorial section'] = 0.08
    final_score = {}
    for cat in percents:
        try:
            val = (float)(input('Input score for {}: '.format(cat)))
            final_score[cat] = val
        except:
            print('Something went wrong. Scores should be inputted as xx.x%. Please try again')
            break
    print()
    for cat in final_score:
        try:
            print('{0:27} {1:10f}'.format(cat, final_score[cat]))
        except:
            print('{0:27} less than 1%'.format(cat))
    print()

    # calculate overall percent in class
    for cat in percents:
        overall_percent += percents[cat] * final_score[cat]


# get GPA breakdown
if overall_percent < 57:
    print('Grade falls below a 2.0')
    print()
    exit()
if overall_percent >= 91:
    print('Congratulations! You got a 4.0!')
    print()
    exit()

# 1.7 percent increase for every 0.1 GPA increase
gpa = round((0.1/1.7)*overall_percent - 1.353, 2)

# print calculations
print("Here's what we've calculated:")
print('Final Percentage: {}'.format(overall_percent))
print('Final GPA: {}'.format(gpa))
print()
