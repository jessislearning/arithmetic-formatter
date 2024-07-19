def arithmetic_arranger(problems, show_answers=False):

    # Checking for Error 1: too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
        #raise ValueError("Error: Too many problems.")

    # Split the equation into A +/- B format:
    A = []
    operator = []
    B = []
    for equation in problems:
        equation_parts = equation.split()
        A.append(equation_parts[0])
        operator.append(equation_parts[1])
        B.append(equation_parts[2])
    
    # Checking for Error 2 : Operator must be '+' or '-'.
    acceptable_char = "+-"
    for char in operator:
        if char not in acceptable_char:
            return "Error: Operator must be '+' or '-'."
            #raise ValueError("Error: Operator must be '+' or '-'.")

    # Checking that numbers A and B are numeric and contains a max of 4 digits     
    for numbers_a in A:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_a.isdigit() == False:
            return "Error: Numbers must only contain digits."
            #raise ValueError("Error: Numbers must only contain digits.")
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_a) > 4:
            return "Error: Numbers cannot be more than four digits."
            #raise ValueError("Error: Numbers cannot be more than four digits.")
   
    for numbers_b in B:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_b.isnumeric() == False:
            return "Error: Numbers must only contain digits."
            #raise ValueError("Error: Numbers must only contain digits.")
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_b) > 4:
            return "Error: Numbers cannot be more than four digits."
            #raise ValueError("Error: Numbers cannot be more than four digits.")
            
    #----Formatting begins here----

    # Determine the max_length and store it to a list
    digit_length = []
    for i in range(len(A)):
        if len(A[i]) >= len(B[i]):
            digit_length.append(len(A[i]))
        else:
            digit_length.append(len(B[i]))
    
    # maximum line length per equation is max_length = digit_length + 2
    max_length = [x + 2 for x in digit_length]

    # creating empty strings where numbers, operator and summation lines will be added
    line1 = ""
    line2 = ""
    line3 = ""
    counter = 0

    # concatenating A, operator, B and summation lines following the required format
    for a in A:
        line1 = line1 + a.rjust(max_length[counter]) + "    "
        line2 = line2 + operator[counter] + " " + B[counter].rjust(max_length[counter]-2) + "    "
        line3 = line3 + ("-" * max_length[counter]) + "    "
        counter+=1  

    # removing the trailing
    line1_clean = line1.rstrip()
    line2_clean = line2.rstrip()
    line3_clean = line3.rstrip()

    # putting together each line and outputting the problems in the correct
    arranged_problems = f"{line1_clean}\n{line2_clean}\n{line3_clean}"

    return arranged_problems
    #print(problems)
