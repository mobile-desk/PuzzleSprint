total_cost = float(input("Cost of your dream home: "))
current_savings = 0.00
r = 0.04
#current_savings*r/12
annual_salary = float(input("Enter your starting annual salary: "))

portion_saved = float(input("Portion of salary to be saved (float): "))
months = 0
portion_down_payment = total_cost * 0.25
semi_annual_raise = float(input("Input a semi-annual salary raise (float): "))



while (portion_down_payment > current_savings):
    monthly_salary = annual_salary / 12
    
    current_savings = current_savings + (current_savings * r / 12) + (portion_saved * monthly_salary) 
    
    months += 1
    if months % 6 == 0:
        f = annual_salary * semi_annual_raise
        annual_salary += f
        
   
   
     
        
    
    
print(months) 