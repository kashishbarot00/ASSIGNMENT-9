def compmpg(miles, gallons):
    mpg = miles / gallons
    return mpg

def compcost(gallons):
    cost = gallons * 2.5
    return cost

city = input("Enter destination city: ")
miles = float(input("Enter miles traveled: "))
gallons = float(input("Enter gallons used: "))

mpg = compmpg(miles, gallons)
cost = compcost(gallons)

print("Destination city:", city)
print("Miles per gallon:", mpg)
print("Cost of gas: $", cost)

