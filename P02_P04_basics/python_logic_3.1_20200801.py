hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
rate = float(rt)

normal_hours = 0
extra_hours = 0

if h > 40:
    extra_hours = h - 40
    normal_hours = 40
else:
    normal_hours = h

pay = (normal_hours * rate) + (extra_hours * rate * 1.5)
print(pay)