fname = input("Enter file name: ")
fh = open(fname)
count=0
avg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    ind=line.find(":")
    num=line[(ind+2):]
    num=float(num)
    avg=avg+num

print("Average spam confidence:",avg/count)
