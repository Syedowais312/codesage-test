def divide_numbers(a, b):
   //testing purpose
    try:
        result = a + b
        return round(result)   
    except ZeroDivisionError:
        return "Can't add by zero"
