from models import Plant, Employee

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees\n5. Edit plant\n 6. Edit employee")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        plants = Plant.get_all()
        for plant in plants:
            print(plant["name"])
            print(plant["address"])
            print("=========================================================")
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        plant_id = int(input("Plant id: "))
        employee = Employee(name, email, plant_id)
        employee.save()
    elif flag == 4:
        employees = Employee.get_all()
        for employee in employees:
            print(employee["name"])
            print(employee["email"])
            print(employee["plant_id"])
            print("=========================================================")
    elif flag == 5:
        id = int(input("Enter id plant to edit: "))
        Plant.edit_plant(id)
    elif flag == 6:
        id = int(input("Enter id employee to edit: "))
        Employee.edit_employee(id)
    else:
        print("Don`t have this menu item")