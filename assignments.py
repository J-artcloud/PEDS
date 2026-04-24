def celsius_to_fahrenheit(c):
    result = (9/5) * c + 32
    return result 

output=celsius_to_fahrenheit(32)
print(output)
##fahrenheit to celsius
def fahrenheit_to_celsius(f):
    result = (5/9) * (f-32)
    return result
output=fahrenheit_to_celsius(89.6)
print(output)
