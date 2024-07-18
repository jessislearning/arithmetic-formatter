def arithmetic_arranger(problems):
    
    # Checking for Error 1: too many problems
    if len(problems) > 5:
        #return "Error: Too many problems."
        raise ValueError("Error: Too many problems.")

    # Split the equation into A (operand) B format:
    A = []
    operator = []
    B = []
    for equation in problems:
        equation_parts = equation.split()
        A.append(equation_parts[0])
        operator.append(equation_parts[1])
        B.append(equation_parts[2])
    
    #print(A, operator, B)
        # the strategy here is putting the split elements into lists
        # the lists should be line1 (containing A), operator (+/-), line2 (containing B)

    # Checking for Error 2 : Operator must be '+' or '-'.
    acceptable_char = "+-"
    for char in operator:
        if char not in acceptable_char:
            #return "Error: Operator must be '+' or '-'."
            raise ValueError("Error: Operator must be '+' or '-'.")

    # Checking that numbers A and B are numeric and contains a max of 4 digits 
    for numbers_a in A:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_a.isnumeric() == False:
            #return "Error: Numbers must only contain digits."
            raise ValueError("Error: Numbers must only contain digits.")
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_a) > 4:
            #return "Error: Numbers cannot be more than four digits."
            raise ValueError("Error: Numbers cannot be more than four digits.")

    for numbers_b in B:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_a.isnumeric() == False:
            #return "Error: Numbers must only contain digits."
            raise ValueError("Error: Numbers must only contain digits.")
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_b) > 4:
            #return "Error: Numbers cannot be more than four digits."
            raise ValueError("Error: Numbers cannot be more than four digits.")

    return arranged_problems
