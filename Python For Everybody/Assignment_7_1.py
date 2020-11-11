fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lines= line.strip()
    print(lines.upper())
