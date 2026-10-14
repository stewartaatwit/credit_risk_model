# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:21:12 2026

@author: ataly
"""

# Starting off small
def debt_income_ratio(monthly_debt_payments, monthly_income):
<<<<<<< HEAD
    
    if monthly_debt_payments<0:
        raise ValueError ("Debt payments can not be negative")
        
    if monthly_income <= 0:
        raise ZeroDivisionError() ("Income must be greater than zero")
        
    
    return(monthly_debt_payments/monthly_income )*100
        
   
        
try:
    
    user_income = int(input('Enter your monthly income:'))
    user_debt = int(input('Enter your debt:'))
    r= debt_income_ratio(user_debt, user_income)
    
except ValueError:
     print("Invalid input. Please enter number") 
 
except ZeroDivisionError:
      print("Income must be greater than zero") 
 
else:
    print(f"Debt-to-income ratio: {r}%")


=======
    if monthly_income <= 0:
        raise ValueError("Monthly income must be greater than zero.")
    
    if monthly_debt_payments < 0:
        raise ValueError("Debt payments cannot be negative.")
    
    return (monthly_debt_payments / monthly_income) * 100


user_income = int(input("Enter your monthly income: "))
user_debt = int(input("Enter your monthly debt payments: "))

r = debt_income_ratio(user_debt, user_income)
print(f"Debt-to-income ratio: {r:.1f}%")
>>>>>>> 4490b9778f6ead28037c3b64912280b7862f74a5
