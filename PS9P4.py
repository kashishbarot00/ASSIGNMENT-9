def comppayrate(jobcode):
    if jobcode == "L":
        return 25
    elif jobcode == "A":
        return 30
    elif jobcode == "J":
        return 50
    else:
        return 0

def compgrosspay(hours, payrate):
    if hours <= 40:
        grosspay = hours * payrate
    else:
        overtime = hours - 40
        otpayrate = payrate * 1.5
        regularpay = 40 * payrate
        otpay = overtime * otpayrate
        grosspay = regularpay + otpay
    return grosspay

lname = input("Enter last name: ")
jobcode = input("Enter job code (L, A, J): ")
hours = float(input("Enter hours worked: "))

payrate = comppayrate(jobcode)
grosspay = compgrosspay(hours, payrate)

print("Last name:", lname)
print("Gross pay: $", grosspay)


