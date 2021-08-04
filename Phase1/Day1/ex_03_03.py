try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate : "))

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
    print(total_pay)
except NameError and ValueError as e:
    print(e)
