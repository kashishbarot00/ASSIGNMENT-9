def comptuition(credithrs, districtcode):
    if districtcode == "I":
        tuitionrate = 250
    elif districtcode == "O":
        tuitionrate = 550
    else:
        tuitionrate = 0
    tuitionowed = credithrs * tuitionrate
    return tuitionowed


name = input("Enter student's name: ")
lname = input("Enter student last name: ")
credithrs = float(input("Enter credit hours: "))
districtcode = input("Enter district code (I for In-district, O for Out-of-district): ")

tuitionowed = comptuition(credithrs, districtcode)

print("Student name: " , name)
print("Tuition owed: $ " , tuitionowed)



