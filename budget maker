ans = 'y'
while ans[0] == 'Y' or ans[0] == 'y': 
    income = float(input('Please enter the amount of money you made on this paycheck: '))
    owed = float(input('Enter money owed this month (Bills, personal, etc.): '))
    pcent = float(input('Enter percent you would like to put into savings after owed money is paid: '))
    pcent = pcent*.01
    inv_pcent = float(input('Enter percent you would like to invest: '))
    inv_pcent = inv_pcent*.01
    left1 = income - owed
    savings = left1*pcent
    left2 = left1 - savings
    invst = left2*inv_pcent
    left3 = left2 - invst

    ov_pcent = 100-pcent+inv_pcent

    '''if pcent+inv_pcent+ov_pcent > 100:'''
        
    
    print()
    print('               ===***===  ALFONSO PROGRAMMING SOLUTIONS  ===***===')
    print()
    
    print('Initial income is: ',income)
    print()
    print('Initial income minus money owed: ',owed)
    print()
    print('Money left after: ',round(left1,2))
    print()
    print('Amount of money to put into savings: ',round(savings,2))
    print()
    print('Amount left after savings deposit: ',round(left2,2))
    print()
    print('Amount of money to put into investments: ',round(invst,2))
    print()
    print('Amount left after investment deposit: ',round(left3,2))
    ans2 = input('Would you like to add this amount to your accounts? ')
    if ans2[0] == 'y' or ans2[0] == 'Y':
        chking = float(input('Enter amount in Checkings: '))
        svings = float(input('Enter amount in Savings: '))
        print()
        print('New total amount in Checkings: ',chking+left3)
        print('New total amount in Savings: ',svings+savings)
        print()
        ans = str(input('Would you like to do this again? '))
    else:
        ans = str(input('Would you like to do this again? '))

print('Thank you for using this program!')
