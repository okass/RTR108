def computepay(h,r):
    above = 0
    normal = h
    if (h > 40):
        above = h - 40
        normal = 40
    return (normal * r + above * r * 1.5)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)