price = float(input('Price: '))
payment = float(input('Payment: '))

change = round(payment-price)
print('Change: ', change)

re = change//1000
print('1000kr bills: ', re)

change = change%1000
re = change//500
print('500kr bills: ', re)

change = change%500
re = change//200
print('200kr bills: ', re)

change = change%200
re = change//100
print('100kr bills: ', re)

change = change%100
re = change//50
print('50kr bills: ', re)

change = change%50
re = change//20
print('20kr bills: ', re)

change = change%20
re = change//10
print('10kr coins: ', re)

change = change%10
re = change//5
print('5kr coins: ', re)

change = change%5
re = change//2
print('2kr coins: ', re)

change = change%2
re = change//1
print('1kr coins: ', re)