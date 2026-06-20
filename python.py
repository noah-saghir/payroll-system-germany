def weekly_compute_pay(hours, rate, Maximum_hours):
    if hours <= Maximum_hours:
        base_pay = (hours * rate)
        return int(base_pay), 0
    else:
        overtime_hours = (hours - Maximum_hours)
        base_pay = ((overtime_hours * (rate * 1.5))+ (Maximum_hours * rate))
        return int(base_pay), overtime_hours


def monthly_compute_pay(hours, rate, Maximum_hours):
    if hours <= Maximum_hours:
        base_pay = ((hours * 4.33) * rate)
        return int(base_pay),0
    else:
        overtime_hours = (hours - Maximum_hours)
        base_pay = (((hours - overtime_hours) * 4.33) * rate)
        return int(base_pay), overtime_hours


print('---Welcom to the payroll System---')
Name = input('Please Enter Employee Name: ')
try:
    Maximum_hours = int(input('Enter Maximum hours of work: '))
    Hours = int(input('Enter Hours of worked: '))
    Rate = int(input('Enter Rate per Hour: '))
except:
    print('Error, please enter a valid number')
    quit()

print('Please Select the salary calculation method')
print('---Choose (1) for Monthly or (2)for Weekly---')

while True:
    calculation_method = input()
    if calculation_method in ['1', '2']:
        break
    else:
        print('Invalid choice, please enter 1 or 2:')
        continue


if calculation_method == '1':
    Gross_pay, overtime_hours = monthly_compute_pay(Hours, Rate, Maximum_hours)
elif calculation_method == '2':
    Gross_pay, overtime_hours = weekly_compute_pay(Hours, Rate, Maximum_hours)


Bonus = 0
while True:
    try:
        Rating = int(input('Enter Performance Rating (1-5): '))
    except:
        print('Error, please enter a number between 1 and 5')
        continue
    if  Rating < 1 or Rating > 5:
        continue
    elif Rating == 5:
        Bonus = Gross_pay * 0.2
        break
    elif Rating == 4:
        Bonus = Gross_pay * 0.1
        break
    else:
        Bonus = 0.0
        break

#_, m_overtime = monthly_compute_pay(Hours, Rate, Maximum_hours)
#_, w_overtime = weekly_compute_pay(Hours, Rate, Maximum_hours)

print('---Employee Sumary---')
print('Employee:', Name)
print('The Maximum Hours of Work:', Maximum_hours)
print('Amount of Work Hours:', Hours)
print('The over Time Work:', overtime_hours)
print('Rate per Hour:', Rate)

if calculation_method == '1':
    print (f'Overtime hours added to your Time Bank for future time-off: {overtime_hours} hours')
    print('Gross Pay per Month:', Gross_pay)
elif calculation_method == '2':
    print('The Bonus overtime Rate: ', (overtime_hours * (Rate * 1.5)))
    print('Gross Pay per Week:', Gross_pay)

print('The Rating Bonus Rate:', int(Bonus))

print('Total Pay:', Gross_pay + int(Bonus))
