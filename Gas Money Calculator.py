############################################################################

def work(work_type):
        work_type == work_type.lower()
        global miles
        global miles_total
        if work_type == 'costco' or work_type[0] == 'c':
            miles = 25
            miles_total = -1
        else:
            miles_total = float(input('Enter amount of miles you did this week: '))
            miles_total = round(miles_total,2)
            
############################################################################
            
def mpg(car_type):
        car_type == car_type.lower()
        global mpg2
        if car_type == 'camry' or car_type[0] == 'c':
            mpg2 = 24
        elif car_type == 'rav4' or car_type[0] == 'r':
            mpg2 = 24
        elif car_type == 'van' or car_type[0] == 'v':
            mpg2 = 20
        else:
            mpg2 = float(input('Please enter a custom mpg: '))
            print()
            
############################################################################

ans = input('Would you like to calculate how much gas money you owe? ')
print()
ans = ans.lower()
while ans[0] == 'y':
    car_type = str(input('What car did you use this week? If not typical car, type other car: '))
    print()
    mpg(car_type)

    work_type = input('Where did you work this week? If not saved in code, type other to type custome number of miles: ')

    if work_type == 'costco' or work_type[0] == 'c':
        work_traveled = float(input('How many times did you go to work this week: '))
        print()

        work(work_type)
        print()
        gas_cost = float(input('How much does a gallon cost right now: '))

        if miles_total >= 0:
            money_owed = (miles_total/mpg2)*gas_cost
        else:
            miles_total = miles*work_traveled
            money_owed = (miles_total/mpg2)*gas_cost
    
        print()
    
        print('You owe: ',round(money_owed,2))
        print()

    else:
        work(work_type)
        print()
        gas_cost = float(input('How much does a gallon cost right now: '))

        if miles_total >= 0:
            money_owed = (miles_total/mpg2)*gas_cost
        else:
            miles_total = miles*work_traveled
            money_owed = (miles_total/mpg2)*gas_cost
    
        print()
    
        print('You owe: ',round(money_owed,2))
        print()

    ans = input('Would you like to do this again? ')
    ans = ans.lower()
    print()
    
else:
    print('Thank you for using our program!')
