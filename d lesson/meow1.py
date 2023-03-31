print('Write one of the types of temperature measure: Kelvin, Fahrenheit, Celsius')
n = input()
print('Write what type of temperature you want to convert')
m = input()
print('Write temperature')
t = int(input())
if n == 'Kelvin':
    if m == 'Celsius':
        print(t - 273.15)
    elif m == 'Fahrenheit':
        print(32 + t * 9/5 - 459.67) 
if n == 'Celsius':
    if m == 'Fahrenheit':
        print(t * 9/5 + 32) 
    elif m == 'Kelvin':
        print(t + 273.15)  
if n == 'Fahrenheit':
    if m == 'Celsius':
        print((t - 32) * 5/9)
    elif m == 'Kelvin':
        print((t + 459.67) * 5/9)            