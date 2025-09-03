def divide_numbers(a, b):
   
    try:
        result = a / b
        return round(result)   
    except ZeroDivisionError:
        return "Can't divide by zeroooooooooooo"
