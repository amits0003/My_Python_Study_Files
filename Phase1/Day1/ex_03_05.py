def computePay(hours, rate):
    time = 0

    pay = 0

    extra_pay = 0

    while time <= hours:
        if time == 40:
            pay = 40 * rate

        if time == hours:
            extra_pay = 1.5 * (hours - 40) * rate

        time = time + 1

    total_pay = pay + extra_pay

    return total_pay


hours = input("Enter Hours: ")
rate = input("Enter Rate par hour: ")

h = float(hours)
r = float(rate)
p = computePay(h, r)
print("Pay", p)
