while True:
    income = int(input('Please provide monthly income: '))
    if income <= 38000:
        tax = income*0.3
        print('Corresponding income tax: ', tax)
    elif income > 38000 and income <= 50000:
        tax = 38000*0.3+(income-38000)*0.35
        print('Corresponding income tax: ', tax)
    elif income > 50000:
        tax = 38000*0.3+(50000-38000)*0.35+(income-50000)*0.40
        print('Corresponding income tax: ', tax)
