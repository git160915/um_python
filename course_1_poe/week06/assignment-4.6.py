def computepay(h, r):
    pay = 0.0

    if h > 40.0 :
        pay = 40 * r
        pay = pay + ((h - 40.0) * r * 1.5)
    else :
        pay = h * r

    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs, rate)
print("Pay", p)