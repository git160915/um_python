hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
pay = 0.0

if h > 40.0 :
    overtime_r = r * 1.5
    pay = 40.0 * r
    pay = pay + ((h % 40) * r * 1.5)
else :
    pay = h * r

print(pay)