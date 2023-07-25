nn = input("Enter the number of times you want to run the loop: \n")

try:
    n = int(nn)
except:
    print("Please enter a valid integer.")
    quit()

while (n>0):
    print(n)
    n-=1
print("Blast Off!")
print(n)