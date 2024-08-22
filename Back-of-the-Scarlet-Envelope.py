class Methuselah:
    def __init__(self, name, worth2021, worth2020):
        self.name = name
        self.worth2021 = worth2021
        self.worth2020 = worth2020
        self.income2021 = self.worth2021 - self.worth2020

jeff_bezos = Methuselah ("Jeff Bezos", 177000000000, 113000000000)

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
months = investment_iterate(initial_investment, monthly_investment, monthly_profit, jeff_bezos.income2021)

print(f"{jeff_bezos.name} earned ${jeff_bezos.income2021} in 2021. To earn as much at a yearly yield of {monthly_profit}% with an initial investment of ${initial_investment} and a monthly investment of ${monthly_investment} would take {months} months, which is equivalent to {months/12} years.") 




