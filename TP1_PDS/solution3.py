def celsius_to_fahrenheit(c, round_to=1):
    f=c*(9/5)+32
    return f
def fahrenheit_to_celsius(f,round_to=1):
    c=(f-32)*(5/9)
    return c
print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(32))