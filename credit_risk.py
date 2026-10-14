# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:21:12 2026

@author: ataly
"""
#starting off small
def debt_income_ratio(monthly_debt_payments, monthly_income):
    if(monthly_debt_payments == 0 or monthly_income == 0):
        return ZeroDivisionError()
    
    return (monthly_debt_payments/monthly_income )*100

    

user_income = int(input('Enter your monthly income:'))
user_debt = int(input('Enter your debt:'))
r= debt_income_ratio(user_debt, user_income)
print(f"Debt-to-income ratio: {r}%")


