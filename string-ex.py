str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':')

pr = str[pos+1:]
pr = pr.strip()

try:
    fpr = float(pr)
except:
    print("Wrongly Done")
    quit()

print(fpr+10)