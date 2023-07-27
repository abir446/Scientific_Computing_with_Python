# sts = 'Hello'

# print(sts[:4]) #Slicing

"Concat"

# a = "HEllo"

# b = a + " There"

# print(b)

# if 'm' in "i am her":
#     print("True")
# else:
#     print("False")

# "Comparing:"
# word = 'banama'
# if word == 'banana':
#     print("All right, Banana")
# elif word < 'banana':
#     print(word+ ' banana')
# else:
#     print('banana '+word)

"Lower Case"
# word = input("Enter your name\n")
# word = word.lower()
# print(word)

"Find"
# word = 'banana'
# pos = word.find('z')
# print(pos)

# greet = "Hello Abir"
# print(greet.upper())

"Replace"

# name = "Hello Moto"
# print(name.replace('Moto','Abir'))


"Strip"
# hi = ' What are you doing?'
# print(hi.strip())

"Simple example of extracting data:"

data = "From Abir.rpba@nit.ac.in Sat Jan 09:14:16 2003"
dataAT = data.find('@')
# print(dataAT)
last = data.find(' ',dataAT)
# print(last)

required = data[dataAT+1 : last]
print(required)