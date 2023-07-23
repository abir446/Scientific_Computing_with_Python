hours = input("Enter the hours you work in a week: ")
rate = input("Enter the rate of your work: ")

fh = float(hours)
fr = float(rate)

if (fh>20.0):
    pay = (fh * fr) + 10
    print("Extra money added.")
else:
    pay = (fh * fr)
    print("No extra money added.")

print("Your total pay: ",pay)
