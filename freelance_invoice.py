#Entries 

#Names
while True:
    name = input('Enter your name: ').strip()

    if not name:
        print('Input field is empty. Please enter you corrent name')
    elif not all(part.isalpha() for part in name.split()):  # allows spaces
        print('Invalid name. Names cannot have numbers or symbols in them. Enter your correct name.')
    else:
        name = name.title()
        break
        
#Region
while True:
    country = input('Where are you from (EU/USA): ').upper()

    if country == "EU" or country == "USA":
        break
    else:
        print('Only USA and EU employees are allowed')

#Hourly Rate
while True:
    try:
        hourly_rate = int(input('Your hourly rate: '))
        break
    except ValueError:
        print('Invalid input! Please enter whole numbers')


#Work Hours
while True:
    try:
        hours_worked = int(input('Hours worked: '))
        break
    except ValueError:
        print('Invalid input! Please enter whole numbers')

print()


def payable():

    subtotal = hourly_rate * hours_worked

    if country == "USA":
        salary = subtotal + (subtotal * 0.05)
        sign = "$"
        tax = "TAX (5%)"
        add_ons = (subtotal * 0.05)
    elif country == 'EU':
        salary = subtotal + (subtotal * 0.20)
        sign = "€"
        tax = "VAT (20%)"
        add_ons = (subtotal * 0.20)
    
    if salary > 1000:
        service_fee = 50
    else:
        service_fee = 0
    
    final_salary = subtotal + add_ons + service_fee
    return subtotal, salary, service_fee, final_salary, sign, tax, add_ons

subtotal, salary, service_fee, final_salary, sign, tax, add_ons = payable()

print('|FREELANCE INVOICE|')

print()

print('Client: ', name)
print('Region: ', country) 

print()

print(f'Hourly Rate: {sign}{hourly_rate}')
print('Hours Worked:', hours_worked)

print()

print(f'Subtotal: {sign}{subtotal}')
print(f'{tax}: {sign}{add_ons}')
print(f'Service Fee: {sign}{service_fee}')

print()

print(f'TOTAL PAYABLE: {sign}{final_salary}')

