# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # greeting and init variables from user input
    print("Grade Point Calculator")
    grade = input("Please enter a letter grade (A, B, C, D, F): ").upper()
    modifier = input("Please enter a modifier (+, -, or nothing): ")

    # assign the correct number value for each possible letter value
    if (grade == "A"):
        grade = 4
    elif (grade == "B"):
        grade = 3
    elif (grade == "C"):
        grade = 2
    elif (grade == "D"):
        grade = 1
    elif (grade == "F"):
        grade = 0
    # if the user doesnt pick a valid grade letter, print error message and end the program
    else:
        print("Invalid letter grade. Please try again.")
        return

    # add/subtract 0.3 depending on the modifier
    if (modifier == "+"):
        grade = grade + 0.3
    elif (modifier == "-"):
        grade = grade - 0.3
    # if no modifier was given, do nothing
    elif (modifier == ""):
        pass
    # if an invalid modifier was given, print error message and end the program
    else:
        print("Invalid modifier. Please try again.")
        return
    
    # if the grade is greater than 4 set it equal to 4
    if (grade >= 4):
        grade = 4
    # if the grade is 0 set it equal to 0 regardless of the modifier
    # 0.7 is the lowest possible non 0 grade so anything lower than that should be a 0
    elif (grade < 0.7):
        grade = 0

    # print the final grade
    print("The numeric value is: {0:.1f} \n".format(grade))

    # YOUR CODE ENDS HERE
main()
