# fhand = open('file-handle.txt')
# count = 0
# for line in fhand:
#     count += 1
#     print(line)

# print("The number of lines in file: ",count)


# Searching in file

# fhand = open('file-handle.txt')
# # inp = fhand.read()
# for line in fhand:
#     line = line.strip()#Rmoving the '\n'
#     if line.startswith('I'):
#         pos = line.find('I')
#         print(line[pos + 1:6])


#Searching method 2: E.g: Finding email addresses in text

fname = input("Enter a file name:\n")
try:
    fhand = open(fname)
except:
    print("File: ",fname, "doesn't exist.")
    quit()
for line in fhand:
    line = line.strip()
    if '@gmail.com' not in line:
        continue
    print(line)