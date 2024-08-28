import math

class Methuselah:
    def __init__(self, name, worth_history):
        self.name = name
        self.worth_history = worth_history
        self.income_history = calculate_income_history(self.worth_history)
    
def calculate_income_history(worth_history):
    income_history={}
    for key in worth_history:
        if key-1 in worth_history:
            income_history[key]=worth_history[key]-worth_history[key-1]
    return income_history


#method calculatemaxincome?  methuselah start end?

#method generatetext?

theflask = Methuselah ("Jeff Bezos", 
                         {2015:34800000000, 
                          2016:35200000000,
                          2017:72800000000,
                          2018:112000000000,
                          2019:131000000000,
                          2020:113000000000,
                          2021:177000000000,
                          2022:171000000000,
                          2023:114000000000})

therot = Methuselah ("Elon Musk", 
                         {2015:12000000000, 
                          2016:10700000000,
                          2017:13900000000,
                          2018:11900000000,
                          2019:22300000000,
                          2020:24600000000,
                          2021:151000000000,
                          2022:219000000000,
                          2023:180000000000})

thebot = Methuselah ("Mark Zuckerberg", 
                         {2015:33400000000, 
                          2016:44600000000,
                          2017:56000000000,
                          2018:71000000000,
                          2019:62300000000,
                          2020:54700000000,
                          2021:97000000000,
                          2022:67300000000,
                          2023:64400000000})

def investment_months_iterate(principal, monthly, profit, target):
    current = principal
    current_months = 0
    while target > current:
        current += monthly
        #print (f"month {current_months} begins at {current}")
        current = current*(1 + ((profit/100)/12))
        #print (f"and ends at {current}")
        current_months += 1
    return current_months

def investment_total_iterate(principal, monthly, profit, time_months):
    total = principal
    i=time_months
    while i > 0:
        total += monthly
        total = total * (1 + ((profit/100)/12))
        print (f"month {time_months-i} ends at {total}")
        i -= 1
        
    return total


avotoast_price = 12
latte_price = 5
weeks_in_a_month = 4

avocado_toasts = int(input("How many avocado toasts do you have a week?: "))
lattes = int(input ("How about lattes?: "))
monthly_investment = weeks_in_a_month* ((avotoast_price * avocado_toasts) + (latte_price * lattes))
print (f"monthly investment = {monthly_investment}")
principal_investment = int(input ("How much do you have on your spending account right now?: $"))
yearly_profit = int(input ("On a scale of 1-7, How lucky do you think you are?: "))
age = int(input ("How old are you?: "))
retirement = int(input ("At what age would you like to retire?: "))
period = retirement - age

print (f"""given a yearly yield of {yearly_profit}% (note: a consistent yield of 7% is considered excellent for an investment),
avocado toasts costing ${avotoast_price} and lattes costing ${latte_price}, 
you could save ${investment_total_iterate(principal_investment, monthly_investment, yearly_profit, period * 12)} 
for retirement simply by investing all of your spending money and the money you spend monthly on your millenial vices!""")

#months = investment_iterate(initial_investment, monthly_investment, monthly_profit, jeff_bezos.income2021)
#print(f"{jeff_bezos.name} earned ${jeff_bezos.income2021} in 2021. To earn as much at a yearly yield of {monthly_profit}% with an initial investment of ${initial_investment} and a monthly investment of ${monthly_investment} would take {months} months, which is equivalent to {months/12} years.") 




