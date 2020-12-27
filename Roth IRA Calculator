#Calculator that computes the returns of an investment for retirement#

import matplotlib.pyplot as plt

ans = 'yes'
while  ans.lower() == 'yes' or ans.lower() == 'y':
    print()
    svings = float(input('Please enter the amount of money in your savings: '))
    sve_amt = float(input('Please enter the amount of money you would like to save each month: '))
    pcent = float(input('Enter percent you think investment will grow each year: '))
    pcent = pcent*.01
    print()
    int_age = float(input('Enter how old you are: '))
    ret_age = float(input('Enter age you would like to retire: '))

    int_age = round(int_age)
    ret_age = round(ret_age)
    
    new_sve = svings
    new_sve2 = svings

    while int_age > ret_age:
        print()
        ret_age = int(input("Invalid age. Please type in new retirement age: "))

    print()
    print()
    print('               ===***===  ALFONSO PROGRAMMING SOLUTIONS  ===***===')
    print()

    print()
    print("Age",int_age,"savings: ", '{:,}'.format(svings))

    x = []
    y = []
    x2 = []
    y2 = []
            
    for i in range(int_age+1,ret_age+1):
            new_sve = (new_sve + sve_amt*12) + ((new_sve + sve_amt*12)*pcent)
            new_sve2 = (new_sve2 + sve_amt*12)
            print("Age", i, "savings: ", '{:,}'.format(round(new_sve,2)))
            x.append(i)
            x2.append(i)
            y.append(new_sve)
            y2.append(new_sve2)
            i+1

    years = ret_age - int_age
    amt_inv = ((years+1)*(sve_amt*12))
    amt_md = new_sve - amt_inv

    plt.plot(x,y)
    plt.plot(x2,y2)
    plt.show()

    print()
    print("Amount Invested (Not including what you already had in savings): ",'{:,}'.format(round(amt_inv,2)))
    print()
    print("Amount made from investment: ",'{:,}'.format(round(amt_md,2)))
    print()

    ans = str(input('Would you like to do this again? (Answer Yes or No): '))

    while ans.lower() != 'yes' and ans.lower() != 'no' and ans.lower() != 'y' and ans.lower() != 'n':
            print()
            ans = str(input('Invalid input. Please answer Yes or No: '))
        
print()
print('Thank you for using this program!')
