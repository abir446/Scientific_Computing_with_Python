fname = input("Enter a file name: \n")

try:
    fhand = open(fname)
except:
    print("Wrong file name entered: ",fname)
    quit()

for line in fhand:
    line = line.strip()
    print(line.upper())