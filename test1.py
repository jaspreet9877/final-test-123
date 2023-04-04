try:
    # get user input for month, day, and year
    month, day, year = map(int, input("Enter the date in the format 'MM DD YY': ").split())
    
    # check if inputs are valid
    if month < 1 or month > 12:
        raise ValueError("Invalid Month Input")
    if day < 1 or day > 31:
        raise ValueError("Invalid Day Input")
    if year < 0 or year > 99:
        raise ValueError("Invalid Year Input")

    print("Success: Congratulations! you entered the correct date.")
   
    print(f"{month}/{day}/{year:02d}")
    
except ValueError as error:
    # handle invalid inputs
    print(f"Error: {error}")
