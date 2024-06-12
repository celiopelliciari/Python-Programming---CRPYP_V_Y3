#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Returns Percentage and Irish equivalent to GPA (4.0) """

# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

# Irish grades dictionary

irish_grades = {
    70: "First Class Honours",
    60: "Upper Second Class (2.1) Honours",
    50: "Lower Second Class (2.2) Honors",
    40: "Class 3 Honors/Pass",
    0: "Fail"}


# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //         computegrade function          // #
# -------------------------------------------- #

# START function computegrade()


def computegrade(s):
    """computegrade() function"""

    p = s / 4 * 100
    for x in irish_grades.keys():
        if p >= x:
            return int(p), irish_grades[x]


# END function computegrade()

# -------------------------------------------- #
# //               help function            // #
# -------------------------------------------- #


def help_():
    """help() function"""

    h = (
            f"\n  ~$ {sys.argv[0]}"
            f"\n\n  Program to translate GPA to Irish academic grades"
            f"\n\n    0 - 4    GPA value between 0 and 4"
            f"\n    exit     Quit the program"
            f"\n    help     Instruction on how to use this program"
            f"\n    quit     Quit the program"
    )
    return h


# END function help()

# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #

# START function main()


def main():
    """main() function"""

    # Declare local variables
    flag = 0

    while True:

        # help() the first time the program is run
        if flag == 0:
            print(help_())
            flag += 1

        # Input from user of GPA grade
        cli = input("\nEnter GPA score (0-4): ")

        # Look for exit or quit, gradeful exit
        if cli == "quit" or cli == "exit":
            print("\n   Goodbye ...\n")
            sys.exit(0)

        # Look for help request
        elif cli == "help":
            print(help_())
            continue

        # Test that the value supplied is a float/integer (0-4)
        try:
            gpa = float(cli)
        except ValueError:
            # Handle case where conversion fails
            print("Invalid GPA input: Please enter a float or integer between 0 and 4")
            continue

        # Test for numbers outside range
        if gpa > 4:
            print("\nMaximum GPA in 4.0, try again")
            continue

        # Send valid numbers for processing to computegrade()
        (presentage, grade) = computegrade(gpa)

        # Print output
        print(
            f"GPA        : {gpa}",
            f"\nPresentage : {presentage}%",
            f"\nGrade      : {grade}",
        )


# END function main()

# ========================================== #
# //          Global environment          // #
# ========================================== #

# Call main function

if __name__ == "__main__":
    main()
else:
    sys.exit(1)

# Exit program

sys.exit(0)

# END
