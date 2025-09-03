def divide_numbers(a, b):
   //creating a new branch
    try:
        result = a / b
        return round(result)   
    except ZeroDivisionError:
        return "Can't divide by zero"
