profit_percen = 23 / 100
totalsales = float(input('Enter the predicted sales = '))
profit = totalsales * profit_percen
profit = round(profit, 2)
profit = '{:0,.2f}'.format(profit)
print("The predicted total sales of this year is " +
      str(profit))

for i in range(2024, 2035):
    totalsales = totalsales + ((totalsales * 5) / 100)
    profit = totalsales * profit_percen
    profit = round(profit, 2)
    profit = '{:0,.2f}'.format(profit)
    print("The profit of year " + str(i) +
          " is " + str(profit))
