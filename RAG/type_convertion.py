data = ["42", "3.14", "True", "100", "hello"]

print (f"{"Original":<10} {"converted":<10} {"type":<10}")
print ("-" * 30)

for values in data:
    try:
        #integer values 
        if values.isdigit ():
            converted = int (values)

        # boolean
        elif values == "True" or values == "False":
            converted = bool(values)

        # float

        elif '.' in values:
            converted = float (values)

        else:
            converted =  (values)
        print(f"{values:<10} {str(converted):<10} {type(converted).__name__:<10}")

    except ValueError:
        print(f"{values:<10} Conversion failed") 
    