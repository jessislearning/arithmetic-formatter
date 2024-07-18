def arithmetic_arranger(problems):
    # Error 1: too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Error 2: operator is not + or -
    acceptable_char = "0123456789-+ "
    for equation in problems:
        for char in equation:
            if char not in acceptable_char:
                return "Error: Operator must be '+' or '-'."
            
    # Error 3: operands must only contain numbers
    # Error 4: operands have more than 4 digits

    #split the equation into A (operand) B format:
    separated = []
    for equation in problems:
        separated.append(equation.split())
    
    #print(separated)

    return arranged_problems
