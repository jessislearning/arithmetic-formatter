def arithmetic_arranger(problems, show_answers=False):

    """
    This arithmetic arranger takes a maximum of A +/- B problems and arranges them
    vertically (e.g. "vertical method" of solving arithmetic problems). 
    - maximum of 5 problems
    - each number must only have 4 digits
    - only addition and subtraction allowed
    - with the option of including the sum/difference

    formatting conditions include:
    -single space between operator and B
    -numbers are right indented
    -the distance between vertical equations is 4 spaces

    for example, an input of ["32 + 200"] should ouput:
       32
    + 200
    -----

    """

    # Checking for Error 1: too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

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

    # Checking that numbers A and B are numeric and contains a max of 4 digits     
    for numbers_a in A:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_a.isdigit() == False:
            return "Error: Numbers must only contain digits."
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_a) > 4:
            return "Error: Numbers cannot be more than four digits."
   
    for numbers_b in B:
        # Checking for Error 3 : operands must only contain numbers
        if numbers_b.isnumeric() == False:
            return "Error: Numbers must only contain digits."
        
        # Checking for Error 4 : operands have more than 4 digits
        if len(numbers_b) > 4:
            return "Error: Numbers cannot be more than four digits."

    #----Solving for the sum or difference----#

    #convert the strings into integers
    A_int = []
    B_int = []

    for string_a in A:
       A_int.append(int(string_a))

    for string_b in B:
       B_int.append(int(string_b))

    # determining whether to add or subtract A +/-B and determining the result
    sum_order = 0
    sum_list = []
    sum_str = []
    for sign in operator:
        if sign == "+":
            sum=A_int[sum_order] + B_int[sum_order]
        else:
            sum=A_int[sum_order] - B_int[sum_order]
        
        sum_order+=1
        sum_list.append(sum)

    # return the sum into a string to prepare for formatting
    for sum in sum_list:
        sum_str.append(str(sum))
                
    #----Formatting begins here----#

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
    line4 = ""

    # concatenating A, operator, B and summation lines following the required format
    counter = 0
    for a in A:
        line1 = line1 + a.rjust(max_length[counter]) + "    "
        line2 = line2 + operator[counter] + " " + B[counter].rjust(max_length[counter]-2) + "    "
        line3 = line3 + ("-" * max_length[counter]) + "    "
        line4 = line4 + sum_str[counter].rjust(max_length[counter]) + "    "
        counter+=1  

    # removing the trailing
    line1_clean = line1.rstrip()
    line2_clean = line2.rstrip()
    line3_clean = line3.rstrip()
    line4_clean = line4.rstrip()

    # putting together each line and outputting the problems in the correct format (including whether to show answer or not)
    if show_answers == True:
        arranged_problems = f"{line1_clean}\n{line2_clean}\n{line3_clean}\n{line4_clean}"
    else:
        arranged_problems = f"{line1_clean}\n{line2_clean}\n{line3_clean}"
    
    
    return arranged_problems
    
