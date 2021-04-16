# Henry Nguyen
# Integration Project
# Everything I've learned in COP 1500

"""My Integration Project"""
__author__ = "Henry"


# Adds two numbers
def do_addition():
    """This function will ask the user for two numbers and add them. It will
    also test whether the user inputted numbers or not"""
    # Tests the code for errors
    try:
        a_first_number = input("Enter first number ")
        a_second_number = input("Enter second number ")
        a_num_1 = int(a_first_number)
        a_num_2 = int(a_second_number)
    except:
        print("Please enter a number")
        a_first_number = input("Enter first number ")
        a_second_number = input("Enter second number ")
        a_num_1 = int(a_first_number)
        a_num_2 = int(a_second_number)
    print("Answer =", a_num_1 + a_num_2)


# Subtracts two numbers
def do_subtraction():
    """This function will ask the user for two numbers and subtract them. It
    will also test whether the user inputted numbers or not"""
    try:
        s_first_number = input("Enter first number ")
        s_second_number = input("Enter second number ")
        s_num_1 = int(s_first_number)
        s_num_2 = int(s_second_number)
    except:
        print("Please enter a number")
        s_first_number = input("Enter first number ")
        s_second_number = input("Enter second number ")
        s_num_1 = int(s_first_number)
        s_num_2 = int(s_second_number)
    print("Answer =", s_num_1 - s_num_2)


# Multiplies two numbers
def do_multiplication():
    """This function will ask the user for two numbers and multiply them. It
    will also test whether the user inputted numbers or not"""
    try:
        m_first_number = input("Enter first number ")
        m_second_number = input("Enter second number ")
        m_num_1 = int(m_first_number)
        m_num_2 = int(m_second_number)
    except:
        print("Please enter a number")
        m_first_number = input("Enter first number ")
        m_second_number = input("Enter second number ")
        m_num_1 = int(m_first_number)
        m_num_2 = int(m_second_number)
    print("Answer =", m_num_1 * m_num_2)


# Divides two numbers
def do_division():
    """This function will ask the user for two numbers and divide them. It
        will also test whether the user inputted numbers or not"""
    try:
        d_first_number = input("Enter first number ")
        d_second_number = input("Enter second number ")
        d_num_1 = int(d_first_number)
        d_num_2 = int(d_second_number)
    except:
        print("Please enter a number")
        d_first_number = input("Enter first number ")
        d_second_number = input("Enter second number ")
        d_num_1 = int(d_first_number)
        d_num_2 = int(d_second_number)
    while d_num_2 == 0:
        print("Cannot divide by zero, please enter a different number")
        d_num_2 = int(input("Enter second number "))
    print("Answer =", d_num_1 / d_num_2)
    # // will only give an integer and % will only give a remainder
    # Gives remainder and answers without decimals
    print("This program can also give you the remainder")
    print("Remainder =", d_num_1 % d_num_2)
    print("This program can also give only an integer")
    print("Without decimal =", d_num_1 // d_num_2)


# Asks user for input to create a rectangle
def make_rectangle():
    """This function will ask the user for the height, length and what they
    want the rectangle to be made of. If the user tries to make a square a
    message will pop up and not allow them to"""
    num = int(input("Enter height of rectangle: "))
    rows = int(input("Enter length of rectangle: "))
    while num == rows:
        # Won't let user make a square if user chooses rectangle
        print("Why would you choose rectangle and try to make a square?")
        print("Try again please")
        num = int(input("Enter height of rectangle: "))
        rows = int(input("Enter length of rectangle: "))
    symbol = input("What symbol would you like the shape to be made of? ")
    for col in range(1, num + 1):
        for row in range(1, rows + 1):
            print(symbol, end=" ")
        print()


# Asks user for input to create a square
def make_square():
    """This function will ask the user for the height, length and what they
    want the square to be made of. If the user tries to make a rectangle a
    message will pop up and not allow them to"""
    num = int(input("Enter height of square: "))
    rows = int(input("Enter length of square: "))
    while num > rows or num < rows:
        # Won't let user make a rectangle if user chooses square
        print("Why would you choose square and try to make a rectangle?")
        print("Try again please")
        num = int(input("Enter height of square: "))
        rows = int(input("Enter length of square: "))
    symbol = input("What symbol would you like the shape to be made of? ")
    for row in range(1, rows + 1):
        for col in range(1, num + 1):
            print(symbol, end=" ")
        print()


# Asks user for input to create a triangle
def make_triangle():
    """This function will ask the user for the height and what they want the
    triangle to made of."""
    print("I can only make right triangles")
    height = int(input("Enter height of triangle: "))
    symbol = input("What symbol would you like the shape to be made of? ")
    for row in range(1, height + 1):
        for column in range(row):
            print(symbol, end=" ")
        print()


# Asks user to choose a shape to create
def choose_shape(shape):
    """This function asks the user to choose what shape they want to create"""
    if shape == "rectangle":
        make_rectangle()
        input("Would you like to choose a different shape? ")
    elif shape == "square":
        make_square()
        input("Would you like to choose a different shape? ")
    elif shape == "triangle":
        make_triangle()
        input("Would you like to choose a different shape? ")


def main():
    """This is the start of the program"""
    print("Welcome to my integration project")
    name = input("What is your name? ")
    # * in a string will repeat the word before it
    print("Hello", name * 5)
    input("\nENTER to continue\n")
    print("Sorry ", end='I am just a little excited!\n')
    input("\nENTER to continue\n")
    # + in a string will put the two together
    print(name + " this project will go through everything I've learned in "
                 "COP 1500")
    input("\nENTER to continue\n")
    print(name + " If you are asked a question answer with either a yes or no")
    input("\nENTER to continue\n")

    # + in a integer will add two numbers
    print("This program will add two numbers")
    input("\nENTER to continue\n")
    do_addition()
    input("\nENTER to continue\n")

    # - will subtract two numbers
    print("This program will subtract two numbers")
    input("\nENTER to continue\n")
    do_subtraction()
    input("\nENTER to continue\n")

    # * will multiply two numbers
    print("This program will multiply two numbers")
    input("\nENTER to continue\n")
    do_multiplication()
    input("\nENTER to continue\n")

    # / will divide two numbers
    print("This program will divide two numbers")
    input("\nENTER to continue\n")
    do_division()
    input("\nENTER to continue\n")

    print("Now that we got all the basic stuff out of the way")
    print("Lets do something more complex!")
    print("This program will calculate compound interest")
    input("\nENTER to continue\n")
    print("The formula of compound interest is: A=P(1+r/n)^nt")
    print("This program can only find A")
    var_p = input("Enter P ")
    var_r = input("Enter r ")
    var_n = input("Enter n ")
    var_t = input("Enter t ")
    num_p = int(var_p)
    num_r = float(var_r)
    num_n = int(var_n)
    num_t = int(var_t)
    # ** is an exponent
    # Shows compound interest formula with user inputs
    print(
        "A=" + var_p + "(1+" + var_r + "/" + var_n + ")^" + "(" + var_n + ")" +
        "(" + var_t + ")")
    answer = input("Are you sure you want these numbers? ")
    if not answer == "yes" or answer == "Yes":
        while answer == "no" or answer == "No":
            var_p = input("Enter P ")
            var_r = input("Enter r ")
            var_n = input("Enter n ")
            var_t = input("Enter t ")
            num_p = int(var_p)
            num_r = float(var_r)
            num_n = int(var_n)
            num_t = int(var_t)
            # Displays the formula with user input
            print(
                "A=" + var_p + "(1+" + var_r + "/" + var_n + ")^" +
                "(" + var_n + ")" + "(" + var_t + ")")
            answer = input("Are you sure you want these numbers? ")
    # Does the actual calculation of compound interest
    print("A=", num_p * (1 + num_r / num_n) ** (num_n * num_t))

    input("\nENTER to continue\n")
    print(
        "What if you want to know the price of buying one item several times?")
    num_items = int(input("Enter the number of items: "))
    item_cost = float(input("Enter the cost of one item: "))
    total_cost = num_items * item_cost
    # Formats the total cost of item
    print("Total cost: $", format(total_cost, "0.2f"), sep='')
    input("\nENTER to continue\n")

    print("I can also calculate college semester GPA")
    classes = int(input("How many classes are you taking? "))
    class_num = int(1)
    grade_point = 0
    credit_score = 0
    print("Answer with letter grade in capitals")
    input("\nENTER to continue\n")
    # Calculates college GPA
    for x in range(1, classes + 1):
        class_num = str(class_num)
        grade = (input("What is your grade in class " + class_num + ": "))
        if grade == "A":
            grade = float(4.00)
        elif grade == "A-":
            grade = float(3.70)
        elif grade == "B+":
            grade = float(3.30)
        elif grade == "B":
            grade = float(3.00)
        elif grade == "B-":
            grade = float(2.70)
        elif grade == "C" or grade == "C-":
            grade = float(2.00)
        elif grade == "D":
            grade = float(1.00)
        elif grade == "F":
            grade = float(0.00)
        weight = grade
        credit = int(input(
            "How many credits do you receive from class " + class_num + ": "))
        credited = credit
        weight *= credited
        grade_point += weight
        credit_score += credit
        class_num = int(class_num)
        class_num += 1
    gpa = (grade_point / credit_score)
    print("Your college GPA is: ", format(gpa, "0.2f"), sep=" ")
    if (credit_score >= 13) and (gpa >= 2.0):
        print("Congrats!")
        print("You are on your way to graduation.")
    else:
        print("You are behind on graduation, work hard!")
    input("\nENTER to continue\n")

    print("Math calculations aren't the only thing I learned though")
    print("I can also make shapes")
    input("\nENTER to continue\n")
    print("I can make a rectangle, square, or triangle")
    shape = input("Which shape would you like? ")
    if shape == "rectangle":
        make_rectangle()
        answer = input("Would you like to choose a different shape? ")
    elif shape == "square":
        make_square()
        answer = input("Would you like to choose a different shape? ")
    elif shape == "triangle":
        make_triangle()
        answer = input("Would you like to choose a different shape? ")
    else:
        while shape != "rectangle" or shape != "square" or shape != "triangle":
            print("You have chosen an invalid word")
            print("Please try again")
            shape = input("Choose a shape again ")
            choose_shape(shape)
    while answer == "yes" or answer == "Yes":
        shape = input("Choose a different shape ")
        if shape == "rectangle":
            make_rectangle()
            answer = input("Would you like to choose a different shape? ")
        elif shape == "square":
            make_square()
            answer = input("Would you like to choose a different shape? ")
        elif shape == "triangle":
            make_triangle()
            answer = input("Would you like to choose a different shape? ")
    input("\nENTER to continue\n")
    print(name + " that is basically everything I've learned in COP 1500")
    input("\nENTER to continue\n")
    print("It has been an extremely fun class! Huge thanks to "
          "Professor Vanselow for teaching me!")


main()
