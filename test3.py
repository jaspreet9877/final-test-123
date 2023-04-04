def convertSalary(salary, to_country):
    conversion_rates = {'Canada': 1, 'USA': 1.18, 'Cambodia': 4847.38, 'United Kingdom': 0.91}
    
    if to_country not in conversion_rates:
        print("Invalid country input!")
        return None
    
    try:
        salary = float(salary.replace(',', ''))
    except ValueError:
        print("Invalid salary input!")
        return None
    
    rate = conversion_rates[to_country]
    if to_country == 'Canada':
        currency_name = 'CAD'
        avg_salary = 64000
    elif to_country == 'USA':
        currency_name = 'USD'
        avg_salary = 56516
    elif to_country == 'Cambodia':
        currency_name = 'Cambodian riel'
        avg_salary = 5649856
    else:
        currency_name = 'Pound Sterling'
        avg_salary = 35423
    
    converted_salary = salary / rate
    
    if converted_salary > avg_salary:
        print(f"You will be rich in {to_country} with a salary of {converted_salary:.2f} {currency_name}")
    else:
        print(f"You will be poor in {to_country} with a salary of {converted_salary:.2f} {currency_name}")
    
    return converted_salary
