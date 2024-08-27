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


#class income? year, amount?
#method calculateincome? year1 year2 return income?
#method calculatemaxincome?  methuselah start end?

#method generatetext?

jeff_bezos = Methuselah ("Jeff Bezos", 
                         {2015:34800000000, 
                          2016:35200000000,
                          2017:72800000000,
                          2018:112000000000,
                          2019:131000000000,
                          2020:113000000000,
                          2021:177000000000,
                          2022:171000000000,
                          2023:114000000000})

def investment_iterate(initial, monthly, profit, target):
    current = initial
    current_months = 0
    while target > current:
        current += monthly
        #print (f"month {current_months} begins at {current}")
        current = current*(1 + ((profit/100)/12))
        #print (f"and ends at {current}")
        current_months += 1
    return current_months


initial_investment = 1000
monthly_investment = 200
monthly_profit = 7
#months = investment_iterate(initial_investment, monthly_investment, monthly_profit, jeff_bezos.income2021)

for year in jeff_bezos.income_history:
    print (f"in {year} {jeff_bezos.name} earned ${jeff_bezos.income_history[year]}")
#print(f"{jeff_bezos.name} earned ${jeff_bezos.income2021} in 2021. To earn as much at a yearly yield of {monthly_profit}% with an initial investment of ${initial_investment} and a monthly investment of ${monthly_investment} would take {months} months, which is equivalent to {months/12} years.") 




