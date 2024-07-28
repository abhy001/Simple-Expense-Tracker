#importing libraries
import numpy as np
import pandas as pd
from datetime import date

#creating empty lists
GOODS_OR_SERVICES= []
PRICES = []
DATES=[]
EXPENSE_TYPES=[]

#function definition
def add_expenses(goods_service, price, date, expense_type):
    GOODS_OR_SERVICES.append(goods_service)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)

#main program
choice=-1
while(choice !=6):
    print('         Welcome to SIMPLE EXPENSE TRACKER          ')
    print('----------------------------------------------------------')
    print('1.Add Food expense')
    print('2.Add Transportation expense')
    print('3.Add GF expense')
    print('4.Add other expense')
    print('5.Show and Save expense report')
    print('6.Exit')
    print()#newline
    choice= int(input('Choose an option:'))

    if choice==6:
        print('Exitting the Program, Bye')
        break
    elif choice==1:
        print('Adding FOOD')
        expense_type= 'FOOD'
    elif choice==2:
        print('Adding TRANSPORTATION')
        expense_type= 'TRANSPORTATION'
    elif choice==3:
        print('Adding GF')
        expense_type= 'GF'

    elif choice==4:
        print('Adding OTHER')
        expense_type= 'MISC'
    elif choice==5:
        #creating DataFrame
        expense_report = pd.DataFrame()
        #assigning colums and datas into it
        expense_report['GOODS/SERVICE']= GOODS_OR_SERVICES
        expense_report['PRICE']=PRICES
        expense_report['DATE']=DATES
        expense_report['EXPENSE TYPE']= EXPENSE_TYPES
        #Saving the expense_report
        expense_report.to_csv('expenses.csv')
        #Show the report
        print(expense_report)
        break
    else:
        print('You have chosen an invalid option')

    if choice==1 or choice==2 or choice==3 or choice==4:
        goods_or_service= input('Enter the goods or service: ')
        price= float(input('Enter the cost: '))
        today= date.today()
        add_expenses(goods_or_service, price, today, expense_type)
        print()


    








        

    


