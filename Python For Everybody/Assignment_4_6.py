def computepay(h,r):

    if h>40:
        rate1=(r*1.5)*(h-40)

    pay=((h-5)*r)+rate1
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
p = computepay(hrs,rate)
print("Pay",p)
