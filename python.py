def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Error, please enter a valid number')

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Error, please enter a valid number')

def weekly_compute_pay(hours, rate, Maximum_hours):
    if hours <= Maximum_hours:
        base_pay = (hours * rate)
        return round(base_pay), 0
    else:
        overtime_hours = (hours - Maximum_hours)
        base_pay = ((overtime_hours * (rate * 1.5))+ (Maximum_hours * rate))
        return round(base_pay), overtime_hours

def monthly_compute_pay(hours, rate, Maximum_hours):
    if hours <= Maximum_hours:
        base_pay = ((hours * 4.33) * rate)
        return round(base_pay),0
    else:
        overtime_hours = (hours - Maximum_hours)
        base_pay = ((Maximum_hours * 4.33) * rate)
        return round(base_pay), overtime_hours
    
def get_rating():
    while True:
        try:
            Rating = int(input('Enter Performance Rating (1-5): '))
        except:
            print('Error, please enter a number between 1 and 5')
            continue
        if Rating < 1 or Rating > 5:
            print('please enter a number between 1 and 5')
            continue
        return Rating

def calculate_bonus(Rating, Gross_pay):
    if Rating == 5:
        return  Gross_pay * 0.2
    elif Rating == 4:
        return Gross_pay * 0.1
    else:
        return  0.0


print('---Welcom to the payroll System---')
Name = input('Please Enter Employee Name: ')

Maximum_hours = get_int_input('Enter Maximum hours of work: ')
Hours = get_int_input('Enter Hours of worked: ')
Rate = get_float_input('Enter Rate per Hour: ')

print('Please Select the salary calculation method')
print('---Choose (1) for Monthly or (2)for Weekly---')

while True:
    calculation_method = input('> ')
    if calculation_method in ['1', '2']:
        break
    else:
        print('Invalid choice, please enter 1 or 2:')
        continue


if calculation_method == '1':
    Gross_pay, overtime_hours = monthly_compute_pay(Hours, Rate, Maximum_hours)
elif calculation_method == '2':
    Gross_pay, overtime_hours = weekly_compute_pay(Hours, Rate, Maximum_hours)


rating = get_rating()
bonus = calculate_bonus(rating, Gross_pay)


print('---Employee Sumary---')
print(f'Employee:                  {Name}')
print(f'The Maximum Hours of Work: {Maximum_hours}')
print(f'Amount of Work Hours:      {Hours}')
print(f'The over Time Work:        {overtime_hours}')
print(f'Rate per Hour:             {Rate:.2f}')

if calculation_method == '1':
    print (f'Time Bank Hours Added:    {overtime_hours} hours')
    print(f'Gross Pay per Month:       {Gross_pay}')
elif calculation_method == '2':
    print(f'The overtime Bonus Pay:    {overtime_hours * (Rate * 1.5)}')
    print(f'Gross Pay per Week:        {Gross_pay}')

print(f'The Rating Bonus:      {round(bonus)}')

print(f'Total Pay:             {Gross_pay + round(bonus)}')