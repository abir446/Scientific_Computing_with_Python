smallest = None

for i in [2,53,12,54,63,223]:
    if smallest is None:
        smallest = i
    if i<smallest:
        smallest = i
    
print(smallest)