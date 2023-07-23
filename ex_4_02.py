def ComputePay(hours,rate):
    pay = hours * rate
    return pay

hours = input("Enter the hours you work in a week: ")
rate = input("Enter the rate of your work: ")

try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Please enter a numeric value.")
    quit()

pay = ComputePay(fh,fr)



print("Your total pay: ",pay)
