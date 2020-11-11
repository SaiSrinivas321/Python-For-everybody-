score = float(input("Enter Score: "))

if score>=0.9 and score<=1.0:
    grade="A"
elif score>=0.8:
    grade="B"
elif score>=0.7:
    grade="C"
elif score>=0.6:
    grade="D"
elif score>=0.0 and score<0.6:
    grade="F"
else:
    print("Out of range")
    quit()

print(grade)
