
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
coffee = float(input('1 coffee @: $ '))
countCoffee = 2.0 * coffee ;

# Modify the line below
sandwich = float(input('1 sandwich @: $ '))

countSand = 4.99 * sandwich ;

# Modify the line below
cake = float(input('1 cake @: $ '))

countCake = 2.75 * cake 

bill_total = countCoffee + countCake + countSand

print('Your total bill is $', float(bill_total))