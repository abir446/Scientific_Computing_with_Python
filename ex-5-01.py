num = 0
tot= 0

while True:
    sval = input("Enter a number: ")
    
    if sval == 'done':
        break

        
    
    
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        continue
    
    num+=1
    tot+=fval
    
print("All done")
print(tot,num,tot/num)